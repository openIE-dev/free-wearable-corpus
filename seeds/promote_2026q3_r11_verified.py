#!/usr/bin/env python3
"""promote_2026q3_r11_verified.py — third FDA+patent verification round.

Verified via FDA accessdata records and Google Patents (Apple assignee
search):

  - Medtronic MiniMed CGMS (1999) → FDA PMA **P980022** (the first FDA-
    approved continuous glucose monitor; PMA confirmed in multiple FDA
    documents citing P980022 / P980022/S071).
  - Apple Watch (1st gen, 2015) → representative Apple PPG patent **US
    10,092,197** ("Reflective surfaces for PPG signal detection";
    inventor Chin San Han; assignee Apple Inc.). One representative patent
    of Apple's ~200-family PPG patent estate; promotes the entry while
    leaving room for further enumeration.

Run from repo root:  python3 seeds/promote_2026q3_r11_verified.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-15"


UPDATES = {
    "medtronic-minimed-cgms-1999": {
        "ip_citations": ["P980022"],
        "regulatory_pathway": "fda-pma",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA PMA P980022 (MiniMed Continuous "
            "Glucose Monitoring System) — approved 1999, the first FDA-approved "
            "continuous glucose monitor. PMA referenced across multiple FDA documents "
            "(P980022, P980022/S071, ...). Direct commercialization of "
            "[[shichiri-1982-wearable-needle-glucose-sensor]] (1982)."
        ),
    },
    "apple-watch-original-2015": {
        "ip_citations": ["US10092197B2"],
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Patent enumerated (one representative): US 10,092,197 B2, 'Reflective "
            "surfaces for PPG signal detection' (assignee Apple Inc.; inventor Chin San "
            "Han) — covers reflective surfaces around the optical apertures of the wrist "
            "PPG to bounce light back into skin and increase signal. One representative "
            "patent of Apple's ~200-family PPG patent estate; additional enumeration is "
            "still TODO for the foundational Mehta/Hoyt/Crisman early Apple Watch HR "
            "patents and the wrist-back optical-emitter/photodetector geometry patents."
        ),
    },
}


def main():
    if not CORPUS.exists() or not CORPUS.stat().st_size:
        raise SystemExit("ERROR: corpus.jsonl missing or empty")

    entries = []
    seen_ids = []
    for line in CORPUS.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        entry = json.loads(line)
        entries.append(entry)
        seen_ids.append(entry["id"])

    by_id = {e["id"]: e for e in entries}

    updated = []
    missing = []
    for eid, updates in UPDATES.items():
        if eid not in by_id:
            missing.append(eid)
            continue
        e = by_id[eid]
        for k, v in updates.items():
            if v is None:
                if k in e:
                    del e[k]
            else:
                e[k] = v
        updated.append(eid)

    with CORPUS.open("w") as f:
        for eid in seen_ids:
            f.write(json.dumps(by_id[eid], ensure_ascii=False, sort_keys=True) + "\n")

    print(f"  promote r11: updated {len(updated)}; missing {len(missing)}")
    for eid in updated:
        print(f"    promoted: {eid}")


if __name__ == "__main__":
    main()
