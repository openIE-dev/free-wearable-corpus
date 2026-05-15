#!/usr/bin/env python3
"""promote_2026q3_r9_verified.py — second promotion round.

Verifications from a second batch of FDA accessdata searches:

  - Omron HeartGuide BP8000-M  → 510(k) **K182166** (cleared Nov 2018)
  - Empatica Embrace            → 510(k) **K181861** (cleared 2018)
  - BioIntelliSense BioSticker  → 510(k) **K191614** (cleared Dec 2019)
  - Given Imaging M2A / PillCam → FDA cleared **1 August 2001** (K-number
                                  still TODO; disclosure_citation tightened)
  - Withings ScanWatch          → FDA cleared **12 October 2021** (K-number
                                  still TODO; entry notes amended)

Run from repo root:  python3 seeds/promote_2026q3_r9_verified.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


UPDATES = {
    "omron-heartguide-2019": {
        "ip_citations": ["K182166"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K182166 (Omron Healthcare, Inc., "
            "BP8000-M HeartGuide); clearance letter dated November 2018; product launched "
            "January 2019. Decision letter at accessdata.fda.gov/cdrh_docs/pdf18/k182166.pdf."
        ),
    },
    "empatica-embrace2-seizure-watch-2018": {
        "ip_citations": ["K181861"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K181861 (Empatica S.r.l., "
            "Embrace physiological-signal-based seizure monitoring system); clearance "
            "2018 (the original Embrace cleared for adults in February 2018; the "
            "Embrace2 variant cleared for children in January 2019). 510(k) summary at "
            "accessdata.fda.gov/cdrh_docs/pdf18/K181861.pdf. Lineage from the MIT Media "
            "Lab EDA-wristband (iCalm/Q sensor) work (Picard et al.). The corresponding "
            "regulatory-bucket entry is [[fda-k181861-empatica-embrace-seizure-system-2018]]."
        ),
    },
    "fda-k181861-empatica-embrace-seizure-system-2018": {
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Verified via FDA 510(k) summary at "
            "accessdata.fda.gov/cdrh_docs/pdf18/K181861.pdf (Empatica S.r.l., 'Embrace' "
            "physiological-signal-based seizure monitoring system, 2018)."
        ),
    },
    "biointellisense-biosticker-2019": {
        "ip_citations": ["K191614"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K191614 (BioIntelliSense, Inc., "
            "BioSticker); clearance December 18, 2019. 510(k) record at "
            "accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K191614; clearance "
            "letter at accessdata.fda.gov/cdrh_docs/pdf19/K191614.pdf. 'First single-use "
            "medical device for up to 30 days of continuous vital signs monitoring.'"
        ),
    },
    "pillcam-given-imaging-2001": {
        "disclosure_citation": (
            "Given Imaging Ltd. (later Medtronic). 'M2A' capsule (subsequently 'PillCam "
            "SB') wireless capsule endoscope, FDA-cleared 1 August 2001 — a swallowable "
            "capsule with a CMOS image sensor, LED illumination, battery and radio that "
            "images the small-bowel mucosa over ~8 hours, transmitting frames to an "
            "external belt-worn receiver/recorder. CE-marked May 2001; renamed PillCam SB "
            "in September 2004."
        ),
        "last_updated": LAST_UPDATED,
        "notes": (
            "FDA clearance date verified as 1 August 2001 (Given Diagnostic Imaging "
            "System / M2A capsule). Exact 510(k) K-number still TODO — search the FDA "
            "510(k) database for Given Imaging clearances in mid-2001 (the first "
            "wireless-capsule-endoscope clearance). Once the K-number is confirmed, "
            "set ip_citations and drop the `draft` flag."
        ),
    },
    "withings-scanwatch-2020": {
        "regulatory_pathway": "fda-510k",
        "last_updated": LAST_UPDATED,
        "notes": (
            "FDA clearance date verified as 12 October 2021 (Withings ScanWatch — the "
            "first wearable simultaneously cleared for ECG/AFib and SpO2). The 2020 "
            "disclosure date in this entry remains correct as the original announcement "
            "/ CE-mark date — the prior-art-relevant date for what was disclosed. The "
            "ScanWatch FDA 510(k) K-number still TODO — search the FDA 510(k) database "
            "for Withings, October 2021. Patent enumeration also TODO."
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
            e = by_id[eid]
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")

    print(f"  promote r9: updated {len(updated)} entries; {len(missing)} missing")
    for eid in updated:
        print(f"    updated:  {eid}")
    for eid in missing:
        print(f"    MISSING:  {eid}")


if __name__ == "__main__":
    main()
