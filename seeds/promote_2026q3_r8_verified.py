#!/usr/bin/env python3
"""promote_2026q3_r8_verified.py — promote draft entries to commons-grade with verified citations.

Takes existing entries in corpus.jsonl, applies field updates (typically:
ip_citations enumerated, regulatory_pathway/identifiers verified, draft
cleared, notes amended), and rewrites the corpus. Verifications backed by
the FDA accessdata database and the USPTO/Google Patents records cited in
each update's `_verified_via` note.

Run from repo root:  python3 seeds/promote_2026q3_r8_verified.py
Idempotent — running it twice is a no-op (the updates re-apply the same
fields).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


# Each update: {id: {field: value, ...}} — fields are merged into the
# entry; setting a value of None deletes that field.
UPDATES = {
    # ---------- Polar PE2000 — Säynäjäkangas US 4,625,733 verified via Google Patents ----------
    "polar-sport-tester-pe2000-1982": {
        "ip_citations": ["US4625733A"],
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Patent enumerated: US 4,625,733 (Säynäjäkangas; 'Procedure and means for "
            "telemetric measuring of heartbeat and ECG signal, using a magnetic proximity "
            "field'; filed 18 July 1984; assignee Polar Electro Oy). The Polar story "
            "is well documented (founded 1977; first wireless HR patent 1980 (FI); Sport "
            "Tester PE2000 launched 1982; Säynäjäkangas 1942–2018)."
        ),
    },
    # ---------- Dexcom G6 — DEN170088 verified via FDA accessdata ----------
    "dexcom-g6-2018": {
        "ip_citations": ["DEN170088"],
        "regulatory_pathway": "fda-de-novo",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: De Novo DEN170088, granted 27 March 2018 — "
            "established the new device class 'integrated continuous glucose monitoring "
            "system' (iCGM) (decision summary at "
            "accessdata.fda.gov/cdrh_docs/reviews/DEN170088.pdf). The Dexcom G6 is the "
            "first device cleared under that classification."
        ),
    },
    # The corresponding regulatory entry is also promoted.
    "fda-den170088-dexcom-icgm-2018": {
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Verified via the FDA De Novo decision summary "
            "(accessdata.fda.gov/cdrh_docs/reviews/DEN170088.pdf): DEN170088 granted "
            "27 March 2018; requester Dexcom, Inc.; created the iCGM device classification."
        ),
    },
    # ---------- Eversense — PMA P160048 verified via FDA accessdata ----------
    "eversense-implantable-cgm-2018": {
        "ip_citations": ["P160048"],
        "regulatory_pathway": "fda-pma",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified: FDA PMA P160048, approved 21 June 2018 "
            "(SSED: accessdata.fda.gov/cdrh_docs/pdf16/P160048B.pdf); 'world's first "
            "long-term implantable continuous glucose monitoring system' (90-day; the "
            "Eversense E3 / 180-day variant followed via P160048/S021). Patent "
            "enumeration (Senseonics ip_citations beyond the PMA) still TODO."
        ),
    },
    # ---------- Abbott FreeStyle Libre Pro — PMA P150021 verified ----------
    # The 2014 entry covers the original (EU-launched 2014) consumer Libre; we also
    # cite the verified FDA PMA P150021 (Libre Pro, US, 2016) as the regulated
    # ancestor of the US consumer-Libre clearance pathway.
    "abbott-freestyle-libre-2014": {
        "ip_citations": ["P150021"],
        "regulatory_pathway": "fda-pma",
        "draft": None,
        "last_updated": LAST_UPDATED,
        "notes": (
            "Regulatory identifier verified for the FreeStyle Libre Pro (the "
            "professional-use US variant): FDA PMA P150021, approved 23 September 2016 "
            "(SSED: accessdata.fda.gov/cdrh_docs/pdf15/p150021b.pdf). The original 2014 "
            "consumer FreeStyle Libre was CE-marked in Europe in September 2014; the "
            "US consumer FreeStyle Libre cleared in 2017 under a separate FDA pathway "
            "(P160030, to verify) — that identifier still TODO. Abbott patent estate "
            "(beyond the PMA) also still TODO."
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

    # Rewrite preserving original order.
    with CORPUS.open("w") as f:
        for eid in seen_ids:
            e = by_id[eid]
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")

    print(f"  promote r8: updated {len(updated)} entries; {len(missing)} missing")
    for eid in updated:
        print(f"    promoted: {eid}")
    for eid in missing:
        print(f"    MISSING (no-op): {eid}")


if __name__ == "__main__":
    main()
