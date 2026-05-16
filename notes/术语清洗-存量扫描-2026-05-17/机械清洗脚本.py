#!/usr/bin/env python3
"""
按术语映射表 v3 对 notes 中的笔记做机械替换。

设计要点:
1. 替换列表按 token 长度降序(确保 "anchor formulation drift" 在 "anchor" 之前匹配)
2. 保护区不替换:
   - fenced code blocks (```...```)
   - inline code (`...`)
   - markdown 链接 URL 部分 (](...))
   - 裸 URL (https://...)
3. F 区允许项不在替换列表中,自然不会被触动:
   - AI / LLM (大写形式)
   - State 后接 A/B/C/D 字母 (映射表里"state"不替换)
   - Layer 后接数字(已在替换列表里→"层",字母保留)
   - 梵文(unicode 不会被 [a-zA-Z] 匹配)
4. 不在映射表的英文词原样保留,供后续映射表增补
"""

import re
import sys
from pathlib import Path

# ============================================================
# 替换列表(按 token 长度降序排列)
# 格式: (英文正则, 中文替换)
# ============================================================

REPLACEMENTS = [
    # ===== reveal 特殊规则(日期 + reveal → 删 reveal 字) =====
    # 必须在 \breveal\b 之前
    (r"(\d{4}-\d{2}-\d{2})\s+reveal\b", r"\1"),
    (r"(\d{1,2}/\d{1,2})\s+reveal\b", r"\1"),

    # ===== D 区复合术语(优先匹配) =====
    (r"\bfunctional substrate ordering\b", "功能基质排序"),
    (r"\banchor formulation drift\b", "锚表述偏移"),
    (r"\banchor formulation\b", "锚表述"),
    (r"\bphenomenal anchor\b", "身心锚"),
    (r"\bmotion continuity\b", "运动连续性"),
    (r"\bmotion quality\b", "运动质量"),
    (r"\bself-correction\b", "自我修正"),
    (r"\bself-correct\b", "自我修正"),
    (r"\bself-diagnosis\b", "自诊"),
    (r"\bself-report\b", "自陈"),
    (r"\bself-check\b", "自查"),
    (r"\bactor-status\b", "行为者地位"),
    (r"\bnon-imposition\b", "不强加"),
    (r"\bcase-by-case\b", "逐例"),
    (r"\bsign vs target\b", "征兆 vs 标的"),
    (r"\bsign vs\. target\b", "征兆 vs 标的"),
    (r"\btime domain\b", "时间域"),
    (r"\bstate domain\b", "状态域"),
    (r"\bframe anchor\b", "见地锚"),
    (r"\bflow-trap\b", "心流陷阱"),
    (r"\bhot state\b", "热态"),
    (r"\bcool state\b", "冷态"),
    (r"\bnext level\b", "次级"),

    # ===== A 区骨干名词(长度降序) =====
    (r"\bcalibration\b", "校准"),
    (r"\bphenomenal\b", "身心"),
    (r"\bformulation\b", "表述"),
    (r"\bderivation\b", "推导"),
    (r"\bframework\b", "框架"),
    (r"\bbottleneck\b", "瓶颈"),
    (r"\bthreshold\b", "阈值"),
    (r"\bsubstrate\b", "基质"),
    (r"\bdimension\b", "维度"),
    (r"\bmanifest\b", "显现"),
    (r"\bcapacity\b", "承载力"),
    (r"\bframing\b", "框定"),
    (r"\btrigger\b", "触发"),
    (r"\bceiling\b", "上限"),
    (r"\bpattern\b", "模式"),
    (r"\bdomain\b", "域"),
    (r"\bframe\b", "见地"),
    (r"\blayer\b", "层"),
    (r"\bpath\b", "路径"),
    (r"\baxis\b", "轴"),

    # ===== B 区过程动词 =====
    (r"\bcrystallize\b", "结晶化"),
    (r"\bchallenge\b", "挑战"),
    (r"\bdissolve\b", "消解"),
    (r"\benforce\b", "强制"),
    (r"\bmonitor\b", "监测"),
    (r"\bhijack\b", "劫持"),
    (r"\bderive\b", "推出"),
    (r"\bresolve\b", "闭合"),
    (r"\bretire\b", "退役"),
    (r"\bescape\b", "漂移逃逸"),
    (r"\bconfirm\b", "确认"),
    (r"\binvoke\b", "调用"),
    (r"\bground\b", "立基"),
    (r"\bverify\b", "验证"),
    (r"\breduce\b", "归约"),
    (r"\bunpack\b", "拆解"),
    (r"\bshift\b", "跃迁"),
    (r"\bdrift\b", "偏移"),
    (r"\breframe\b", "重置框架"),
    (r"\bpush\b", "深挖"),
    (r"\bhold\b", "成立"),
    (r"\blift\b", "拔高"),
    (r"\banchor\b", "锚"),  # 长度最短,必须最后
    (r"\bfit\b", "嵌合"),

    # ===== C 区修饰词 =====
    (r"\bphenomenological\b", "现象学的"),
    (r"\bretroactive\b", "回溯性"),
    (r"\bstructurally\b", "结构上"),
    (r"\bontological\b", "本体论的"),
    (r"\bstructural\b", "结构性"),
    (r"\bunprompted\b", "无外引"),
    (r"\bconfirmed\b", "已确认"),
    (r"\bspontaneous\b", "自发"),
    (r"\bqualified\b", "有限定"),
    (r"\bplausible\b", "看似可信"),
    (r"\bbaseline\b", "基准"),
    (r"\bcandidate\b", "候选"),
    (r"\bspecial\b", "特殊"),
    (r"\bspecific\b", "具体"),
    (r"\bsomatic\b", "身体层"),
    (r"\bpositive\b", "正面"),
    (r"\bnegative\b", "负面"),
    (r"\binternal\b", "内部"),
    (r"\bcurrent\b", "当前"),
    (r"\bhealthy\b", "健康"),
    (r"\bhybrid\b", "混合"),
    (r"\bexplicit\b", "明文"),
    (r"\btrivial\b", "微不足道"),
    (r"\breactive\b", "反应式"),
    (r"\bactive\b", "活跃"),
    (r"\bstable\b", "稳态"),
    (r"\bstrong\b", "强"),
    (r"\bfinal\b", "最终"),
    (r"\blevel\b", "层级"),
    (r"\bouter\b", "外部"),
    (r"\bstep\b", "步"),
    (r"\broot\b", "根"),
    (r"\bmeta\b", "元"),
    (r"\bdual\b", "双"),

    # ===== D 区原子术语 =====
    (r"\btransmission\b", "传承"),
    (r"\bcontinuity\b", "连续性"),
    (r"\bdirectional\b", "方向"),
    (r"\bfunctional\b", "功能性的"),
    (r"\bamplitude\b", "振幅"),
    (r"\bchecklist\b", "核查清单"),
    (r"\bintuition\b", "直觉"),
    (r"\bimposing\b", "强加"),
    (r"\bmechanism\b", "机制"),
    (r"\bpartition\b", "切分"),
    (r"\brestoration\b", "复位"),
    (r"\bretention\b", "保持"),
    (r"\bevidence\b", "证据"),
    (r"\bmapping\b", "映射"),
    (r"\bordering\b", "排序"),
    (r"\bmarkers\b", "标记"),
    (r"\binsight\b", "洞见"),
    (r"\beffort\b", "用力"),
    (r"\bmotion\b", "运动"),
    (r"\bmarker\b", "标记"),
    (r"\bready\b", "就绪"),
    (r"\breset\b", "重置"),
    (r"\bslot\b", "槽位"),
    (r"\bsink\b", "吸入口"),
    (r"\bstub\b", "占位"),
    (r"\bgap\b", "缺口"),

    # ===== v4 增补(2026-05-17,步骤 3 第一波) =====
    # D 区推出
    (r"\bactor\b", "行为者"),  # 由 actor-status=行为者地位 推出
    (r"\bsign\b", "征兆"),     # 由 sign vs target 推出(裸用)
    (r"\btarget\b", "标的"),   # 同上(裸用)
    # 新增基础词
    (r"\bphenomenology\b", "现象学"),
    (r"\bdispositional\b", "倾向性的"),
    (r"\bculture\b", "文化"),
    (r"\bverbal\b", "言语的"),
    (r"\bforcing\b", "强行"),
    (r"\bagency\b", "能动性"),
    (r"\bpartial\b", "部分"),
    (r"\bdesign\b", "设计"),
    (r"\bimage\b", "形象"),
    (r"\blabel\b", "标签"),
    (r"\bshame\b", "惭"),
    (r"\bguilt\b", "愧"),
    (r"\bfaith\b", "信"),
    (r"\bbase\b", "基础"),
    (r"\bpain\b", "疼痛"),
    (r"\bmin\b", "分钟"),
    # bug 修:reveal 裸用(date+reveal 已在最顶部特殊规则处理)
    (r"\breveal\b", "揭示"),
]

# ============================================================
# 保护区(不替换)
# ============================================================

SKIP_PATTERNS = [
    re.compile(r"```.*?```", re.DOTALL),           # fenced code
    re.compile(r"`[^`\n]+`"),                       # inline code
    re.compile(r"\]\([^)]+\)"),                     # markdown link URL
    re.compile(r"https?://\S+"),                    # bare URLs
]


def find_protected_ranges(text: str) -> list[tuple[int, int]]:
    """找出所有保护区间(不参与替换),合并重叠。"""
    ranges = []
    for pat in SKIP_PATTERNS:
        for m in pat.finditer(text):
            ranges.append((m.start(), m.end()))
    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append([start, end])
    return [(s, e) for s, e in merged]


def apply_replacements(text: str, replacements) -> str:
    """对单段文本应用所有替换。"""
    for pat, repl in replacements:
        text = re.sub(pat, repl, text)
    return text


def clean_file(text: str) -> tuple[str, int]:
    """处理整篇文本,返回 (新文本, 替换次数估算)。"""
    protected = find_protected_ranges(text)

    parts = []
    pos = 0
    original_eng_count = len(re.findall(r"[a-zA-Z]{3,}", text))

    for start, end in protected:
        editable = text[pos:start]
        editable = apply_replacements(editable, [(re.compile(p), r) for p, r in REPLACEMENTS])
        parts.append(editable)
        parts.append(text[start:end])
        pos = end

    tail = text[pos:]
    tail = apply_replacements(tail, [(re.compile(p), r) for p, r in REPLACEMENTS])
    parts.append(tail)

    new_text = "".join(parts)
    new_eng_count = len(re.findall(r"[a-zA-Z]{3,}", new_text))

    return new_text, original_eng_count - new_eng_count


def main():
    if len(sys.argv) < 2:
        print("用法: python3 notes_terminology_cleaner.py <file1> [file2] ...", file=sys.stderr)
        sys.exit(1)

    total_replaced = 0
    for fp in sys.argv[1:]:
        path = Path(fp)
        if not path.exists():
            print(f"文件不存在: {fp}", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        cleaned, replaced = clean_file(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            print(f"✓ {fp}: {replaced} 处英文词被替换")
            total_replaced += replaced
        else:
            print(f"- {fp}: 无变更")

    print(f"\n总计替换: {total_replaced} 处")


if __name__ == "__main__":
    main()
