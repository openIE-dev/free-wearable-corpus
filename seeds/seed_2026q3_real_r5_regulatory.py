#!/usr/bin/env python3
"""seed_2026q3_real_r5_regulatory.py — landmark FDA decisions (regulatory bucket).

The first entries in the `regulatory` bucket: the De Novo classifications
and key 510(k)s that created (or anchor) whole categories of consumer
wearable medical devices. A De Novo decision summary or a 510(k) record is
a public, dated, third-party-attested government disclosure of the device
it describes, and (for 510(k)s) of the predicate-device chain it cites.

Verified against FDA records where noted; flagged draft where the
identifier still needs confirmation against the FDA database.

Run from repo root:  python3 seeds/seed_2026q3_real_r5_regulatory.py
Idempotent — skips ids already present.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("corpus", "regulatory")
    kw.setdefault("ip_status", "regulatory-filing")
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    E(
        id="fda-den180044-apple-watch-ecg-app-2018",
        canonical_name="FDA De Novo DEN180044 (2018) — over-the-counter electrocardiograph software for use in detecting atrial fibrillation (Apple Watch ECG app)",
        aliases=["DEN180044", "Apple Watch ECG app De Novo", "OTC ECG software classification"],
        first_disclosure_date="2018-09-11",
        disclosure_citation="U.S. FDA, De Novo Classification Request DEN180044 (Apple Inc., 'ECG App'), granted 11 September 2018 — decision summary at accessdata.fda.gov/cdrh_docs/reviews/DEN180044.pdf; established a new FDA device classification for over-the-counter electrocardiograph software intended to acquire, store, transfer and display a single-lead (Lead I) ECG and to provide a rhythm classification (AFib vs. sinus rhythm) on a consumer wrist-worn platform, with general/special controls.",
        creator="U.S. Food and Drug Administration (CDRH); requester Apple Inc.",
        creator_country="US",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist", "fingertip"],
        sensors=["sensor-ecg"],
        algorithms=["algo-afib-detection", "algo-arrhythmia-classification"],
        clinical_endpoints=["electrocardiogram", "atrial-fibrillation"],
        regulatory_pathway="fda-de-novo",
        ip_citations=["DEN180044"],
        notes="Verified: DEN180044 confirmed via the FDA De Novo decision-summary record (accessdata.fda.gov/cdrh_docs/reviews/DEN180044.pdf). Software-feature device; the host hardware is the Apple Watch Series 4 ([[apple-watch-series4-ecg-2018]]).",
        prior_art_notes=(
            "A public, dated FDA decision describing — and creating the device class for — "
            "over-the-counter single-lead ECG software on a consumer wrist-worn device "
            "with on-device AFib-vs-sinus classification. As a government disclosure it "
            "establishes, as of 11 September 2018, the public availability of the device "
            "described: a wristworn Lead-I ECG with consumer-facing rhythm classification. "
            "Useful prior art for later claims to that combination; the De Novo decision "
            "summary also enumerates the clinical validation and the bench/algorithm "
            "characteristics, which are themselves citable. Pairs with the product entry "
            "[[apple-watch-series4-ecg-2018]] and the standard "
            "[[ieee-11073-10406-basic-ecg-2011]]."
        ),
        sources=["U.S. FDA, DEN180044 decision summary, 2018."],
        cpc_classifications=["A61B 5/318", "A61B 5/352", "A61B 5/333", "G16H 50/20"],
    ),
    E(
        id="fda-den180042-irregular-rhythm-notification-2018",
        canonical_name="FDA De Novo DEN180042 (2018) — photoplethysmograph analysis software for over-the-counter irregular-rhythm (possible-AFib) notification (Apple Watch)",
        aliases=["DEN180042", "Irregular Rhythm Notification Feature De Novo", "OTC PPG-AF screening software classification"],
        first_disclosure_date="2018-09-11",
        disclosure_citation="U.S. FDA, De Novo Classification Request DEN180042 (Apple Inc., 'Irregular Rhythm Notification Feature'), granted 11 September 2018 — decision summary at accessdata.fda.gov/cdrh_docs/reviews/DEN180042.pdf; established a new FDA device classification for software that analyses pulse-rate data from a consumer wrist-worn photoplethysmography sensor, intermittently and in the background, to identify episodes of irregular heart rhythm suggestive of atrial fibrillation and notify the user, with general/special controls.",
        creator="U.S. Food and Drug Administration (CDRH); requester Apple Inc.",
        creator_country="US",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg"],
        algorithms=["algo-afib-detection", "algo-hr"],
        clinical_endpoints=["irregular-rhythm", "atrial-fibrillation"],
        regulatory_pathway="fda-de-novo",
        ip_citations=["DEN180042"],
        notes="Verified: DEN180042 confirmed via the FDA De Novo decision-summary record (accessdata.fda.gov/cdrh_docs/reviews/DEN180042.pdf). Software-feature device on the Apple Watch wrist-PPG platform; validated in the Apple Heart Study (~419k participants).",
        prior_art_notes=(
            "A public, dated FDA decision describing — and creating the device class for — "
            "background PPG-based screening for irregular heart rhythm / possible atrial "
            "fibrillation on a consumer wrist wearable, with user notification. Establishes "
            "as of 11 September 2018 the public availability of: a wrist-PPG device that "
            "intermittently analyses pulse-rate variability to flag possible AFib and "
            "notifies the wearer. Prior art for later claims to that combination; the "
            "decision summary's account of the algorithm and the Apple Heart Study "
            "validation is citable. Pairs with [[apple-watch-series4-ecg-2018]], "
            "[[allen-2007-ppg-review]], and the fictional AR-overlay antecedents are "
            "irrelevant here — this is enabling prior art."
        ),
        sources=["U.S. FDA, DEN180042 decision summary, 2018."],
        cpc_classifications=["A61B 5/02405", "A61B 5/352", "A61B 5/02416", "G16H 50/20"],
    ),
    E(
        id="fda-k113862-irhythm-zio-patch-2011",
        canonical_name="FDA 510(k) K113862 (~2011) — iRhythm Zio Patch, long-term single-lead adhesive ECG monitor",
        aliases=["K113862", "Zio Patch 510(k)", "Zio XT clearance"],
        first_disclosure_date="2011-12",
        disclosure_citation="U.S. FDA, 510(k) Premarket Notification K113862 (iRhythm Technologies, Inc., 'Zio Patch') — record at accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K113862; a single-use adhesive chest patch recording a single channel of ECG continuously for up to ~14 days for later analysis, cleared as substantially equivalent to predicate ambulatory-ECG (Holter-class) devices. (Followed by a chain of subsequent iRhythm 510(k)s — e.g. K143513, K163512, K181502 — refining the device, the algorithm/ZEUS software, and the Zio AT mobile-cardiac-telemetry variant.)",
        creator="U.S. Food and Drug Administration (CDRH); submitter iRhythm Technologies, Inc.",
        creator_country="US",
        form_factor="patch",
        contact_surface="skin",
        anatomical_target=["chest"],
        sensors=["sensor-ecg"],
        algorithms=["algo-arrhythmia-classification", "algo-afib-detection"],
        clinical_endpoints=["electrocardiogram", "arrhythmia"],
        regulatory_pathway="fda-510k",
        ip_citations=["K113862"],
        lineage_ancestors=["holter-1961-ambulatory-ecg"],
        notes="K113862 confirmed via the FDA 510(k) database listing (pmn.cfm?ID=K113862); exact clearance date (within 2011/early 2012) and the full predicate chain to be transcribed from the FDA record when enumerating it.",
        prior_art_notes=(
            "A public, dated FDA record of a single-use adhesive chest patch that records "
            "one channel of ECG continuously for up to ~14 days for later arrhythmia "
            "analysis — the modern 'ECG patch' realization of ambulatory ECG "
            "([[holter-1961-ambulatory-ecg]]). Establishes as of ~2011 the public "
            "availability of an adhesive long-wear single-lead ECG patch with downstream "
            "automated arrhythmia analysis; and, as a 510(k), it cites a predicate chain "
            "back to earlier ambulatory-ECG devices — that chain is itself prior art. "
            "Prior art for ECG-patch claims; product-side and regulatory anchor for the "
            "patch × ECG cross-cut. Cf. [[apple-watch-series4-ecg-2018]] (the wrist "
            "single-lead route)."
        ),
        sources=["U.S. FDA, 510(k) K113862 record, 2011."],
        cpc_classifications=["A61B 5/333", "A61B 5/282", "A61B 5/0006", "A61B 5/259"],
    ),
    E(
        id="fda-den170088-dexcom-icgm-2018",
        canonical_name="FDA De Novo (2018) — 'integrated continuous glucose monitoring system' (iCGM) classification (Dexcom G6)",
        aliases=["iCGM De Novo", "DEN170088", "integrated CGM classification", "Dexcom G6 iCGM"],
        first_disclosure_date="2018-03-27",
        disclosure_citation="U.S. FDA, De Novo classification (Dexcom, Inc., 'Dexcom G6 Continuous Glucose Monitoring System'), granted March 2018 — established the new device class 'integrated continuous glucose monitoring system' (iCGM): a CGM intended to reliably and securely transmit glucose data to digitally-connected devices (e.g. automated insulin-dosing systems), with stringent accuracy special controls; reportedly DEN170088 (verify against the FDA De Novo database).",
        creator="U.S. Food and Drug Administration (CDRH); requester Dexcom, Inc.",
        creator_country="US",
        form_factor="patch",
        form_factor_tags=["implantable"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "abdomen", "upper-arm"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-de-novo",
        draft=True,
        notes="Draft: the De Novo identifier (DEN170088) and the exact granted date are reported from memory and a partial search — verify against the FDA De Novo database, then promote. The substance (the iCGM classification, created via the Dexcom G6 De Novo in 2018) is well established.",
        prior_art_notes=(
            "A public, dated FDA decision creating the 'integrated CGM' device class — a "
            "continuous glucose monitor designed to interoperate (transmit glucose data) "
            "with other devices such as automated insulin pumps, under defined accuracy "
            "and security special controls. Establishes as of 2018 the public availability "
            "of an interoperable, factory-calibrated real-time CGM intended as a component "
            "of a connected diabetes-management system. Prior art for CGM-interoperability "
            "and connected-CGM claims; regulatory anchor pairing with "
            "[[dexcom-g6-2018]] and [[shichiri-1982-wearable-needle-glucose-sensor]]."
        ),
        sources=["U.S. FDA, Dexcom G6 De Novo decision (iCGM classification), 2018."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61M 5/172", "G16H 20/17"],
    ),
    E(
        id="fda-k181861-empatica-embrace-seizure-system-2018",
        canonical_name="FDA 510(k) K181861 (2018) — Empatica Embrace physiological-signal-based seizure monitoring system",
        aliases=["K181861", "Embrace 510(k)", "Empatica seizure system clearance"],
        first_disclosure_date="2018",
        disclosure_citation="U.S. FDA, 510(k) Premarket Notification K181861 (Empatica Inc., 'Embrace' physiological-signal-based seizure monitoring system) — a wrist-worn device using accelerometry plus electrodermal activity to detect probable generalized tonic-clonic seizures and alert caregivers; reported as the first FDA-cleared smartwatch indicated for use in neurology (clearance announced February 2018). (Verify which Embrace generation K181861 maps to; the original clearance may carry a different K-number.)",
        creator="U.S. Food and Drug Administration (CDRH); submitter Empatica Inc.",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-accelerometer", "sensor-gsr"],
        algorithms=["algo-seizure-detection"],
        clinical_endpoints=["seizure-event", "electrodermal-activity"],
        regulatory_pathway="fda-510k",
        draft=True,
        ip_citations=["K181861"],
        notes="Draft: K181861 found via a partial search of FDA-related documents and tied to the Embrace seizure-monitoring system; the exact mapping to the Embrace vs. Embrace2 generation and the clearance date need confirmation against the FDA 510(k) database, then promote.",
        prior_art_notes=(
            "A public, dated FDA record of a wrist-worn device detecting probable "
            "generalized tonic-clonic seizures from combined accelerometry and "
            "electrodermal activity, with caregiver alerting — the non-EEG route to "
            "wearable seizure detection. Establishes the public availability of that "
            "device as of 2018; the 510(k) cites a predicate chain that is itself prior "
            "art. Prior art for wrist-based seizure-detection claims using motion + EDA; "
            "regulatory anchor pairing with [[empatica-embrace2-seizure-watch-2018]] (the "
            "EEG route is anchored separately by "
            "[[zanetti-aminifar-atienza-eglass-2025]] and "
            "[[chb-mit-scalp-eeg-database-2009]])."
        ),
        sources=["U.S. FDA, 510(k) K181861 record (Empatica Embrace seizure monitoring system), 2018."],
        cpc_classifications=["A61B 5/4094", "A61B 5/0531", "A61B 5/1117", "G16H 50/20"],
    ),
]


def main():
    existing = set()
    if CORPUS.exists() and CORPUS.stat().st_size:
        for line in CORPUS.read_text().splitlines():
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])
    added = skipped = 0
    with CORPUS.open("a") as f:
        for e in ENTRIES:
            if e["id"] in existing:
                skipped += 1
                continue
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
            added += 1
    print(f"  real regulatory r5: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
