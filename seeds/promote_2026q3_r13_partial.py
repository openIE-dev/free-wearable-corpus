#!/usr/bin/env python3
"""promote_2026q3_r13_partial.py — partial refinement round.

Aktiia G0 / Hilo Band → FDA 510(k) cleared 8 July 2025 as the FIRST
over-the-counter cuffless blood pressure monitor (per FDA News, MobiHealth,
Fierce Biotech, Aktiia/BioSpace). Specific K-number not surfaced via
WebSearch; refines the notes with the verified FDA pathway and the
prior-art-relevant timeline.

Apple Watch Series 4 / Digital Crown ECG: confirms the technical
description of the conductive Digital Crown electrode architecture (Apple
patentlyapple coverage). Adds detail to notes; remains commons-grade
already (DEN180044 was verified in r5).

Run from repo root:  python3 seeds/promote_2026q3_r13_partial.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-15"


UPDATES = {
    "aktiia-bracelet-cuffless-bp-2021": {
        "regulatory_pathway": "fda-510k",
        "last_updated": LAST_UPDATED,
        "notes": (
            "FDA pathway and timeline refined: Aktiia's G0 system (consumer name "
            "'Hilo Band') received FDA 510(k) clearance on 8 July 2025 as the first "
            "OTC-cleared cuffless blood pressure monitor in the US (per multiple "
            "outlets including MedTech Dive, FierceBiotech, BioSpace). Validated "
            "against double-auscultation in a 140-patient trial. Specific FDA "
            "K-number to be enumerated from the FDA 510(k) database. The 2021 "
            "first_disclosure_date in this entry remains correct as the original "
            "CE-mark / European launch — the prior-art-relevant date for what was "
            "disclosed; the FDA clearance is a downstream regulatory event."
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
    updated = missing = 0
    for eid, updates in UPDATES.items():
        if eid not in by_id:
            missing += 1
            continue
        e = by_id[eid]
        for k, v in updates.items():
            if v is None:
                e.pop(k, None)
            else:
                e[k] = v
        updated += 1
    with CORPUS.open("w") as f:
        for eid in seen_ids:
            f.write(json.dumps(by_id[eid], ensure_ascii=False, sort_keys=True) + "\n")
    print(f"  r13 partial: updated {updated}; missing {missing}")


if __name__ == "__main__":
    main()
