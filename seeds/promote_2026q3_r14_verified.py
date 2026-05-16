#!/usr/bin/env python3
"""promote_2026q3_r14_verified.py — fifth FDA verification round.

  - Apple AirPods Pro 2 Hearing Aid Feature (2024)
        → FDA De Novo **DEN230081** ("Hearing Aid Feature"; decision summary
          PDF at accessdata.fda.gov/cdrh_docs/reviews/DEN230081.pdf — the
          first FDA-authorized OTC hearing-aid software).
  - Abbott FreeStyle Libre 2 (US, 2020)
        → FDA clearance date verified **15 June 2020** (then iCGM/AID
          integration cleared 6 March 2023; specific K-number still TODO).
  - Masimo W1 (2022-2024)
        → Representative FDA 510(k) **K240229** (the August 2024 connectivity
          clearance to Masimo SafetyNet); original Nov 2023 OTC/Rx clearance
          K-number still TODO. The W1 is the first FDA-cleared watch with
          continuous OTC/Rx SpO2 + PR.

Run from repo root:  python3 seeds/promote_2026q3_r14_verified.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-15"


UPDATES = {
    "apple-airpods-pro-2-hearing-health-2024": {
        "ip_citations": ["DEN230081"],
        "regulatory_pathway": "fda-de-novo",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA De Novo DEN230081 ('Hearing Aid "
            "Feature') — the first FDA-authorized OTC hearing-aid software. Decision "
            "summary PDF surfaces at "
            "accessdata.fda.gov/cdrh_docs/reviews/DEN230081.pdf. Authorized September "
            "2024; software (Hearing Test + Hearing Aid Feature + Hearing Protection) "
            "shipped with iOS 18 / iOS 18.1 in late October 2024 to AirPods Pro 2 (and "
            "later AirPods Pro 3). Companion related 510(k) K243150 also surfaces for "
            "an Apple Inc. hearing-related device; precise mapping to be enumerated."
        ),
    },
    "abbott-freestyle-libre-2-2018": {
        "regulatory_pathway": "fda-de-novo",
        "last_updated": LAST_UPDATED,
        "notes": (
            "Abbott FreeStyle Libre 2 — CE-marked October 2018 in Europe; US FDA "
            "clearance for adults and children (age 4+) granted **15 June 2020** as an "
            "iCGM with optional real-time alarms (Bluetooth, no scan required). The "
            "iOS app received separate clearance on 2 August 2021. Subsequent 6 March "
            "2023 FDA clearance permitted integration of Libre 2 and Libre 3 with "
            "automated insulin delivery (AID) systems. Specific K-numbers (Libre 2 "
            "original US, Libre 2 iOS app, Libre 2 AID-integration, Libre 3) still "
            "TODO; entry remains draft until enumerated."
        ),
    },
    "masimo-w1-2022": {
        "ip_citations": ["K240229"],
        "regulatory_pathway": "fda-510k",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory pathway and one representative identifier verified: the W1's "
            "FDA history includes (a) initial OTC/Rx 510(k) clearance announced 16 Nov "
            "2023 for continuous SpO2 + PR (specific K-number still TODO) and (b) FDA "
            "510(k) K240229 granted in August 2024 adding Bluetooth connectivity to "
            "the Masimo SafetyNet telemonitoring system "
            "(accessdata.fda.gov/cdrh_docs/pdf24/K240229.pdf). The first 2022 product "
            "announcement is the prior-art-relevant disclosure; the November 2023 "
            "OTC/Rx clearance marked the first FDA-cleared watch with continuous "
            "OTC/Rx SpO2 + PR."
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
    for eid, updates in UPDATES.items():
        if eid not in by_id:
            continue
        e = by_id[eid]
        for k, v in updates.items():
            if v is None:
                e.pop(k, None)
            else:
                e[k] = v
        updated.append(eid)
    with CORPUS.open("w") as f:
        for eid in seen_ids:
            f.write(json.dumps(by_id[eid], ensure_ascii=False, sort_keys=True) + "\n")
    print(f"  r14: updated {len(updated)}")
    for eid in updated:
        print(f"    {eid}")


if __name__ == "__main__":
    main()
