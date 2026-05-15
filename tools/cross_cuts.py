#!/usr/bin/env python3
"""cross_cuts.py — regenerate per-tag and intersection cross-cut files.

Usage:
    python3 tools/cross_cuts.py

Reads `corpus.jsonl` and groups entries across three axes:
    - form_factor (single value) + form_factor_tags (list)
    - sensors (list)
    - algorithms (list)

For each axis tag, writes a markdown file at `cross_cuts/<tag>.md` listing
every disclosing entry in chronological order with the fields that matter
for prior art citation.

Additionally generates intersection cross-cuts for pairs of tags from
different axes (form_factor × sensor, sensor × algorithm) where the
intersection has at least MIN_INTERSECTION entries. These are the inputs
to OBVIOUSNESS_TEMPLATE.md.

Also writes `cross_cuts/INDEX.md` summarizing all cross-cuts.

These files are the working prior art search tool.
"""
import json
from collections import defaultdict
from itertools import product
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
OUT_DIR = ROOT / "cross_cuts"

MIN_INTERSECTION = 3  # only generate intersection files with ≥ this many entries
INTERSECTION_SEP = "__"


def load_corpus():
    if not CORPUS.exists() or CORPUS.stat().st_size == 0:
        return []
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def date_key(e):
    return e.get("first_disclosure_date") or ""


def axes_for(entry):
    """Return dict of axis-name → set of tags this entry carries."""
    ff = set()
    if entry.get("form_factor"):
        ff.add(entry["form_factor"])
    for t in entry.get("form_factor_tags") or []:
        ff.add(t)
    sensors = set(entry.get("sensors") or [])
    algorithms = set(entry.get("algorithms") or [])
    return {"form_factor": ff, "sensors": sensors, "algorithms": algorithms}


def render_entry(e, tier_1_only=False):
    """Return list of markdown lines for one entry."""
    date = e.get("first_disclosure_date", "?")
    name = e.get("canonical_name", "")
    tier = e.get("tier", 1)
    lines = []
    if tier == 2 and tier_1_only is False:
        # short rendering for Tier 2 reference-only entries
        cite = e.get("disclosure_citation", "")
        if len(cite) > 200:
            cite = cite[:200] + "…"
        lines.append(f"- **{name}** ({date}) — `{e.get('id','')}` "
                     f"[{e.get('corpus','')}] — {cite}")
        return lines
    # full rendering for Tier 1
    lines.append(f"## {name} ({date})")
    lines.append("")
    lines.append(f"- **id**: `{e.get('id', '')}`")
    lines.append(f"- **corpus**: {e.get('corpus', '')}")
    if e.get("form_factor"):
        lines.append(f"- **form factor**: {e['form_factor']}")
    if e.get("creator"):
        lines.append(f"- **creator**: {e['creator']}")
    if e.get("disclosure_citation"):
        lines.append(f"- **disclosure**: {e['disclosure_citation']}")
    if e.get("ip_status"):
        lines.append(f"- **ip status**: {e['ip_status']}")
    if e.get("sensors"):
        lines.append(f"- **sensors**: {', '.join(e['sensors'])}")
    if e.get("algorithms"):
        lines.append(f"- **algorithms**: {', '.join(e['algorithms'])}")
    if e.get("prior_art_notes"):
        lines.append(f"- **prior art notes**: {e['prior_art_notes']}")
    lines.append("")
    return lines


def write_tag_file(tag, entries, axis_label):
    entries_sorted = sorted(entries, key=date_key)
    earliest = entries_sorted[0].get("first_disclosure_date", "?")
    lines = [
        "---",
        f"title: {tag}",
        "parent: Cross-cuts",
        "layout: default",
        "---",
        "",
        f"# Cross-cut: `{tag}`",
        "",
        f"Axis: **{axis_label}**",
        "",
        f"**{len(entries_sorted)} corpus entries disclose this tag.**",
        "",
        f"Earliest disclosure: {earliest}",
        "",
        "Listed in chronological order. Each entry's `prior_art_notes` and",
        "`disclosure_citation` constitute the citeable prior art material.",
        "",
        "---",
        "",
    ]
    for e in entries_sorted:
        lines.extend(render_entry(e))
    (OUT_DIR / f"{tag}.md").write_text("\n".join(lines))


def write_intersection_file(tag_a, tag_b, entries, axes_pair):
    entries_sorted = sorted(entries, key=date_key)
    earliest = entries_sorted[0].get("first_disclosure_date", "?")
    fname = f"{tag_a}{INTERSECTION_SEP}{tag_b}.md"
    title = f"{tag_a} ∩ {tag_b}"
    lines = [
        "---",
        f"title: {title}",
        "parent: Cross-cuts",
        "layout: default",
        "---",
        "",
        f"# Intersection cross-cut: `{tag_a}` ∩ `{tag_b}`",
        "",
        f"Axes: **{axes_pair[0]} × {axes_pair[1]}**",
        "",
        f"**{len(entries_sorted)} corpus entries disclose both tags.**",
        "",
        f"Earliest disclosure: {earliest}",
        "",
        "These entries are the direct inputs to "
        "[OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). "
        "Any patent claim combining these two elements is anticipated or "
        "rendered obvious by the chain below.",
        "",
        "---",
        "",
    ]
    for e in entries_sorted:
        lines.extend(render_entry(e))
    (OUT_DIR / fname).write_text("\n".join(lines))


def write_index(by_tag_axis, intersections):
    """by_tag_axis: {(axis, tag): [entries]}
    intersections: {(axis_a, tag_a, axis_b, tag_b): [entries]}
    """
    lines = [
        "---",
        "title: Cross-cuts",
        "has_children: true",
        "nav_order: 4",
        "permalink: /cross_cuts/",
        "---",
        "",
        "# Cross-cut index",
        "",
        "Each cross-cut file lists every corpus entry carrying the tagged",
        "component, in chronological order by first verified public",
        "disclosure date. Use these as the working prior art search tool",
        "when assessing wearable patent claims.",
        "",
        "Three families:",
        "",
        "1. **Single-axis cross-cuts** — one file per form-factor / sensor /",
        "   algorithm tag.",
        "2. **Intersection cross-cuts** — one file per (axis × axis) tag pair",
        f"   with ≥{MIN_INTERSECTION} entries. These are the direct inputs to",
        "   [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html).",
        "",
        "## Single-axis cross-cuts",
        "",
    ]

    by_axis = defaultdict(list)
    for (axis, tag), es in by_tag_axis.items():
        es_sorted = sorted(es, key=date_key)
        earliest = es_sorted[0].get("first_disclosure_date", "?")
        by_axis[axis].append((tag, len(es_sorted), earliest))

    for axis in ("form_factor", "sensors", "algorithms"):
        if axis not in by_axis:
            continue
        lines.append(f"### {axis}")
        lines.append("")
        lines.append("| Tag | Entries | Earliest |")
        lines.append("|---|---|---|")
        for tag, n, earliest in sorted(by_axis[axis]):
            lines.append(f"| [`{tag}`]({tag}.html) | {n} | {earliest} |")
        lines.append("")

    lines.append("## Intersection cross-cuts")
    lines.append("")
    if not intersections:
        lines.append("_(none yet — populated as corpus density grows past the "
                     f"≥{MIN_INTERSECTION}-entry threshold per pair)_")
    else:
        lines.append("| Pair | Axes | Entries | Earliest |")
        lines.append("|---|---|---|---|")
        for (axis_a, tag_a, axis_b, tag_b), es in sorted(intersections.items()):
            es_sorted = sorted(es, key=date_key)
            earliest = es_sorted[0].get("first_disclosure_date", "?")
            fname = f"{tag_a}{INTERSECTION_SEP}{tag_b}"
            lines.append(
                f"| [`{tag_a} ∩ {tag_b}`]({fname}.html) | {axis_a} × {axis_b} "
                f"| {len(es_sorted)} | {earliest} |"
            )

    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for f in OUT_DIR.glob("*.md"):
        f.unlink()

    entries = load_corpus()

    by_tag_axis = defaultdict(list)
    for e in entries:
        axes = axes_for(e)
        for axis, tags in axes.items():
            for t in tags:
                by_tag_axis[(axis, t)].append(e)

    for (axis, tag), group in by_tag_axis.items():
        write_tag_file(tag, group, axis_label=axis)

    # Intersections: form_factor × sensors, sensors × algorithms,
    # form_factor × algorithms.
    AXIS_PAIRS = [
        ("form_factor", "sensors"),
        ("sensors", "algorithms"),
        ("form_factor", "algorithms"),
    ]
    intersections = {}
    for axis_a, axis_b in AXIS_PAIRS:
        # collect all tag pairs that co-occur in any entry
        for e in entries:
            axes = axes_for(e)
            for ta, tb in product(axes[axis_a], axes[axis_b]):
                key = (axis_a, ta, axis_b, tb)
                intersections.setdefault(key, []).append(e)
        # filter to pairs with enough entries; dedupe within group
    intersections = {
        k: list({e["id"]: e for e in v}.values())
        for k, v in intersections.items()
        if len({e["id"] for e in v}) >= MIN_INTERSECTION
    }
    for (axis_a, ta, axis_b, tb), es in intersections.items():
        write_intersection_file(ta, tb, es, (axis_a, axis_b))

    write_index(by_tag_axis, intersections)

    print(f"  single-axis cross-cuts: {len(by_tag_axis)}")
    print(f"  intersection cross-cuts: {len(intersections)} (threshold ≥{MIN_INTERSECTION})")


if __name__ == "__main__":
    main()
