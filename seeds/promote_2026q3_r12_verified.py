#!/usr/bin/env python3
"""promote_2026q3_r12_verified.py — fourth FDA+patent verification round.

Five verifications via FDA accessdata + Google Patents:

  - Dexcom STS (2006)            → FDA PMA **P050012** (approved 24 Mar 2006)
  - AliveCor KardiaMobile (2012) → FDA 510(k) **K122356** (Dec 2012)
  - Verily/Google smart contact lens (2014)
                                 → **US 8,608,310** ("Wireless powered contact
                                   lens with biosensor"; assignee University
                                   of Washington Center for Commercialization;
                                   inventors Yao, Parviz, Otis, Liao —
                                   foundational patent the Google[X] / Verily
                                   project built on; Parviz and Otis later
                                   moved from UW to Google[X])
  - Withings ScanWatch (2020/21) → FDA 510(k) **K201456** (cleared 12 Oct 2021)
  - VitalConnect VitalPatch (2016)
                                 → FDA 510(k) **K163453**

Also: Abilify MyCite approval date corrected from 13 → 14 November 2017
(remains draft pending NDA/510(k) identifier).

Run from repo root:  python3 seeds/promote_2026q3_r12_verified.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-15"


UPDATES = {
    "dexcom-sts-2006": {
        "ip_citations": ["P050012"],
        "regulatory_pathway": "fda-pma",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA PMA P050012 (Dexcom STS Continuous "
            "Glucose Monitoring System), approval order 24 March 2006 — SSED at "
            "accessdata.fda.gov/cdrh_docs/pdf5/p050012b.Pdf. (The successor STS-7 "
            "is P050012/S001.) Patent enumeration (Dexcom ip_citations beyond the "
            "PMA) still TODO."
        ),
    },
    "alivecor-kardiamobile-2012": {
        "ip_citations": ["K122356"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K122356 (AliveCor Heart "
            "Monitor / KardiaMobile), cleared December 2012 — 510(k) summary at "
            "fda.gov/cdrh/510k/K122356.pdf. The Kardia Band (Apple Watch ECG strap, "
            "2017) is separately K171816 — to enumerate. Patent enumeration also TODO."
        ),
    },
    "verily-google-smart-contact-lens-2014": {
        "ip_citations": ["US8608310B2"],
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Foundational patent identified: US 8,608,310 B2 ('Wireless powered contact "
            "lens with biosensor'; filed 21 Feb 2012; granted 17 Dec 2013; assignee "
            "University of Washington Center for Commercialization; inventors Huanfen "
            "Yao, Babak Amirparviz, Brian Otis, Yu-Te Liao). Parviz and Otis later "
            "founded / led the Google[X] / Verily smart-contact-lens program, so this "
            "is the academic-side foundation that the Verily effort built on. Further "
            "Verily-assigned continuations (e.g. US 9,184,698 and following) remain "
            "TODO. The Verily project was discontinued by Alphabet in November 2018 "
            "after tear/blood glucose correlation proved insufficient."
        ),
    },
    "withings-scanwatch-2020": {
        "ip_citations": ["K201456"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K201456 (Withings ScanWatch), "
            "cleared 12 October 2021 — record at "
            "accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K201456; clearance "
            "letter at accessdata.fda.gov/cdrh_docs/pdf20/K201456.pdf. The 2020 entry "
            "first_disclosure_date is the original announcement (CE-mark date); FDA "
            "clearance landed in October 2021. The first wearable simultaneously cleared "
            "to record ECG and SpO2."
        ),
    },
    "vitalconnect-vitalpatch-2016": {
        "ip_citations": ["K163453"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA 510(k) K163453 (VitalConnect VitalPatch), "
            "cleared 2016 — clearance letter at "
            "accessdata.fda.gov/cdrh_docs/pdf16/K163453.pdf. (Subsequent clearances "
            "include K183078 for extended wear; the 'fifth clearance' was December 2017, "
            "raising wear duration from 96 to 120 hours.) Patent enumeration still TODO."
        ),
    },
    "proteus-abilify-mycite-2017": {
        "first_disclosure_date": "2017-11-14",
        "last_updated": LAST_UPDATED,
        "notes": (
            "FDA approval date refined to 14 November 2017 (Otsuka/Proteus press release "
            "and Otsuka US discover-articles). Remains draft pending the NDA identifier "
            "(aripiprazole tablets with sensor) and the corresponding 510(k) for the "
            "Proteus ingestible event marker / MyCite Patch."
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

    print(f"  promote r12: updated {len(updated)}; missing {len(missing)}")
    for eid in updated:
        print(f"    updated:  {eid}")


if __name__ == "__main__":
    main()
