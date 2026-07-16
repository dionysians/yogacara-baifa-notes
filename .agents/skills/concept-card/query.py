#!/usr/bin/env python3
"""Query existing concept cards under resources/cards/.

Usage:
  query.py list
  query.py lookup <name>
  query.py lookup-batch <name1> <name2> ...

Outputs JSON. Cards are parsed by reading YAML-ish frontmatter
(name, type, aliases). Minimal parser — no external deps.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CARDS_DIR = Path(__file__).resolve().parents[3] / "resources" / "cards"


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip()
    meta: dict = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            items = [i.strip().strip("'\"") for i in inner.split(",") if i.strip()]
            meta[key] = items
        else:
            meta[key] = val.strip("'\"")
    return meta


def load_cards() -> list[dict]:
    cards = []
    if not CARDS_DIR.exists():
        return cards
    for path in sorted(CARDS_DIR.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        meta = parse_frontmatter(text)
        name = meta.get("name") or path.stem
        aliases = meta.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases] if aliases else []
        cards.append({
            "name": name,
            "type": meta.get("type", ""),
            "aliases": aliases,
            "path": str(path.relative_to(CARDS_DIR.parents[1])),
            "filename": path.name,
        })
    return cards


def build_index(cards: list[dict]) -> dict:
    """Map normalized name/alias -> list of (match_kind, card)."""
    idx: dict[str, list[tuple[str, dict]]] = {}
    for c in cards:
        idx.setdefault(c["name"], []).append(("exact", c))
        for a in c["aliases"]:
            idx.setdefault(a, []).append(("alias", c))
    return idx


def lookup(query: str, idx: dict) -> dict:
    hits = idx.get(query, [])
    if not hits:
        return {"query": query, "match": "none"}
    exact_hits = [h for h in hits if h[0] == "exact"]
    alias_hits = [h for h in hits if h[0] == "alias"]
    if exact_hits and alias_hits:
        return {
            "query": query,
            "match": "conflict",
            "note": "name in one card, alias in another — model must resolve",
            "candidates": [
                {"kind": k, "canonical_name": c["name"], "path": c["path"]}
                for k, c in hits
            ],
        }
    if len(hits) > 1:
        return {
            "query": query,
            "match": "conflict",
            "note": "multiple cards share this name/alias",
            "candidates": [
                {"kind": k, "canonical_name": c["name"], "path": c["path"]}
                for k, c in hits
            ],
        }
    kind, card = hits[0]
    return {
        "query": query,
        "match": kind,
        "canonical_name": card["name"],
        "path": card["path"],
        "type": card["type"],
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    cards = load_cards()
    if cmd == "list":
        print(json.dumps({"count": len(cards), "cards": cards}, ensure_ascii=False, indent=2))
        return 0
    idx = build_index(cards)
    if cmd == "lookup":
        if len(argv) < 3:
            print(json.dumps({"error": "lookup requires a name"}))
            return 1
        print(json.dumps(lookup(argv[2], idx), ensure_ascii=False, indent=2))
        return 0
    if cmd == "lookup-batch":
        results = [lookup(q, idx) for q in argv[2:]]
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    print(json.dumps({"error": f"unknown command: {cmd}"}))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
