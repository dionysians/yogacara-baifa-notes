#!/usr/bin/env python3
"""
分析 notes/ 下所有 .md 文件的英文词分布。

输出两个维度:
A. 按文件:英文词总数、唯一词数、英文/总字符比例(粗估)
B. 全局:跨所有笔记的英文词频(top N)

排除:
- 历史/归档目录
- code blocks (```...```)
- markdown 链接的 URL/路径部分(保留链接文本)
- 裸文件路径(*.md, https://...)
- AI / LLM(F 区允许)

输出:
- /tmp/notes_eng_by_file.tsv:按文件统计
- /tmp/notes_eng_global_freq.tsv:全局词频
- stdout: 摘要 + 头部表格
"""

import os
import re
import sys
from collections import Counter
from pathlib import Path

NOTES_DIR = "notes"
SKIP_DIRS = {"历史"}
F_AREA_ALLOWED = {"AI", "LLM", "MD"}  # 大小写不敏感比较

WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z\-]{2,}")  # 3+ 字英文 token


def clean_content(text: str) -> str:
    """去除不应计入英文统计的内容:代码块、链接 URL、文件路径。"""
    # 1. 去掉 fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # 2. 行内 code: `...`
    text = re.sub(r"`[^`]+`", "", text)
    # 3. markdown 链接 [text](url) - 保留 text,去 url
    text = re.sub(r"\]\([^)]*\)", "]", text)
    # 4. 裸 URL
    text = re.sub(r"https?://\S+", "", text)
    # 5. 文件路径(含 .md 或 / 多段)
    text = re.sub(r"[\w一-鿿/\-]+\.md\b", "", text)
    # 6. YAML frontmatter(--- ... ---)
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    return text


def extract_words(text: str) -> list[str]:
    """提取英文词 token,过滤 F 区允许项。"""
    words = WORD_RE.findall(text)
    return [w for w in words if w.upper() not in F_AREA_ALLOWED]


def count_total_chars(text: str) -> int:
    """粗估文本总字符数(去空白)。"""
    return len(re.sub(r"\s", "", text))


def main():
    if not Path(NOTES_DIR).exists():
        print(f"目录不存在: {NOTES_DIR}", file=sys.stderr)
        sys.exit(1)

    file_stats = []  # (filepath, eng_total, eng_unique, total_chars, ratio_pct)
    global_counter = Counter()

    for path in Path(NOTES_DIR).rglob("*.md"):
        # 跳过归档目录
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"读取失败: {path} - {e}", file=sys.stderr)
            continue

        cleaned = clean_content(raw)
        words = extract_words(cleaned)
        total_chars = count_total_chars(cleaned)

        if not words:
            continue

        # 估算英文字符占比
        eng_chars = sum(len(w) for w in words)
        ratio_pct = (eng_chars / total_chars * 100) if total_chars > 0 else 0

        file_stats.append(
            (
                str(path),
                len(words),
                len(set(w.lower() for w in words)),
                total_chars,
                ratio_pct,
            )
        )
        global_counter.update(w.lower() for w in words)

    # 排序:按英文词总数降序
    file_stats.sort(key=lambda x: -x[1])

    # 输出按文件 TSV
    with open("/tmp/notes_eng_by_file.tsv", "w", encoding="utf-8") as f:
        f.write("文件\t英文词数\t唯一词\t总字符\t英文占比%\n")
        for fp, cnt, uniq, total, ratio in file_stats:
            f.write(f"{fp}\t{cnt}\t{uniq}\t{total}\t{ratio:.2f}\n")

    # 输出全局词频 TSV
    with open("/tmp/notes_eng_global_freq.tsv", "w", encoding="utf-8") as f:
        f.write("词\t频次\n")
        for word, cnt in global_counter.most_common():
            f.write(f"{word}\t{cnt}\n")

    # ===== 摘要输出 =====
    total_files = len(file_stats)
    total_eng_words = sum(s[1] for s in file_stats)
    total_uniq_words = len(global_counter)

    print(f"==================== 摘要 ====================")
    print(f"扫描文件数(有英文)          : {total_files}")
    print(f"英文词总出现次数             : {total_eng_words:,}")
    print(f"全局唯一英文词数              : {total_uniq_words}")
    print()

    print(f"==================== A. 文件英文密度 TOP 30 ====================")
    print(f"{'#':>3}  {'文件':<55} {'英文词数':>8} {'唯一':>5} {'占比%':>6}")
    for i, (fp, cnt, uniq, _, ratio) in enumerate(file_stats[:30], 1):
        short = fp.replace("notes/", "")
        if len(short) > 53:
            short = "…" + short[-52:]
        print(f"{i:>3}  {short:<55} {cnt:>8} {uniq:>5} {ratio:>5.1f}%")

    print()
    print(f"==================== B. 全局英文词频 TOP 60 ====================")
    print(f"{'#':>3}  {'词':<25} {'频次':>6}")
    for i, (word, cnt) in enumerate(global_counter.most_common(60), 1):
        print(f"{i:>3}  {word:<25} {cnt:>6}")

    print()
    print(f"完整 TSV:")
    print(f"  - /tmp/notes_eng_by_file.tsv      (按文件)")
    print(f"  - /tmp/notes_eng_global_freq.tsv  (全局词频)")


if __name__ == "__main__":
    main()
