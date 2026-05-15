#!/usr/bin/env python3
"""promote_2026q3_r10_pubmed.py — attach verified PubMed PMIDs to academic entries.

According to PubMed (https://pubmed.ncbi.nlm.nih.gov), 13 of the corpus's
academic foundational entries have been verified by exact-author/title
queries and metadata fetches. Each entry's `ip_citations` is updated with
the canonical `PMID:NNNNNN` identifier (a stable third-party-attested
citation a patent examiner can pull directly from the National Library of
Medicine). For three entries, the `first_disclosure_date` is also refined
to the earlier 'epub ahead of print' / online-publication date returned by
PubMed (the prior-art-relevant date is the earlier disclosure).

Run from repo root:  python3 seeds/promote_2026q3_r10_pubmed.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"

# Each tuple: (entry_id, PMID, optional first_disclosure_date update, optional comment to splice into notes).
PMID_UPDATES = [
    ("zanetti-aminifar-atienza-eglass-2025", "41318658", "2025-11-29",
     "PMID:41318658 confirmed; published 29 November 2025; Sci Rep 2025;15(1):43574."),
    ("allen-2007-ppg-review", "17322588", None,
     "PMID:17322588 confirmed; Physiol Meas 2007;28(3):R1-39."),
    ("wolpaw-2002-bci-review", "12048038", None,
     "PMID:12048038 confirmed; Clin Neurophysiol 2002;113(6):767-91."),
    ("gao-javey-2016-wearable-sweat-sensor-array", "26819044", None,
     "PMID:26819044 confirmed; Nature 2016;529(7587):509-514."),
    ("mukkamala-2015-ptt-cuffless-bp-review", "26057530", None,
     "PMID:26057530 confirmed; IEEE Trans Biomed Eng 2015;62(8):1879-1901."),
    ("koh-rogers-2016-soft-microfluidic-sweat-device", "27881826", None,
     "PMID:27881826 confirmed; Sci Transl Med 2016;8(366):366ra165."),
    ("bandodkar-2015-tattoo-glucose-sensor", "25496376", "2014-12-12",
     "PMID:25496376 confirmed; epub 12 December 2014, print Anal Chem 2015;87(1):394-8 — first_disclosure_date refined to the epub date."),
    ("heikenfeld-2018-wearable-sensors-lab-on-chip-review", "29182185", "2018-01-16",
     "PMID:29182185 confirmed; Lab Chip 2018;18(2):217-248; first_disclosure_date refined to PubMed-reported 2018-01-16."),
    ("cole-kripke-1992-wrist-actigraphy-sleep", "1455130", None,
     "PMID:1455130 confirmed; Sleep 1992;15(5):461-9; doi 10.1093/sleep/15.5.461."),
    ("englehart-hudgins-2003-myoelectric-control", "12848352", None,
     "PMID:12848352 confirmed; IEEE Trans Biomed Eng 2003;50(7):848-54; doi 10.1109/TBME.2003.813539."),
    ("debener-2015-ceegrid-around-ear-eeg", "26572314", None,
     "PMID:26572314 confirmed; Sci Rep 2015;5:16743; doi 10.1038/srep16743."),
    ("iddan-2000-wireless-capsule-endoscopy", "10839527", None,
     "PMID:10839527 confirmed; Nature 2000;405(6785):417; doi 10.1038/35013140."),
    ("inan-2015-bcg-scg-review", "25312966", "2014-10-07",
     "PMID:25312966 confirmed; IEEE J Biomed Health Inform 2015;19(4):1414-27; epub 7 October 2014, first_disclosure_date refined."),
]


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
    for eid, pmid, new_date, comment in PMID_UPDATES:
        if eid not in by_id:
            missing.append(eid)
            continue
        e = by_id[eid]
        ip_cit_token = f"PMID:{pmid}"
        cits = list(e.get("ip_citations") or [])
        if ip_cit_token not in cits:
            cits.append(ip_cit_token)
        e["ip_citations"] = cits
        if new_date:
            e["first_disclosure_date"] = new_date
        existing_notes = (e.get("notes") or "").strip()
        appended = f"PubMed-verified ({LAST_UPDATED}): {comment}"
        e["notes"] = (existing_notes + "\n\n" + appended).strip() if existing_notes else appended
        e["last_updated"] = LAST_UPDATED
        updated.append(eid)

    with CORPUS.open("w") as f:
        for eid in seen_ids:
            f.write(json.dumps(by_id[eid], ensure_ascii=False, sort_keys=True) + "\n")

    print(f"  promote r10 (PubMed PMIDs): updated {len(updated)}; missing {len(missing)}")
    for eid in updated:
        print(f"    PMID-tagged:  {eid}")
    for eid in missing:
        print(f"    MISSING:      {eid}")


if __name__ == "__main__":
    main()
