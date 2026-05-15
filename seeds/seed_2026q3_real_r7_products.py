#!/usr/bin/env python3
"""seed_2026q3_real_r7_products.py — more wearable products (draft tier).

Chest-strap ECG (Polar H10); textile smart shirts (Hexoskin); smart socks
with sole pressure sensors (Sensoria — opens the `sock` form factor);
hospital-grade wrist pulse oximetry (Masimo W1); multi-parameter chest
patches (VitalConnect VitalPatch, BioIntelliSense BioSticker); the second
wave of smart rings (Ultrahuman, Samsung Galaxy Ring).

All draft:true — patent and FDA-identifier enumeration TODO.

Run from repo root:  python3 seeds/seed_2026q3_real_r7_products.py
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
    kw.setdefault("corpus", "private")
    kw.setdefault("ip_status", "patented")
    kw.setdefault("draft", True)
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


WORK = ("Draft: enumerate patent numbers and (where regulated) the exact FDA 510(k)/"
        "De Novo/PMA identifiers, then promote to commons-grade.")


ENTRIES = [
    E(
        id="polar-h10-chest-strap-2017",
        canonical_name="Polar H10 (2017) — research-grade chest-strap ECG heart-rate sensor",
        aliases=["Polar H10", "Polar H10 strap"],
        first_disclosure_date="2017-01",
        disclosure_citation="Polar Electro Oy. 'Polar H10' chest heart-rate sensor, released 2017 — a chest strap with two dry electrodes deriving a single-lead ECG, computing R-R intervals and heart rate, with onboard 1-session memory, dual-broadcast (BLE + ANT+ + 5 kHz GymLink), an accelerometer (relative orientation), and well-documented R-R-interval accuracy (often used as a gold-standard reference for consumer wearables).",
        creator="Polar Electro Oy",
        creator_country="FI",
        form_factor="garment",
        form_factor_tags=["patch"],
        contact_surface="skin",
        anatomical_target=["chest", "sternum"],
        sensors=["sensor-ecg", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-hrv", "algo-arrhythmia-classification"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "r-r-interval"],
        lineage_ancestors=["polar-sport-tester-pe2000-1982"],
        notes="Draft. " + WORK + " The reference-grade modern chest strap; widely used as the comparator in PPG-HRV validation studies.",
        prior_art_notes=(
            "Discloses a chest strap with two dry electrodes deriving single-lead ECG, "
            "with on-strap R-R-interval computation, multi-protocol broadcast (BLE + "
            "ANT+ + the 5 kHz GymLink legacy band), and accelerometer-assisted noise "
            "rejection. Anticipates chest-strap-ECG claims combining 'dry textile/elastic "
            "chest electrodes', 'on-strap derivation of R-R intervals and HR', and "
            "'multi-protocol simultaneous wireless broadcast' from 2017. Product-side "
            "anchor for the garment/patch × ECG strap cross-cut; refines "
            "[[polar-sport-tester-pe2000-1982]]."
        ),
        sources=["Polar Electro Oy, H10 (product, 2017)."],
        cpc_classifications=["A61B 5/0006", "A61B 5/318", "A61B 5/02438", "H04W 4/80"],
    ),
    E(
        id="hexoskin-smart-shirt-2014",
        canonical_name="Hexoskin smart shirt (2014) — textile-integrated ECG, respiration and activity garment",
        aliases=["Hexoskin", "Hexoskin Smart Shirt", "Astroskin"],
        first_disclosure_date="2013",
        disclosure_citation="Carre Technologies Inc. (Hexoskin). 'Hexoskin Smart Shirt', introduced 2013 (consumer); a compression shirt with knitted dry textile electrodes for single-lead ECG, two-channel respiratory inductive plethysmography (thoracic + abdominal expansion), a 3-axis accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate/volume, cadence, steps, and sleep. (Used in NASA/CSA 'Astroskin' studies.)",
        creator="Carre Technologies Inc.",
        creator_country="CA",
        form_factor="garment",
        contact_surface="skin",
        anatomical_target=["chest", "torso"],
        sensors=["sensor-ecg", "sensor-respiration-impedance", "sensor-piezoelectric", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-activity-classification", "algo-sleep-staging"],
        clinical_endpoints=["electrocardiogram", "respiration", "activity"],
        lineage_ancestors=["paradiso-2005-wealthy-knitted-smart-shirt"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a consumer/research compression shirt with textile-integrated "
            "dry ECG electrodes, two-channel respiratory inductive plethysmography "
            "(thoracic + abdominal), an accelerometer, and a removable electronics pod, "
            "deriving HR, HRV, breathing rate and volume, activity, and sleep. A "
            "commercial realization of [[paradiso-2005-wealthy-knitted-smart-shirt]]; "
            "anticipates smart-shirt claims combining 'textile-integrated ECG and "
            "respiration sensors' and 'a detachable electronics module' from 2013. "
            "Product-side anchor for the garment × textile-electrode cross-cut."
        ),
        sources=["Carre Technologies Inc., Hexoskin Smart Shirt (product, 2013/2014)."],
        cpc_classifications=["A61B 5/0205", "A61B 5/259", "A41D 1/00", "A61B 5/0809"],
    ),
    E(
        id="sensoria-smart-socks-2014",
        canonical_name="Sensoria Smart Socks (2014) — pressure-sensing sock + electronic anklet for gait/running analysis",
        aliases=["Sensoria", "Sensoria smart sock", "Sensoria Fitness sock"],
        first_disclosure_date="2014-01",
        disclosure_citation="Sensoria Inc. 'Sensoria Fitness Smart Socks', announced January 2014 — running socks with three pressure-sensitive textile sensors woven into the sole (under the heel, ball of foot, and toes) and a magnetically-attached 'Sensoria Core' anklet (accelerometer + Bluetooth) that derives cadence, foot strike pattern (heel/mid/forefoot), foot landing zone, pace, distance, and provides real-time audio coaching.",
        creator="Sensoria Inc. (formerly Heapsylon)",
        creator_country="US",
        form_factor="sock",
        form_factor_tags=["legband"],
        contact_surface="skin",
        anatomical_target=["foot", "ankle"],
        sensors=["sensor-pressure-skin", "sensor-piezoelectric", "sensor-accelerometer"],
        algorithms=["algo-step-count", "algo-gait-analysis", "algo-activity-classification"],
        clinical_endpoints=["gait", "foot-pressure", "running-cadence", "running-pace"],
        notes="Draft. " + WORK + " Opens the `sock` form factor on the real-product side (previously empty).",
        prior_art_notes=(
            "Discloses a sock with multiple pressure-sensitive textile sensors woven into "
            "the sole, paired with a removable ankle-worn electronics module that derives "
            "cadence, foot-strike pattern, pressure distribution, and pace. Anticipates "
            "smart-sock/sole-pressure-sensing claims combining 'a sock with one or more "
            "textile pressure sensors at multiple positions of the foot sole' and 'a "
            "paired electronics module deriving gait metrics' from 2014. Product-side "
            "anchor for the sock form-factor cross-cut (the only `sock` entry); cf. "
            "[[nike-plus-ipod-sport-kit-2006]] (the earlier shoe/insole route)."
        ),
        sources=["Sensoria Inc., Sensoria Fitness Smart Socks (product, 2014)."],
        cpc_classifications=["A43B 17/00", "A61B 5/1038", "A61B 5/1117", "A41B 11/00"],
    ),
    E(
        id="masimo-w1-2022",
        canonical_name="Masimo W1 (2022) — first FDA-cleared continuous wrist medical-grade pulse oximetry watch",
        aliases=["Masimo W1", "Masimo Watch"],
        first_disclosure_date="2022-05",
        disclosure_citation="Masimo Corp. 'Masimo W1' health-tracking watch, announced May 2022 — a wrist-worn device performing continuous medical-grade pulse oximetry (SpO2), pulse rate, perfusion index (PI), pleth variability index (PVi), respiratory rate from the PPG, and HRV, using Masimo's SET/rainbow signal-extraction algorithms. (FDA cleared as a continuous-monitoring medical device.)",
        creator="Masimo Corp.",
        creator_country="US",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-spo2", "sensor-multi-wavelength-ppg", "sensor-accelerometer"],
        algorithms=["algo-spo2-estimation", "algo-hr", "algo-hrv", "algo-respiratory-rate"],
        clinical_endpoints=["blood-oxygen", "heart-rate", "perfusion-index", "respiratory-rate", "heart-rate-variability"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK + " Center of the Masimo–Apple SpO2 patent dispute; the W1's continuous medical-grade SpO2 is the disputed-claim domain.",
        prior_art_notes=(
            "Discloses a wrist-worn device performing continuous medical-grade pulse "
            "oximetry — SpO2, PR, perfusion index, PVi, RR-from-PPG, HRV — using "
            "established signal-extraction methods, distinguished from consumer "
            "spot-check SpO2 by continuous operation and clearance for medical use. "
            "Anticipates wrist-continuous-medical-SpO2 claims from 2022; the underlying "
            "two-wavelength SpO2 method is much older ([[aoyagi-1974-two-wavelength-"
            "pulse-oximetry]], [[mendelson-ochs-1988-reflectance-pulse-oximetry]], "
            "[[iso-80601-2-61-pulse-oximeter-equipment-2011]]). Product-side anchor for "
            "the watch × continuous-SpO2 cross-cut."
        ),
        sources=["Masimo Corp., W1 health-tracking watch (product, 2022)."],
        cpc_classifications=["A61B 5/14552", "A61B 5/02416", "A61B 5/1455", "A61B 5/746"],
    ),
    E(
        id="vitalconnect-vitalpatch-2016",
        canonical_name="VitalConnect VitalPatch (2016) — adhesive chest patch with single-lead ECG and multi-parameter monitoring",
        aliases=["VitalPatch", "VitalConnect"],
        first_disclosure_date="2016",
        disclosure_citation="VitalConnect, Inc. 'VitalPatch' biosensor, FDA-cleared as a single-use adhesive chest patch with single-lead ECG, heart rate, heart-rate variability, respiratory rate, skin temperature, posture, activity, and fall detection, streamed wirelessly to a smartphone/relay; 7-day wear (later 14-day variants).",
        creator="VitalConnect, Inc.",
        creator_country="US",
        form_factor="patch",
        contact_surface="skin",
        anatomical_target=["chest"],
        sensors=["sensor-ecg", "sensor-accelerometer", "sensor-skin-temperature"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-activity-classification", "algo-posture-detection", "algo-fall-detection", "algo-arrhythmia-classification"],
        clinical_endpoints=["electrocardiogram", "heart-rate-variability", "respiratory-rate", "skin-temperature", "posture", "fall-event"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a single-use adhesive chest patch deriving single-lead ECG, HR, "
            "HRV, respiratory rate, skin temperature, posture, activity, and falls in "
            "one body-worn unit, streamed wirelessly — i.e. a packed multi-parameter "
            "vital-signs patch. Anticipates multi-parameter ECG-patch claims combining "
            "any subset of those measurements in one adhesive form factor from 2016. "
            "Product-side anchor for the patch × multi-parameter-vitals cross-cut "
            "alongside [[fda-k113862-irhythm-zio-patch-2011]] (the AFib-focused variant)."
        ),
        sources=["VitalConnect, Inc., VitalPatch biosensor (product, 2016)."],
        cpc_classifications=["A61B 5/333", "A61B 5/318", "A61B 5/0205", "A61B 5/1117"],
    ),
    E(
        id="biointellisense-biosticker-2019",
        canonical_name="BioIntelliSense BioSticker (2019) — long-wear adhesive chest patch with extensive multi-parameter monitoring",
        aliases=["BioSticker", "BioIntelliSense BioSticker"],
        first_disclosure_date="2019-12",
        disclosure_citation="BioIntelliSense, Inc. 'BioSticker' single-use adhesive medical-grade biosensor, FDA-cleared 2019 — a chest patch with up to 30-day wear continuously measuring skin temperature, single-lead ECG-derived heart rate at rest, respiratory rate at rest, body position, activity (steps, cadence, gait), sleep, cough, vomiting events, and falls, with wireless upload.",
        creator="BioIntelliSense, Inc.",
        creator_country="US",
        form_factor="patch",
        contact_surface="skin",
        anatomical_target=["chest"],
        sensors=["sensor-ecg", "sensor-accelerometer", "sensor-skin-temperature", "sensor-microphone-air"],
        algorithms=["algo-hr", "algo-respiratory-rate", "algo-activity-classification", "algo-posture-detection", "algo-fall-detection", "algo-cough-detection", "algo-gait-analysis", "algo-sleep-staging"],
        clinical_endpoints=["skin-temperature", "heart-rate", "respiratory-rate", "posture", "activity", "fall-event", "cough", "sleep"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a single-use 30-day adhesive chest patch combining skin "
            "temperature, resting HR-from-ECG, resting RR, posture/activity, sleep, "
            "cough and vomiting event detection, and falls — i.e. an unusually broad "
            "multi-parameter long-wear patch with explicit event-detection (cough, "
            "vomit) classifiers. Anticipates long-wear multi-parameter patch claims "
            "from 2019, including the event-detection (cough/vomit) elements that some "
            "later patents recite. Product-side anchor for the patch × long-wear "
            "multi-parameter cross-cut."
        ),
        sources=["BioIntelliSense, Inc., BioSticker (product, 2019)."],
        cpc_classifications=["A61B 5/333", "A61B 5/01", "A61B 5/1117", "A61B 7/003"],
    ),
    E(
        id="samsung-galaxy-ring-2024",
        canonical_name="Samsung Galaxy Ring (2024) — smart ring with PPG, skin temperature and accelerometer for HR/HRV, sleep and cycle tracking",
        aliases=["Galaxy Ring", "Samsung Ring"],
        first_disclosure_date="2024-07-10",
        disclosure_citation="Samsung Electronics. 'Samsung Galaxy Ring', announced July 2024 — a finger ring with infrared photoplethysmography, an IR skin-temperature sensor, and a 3-axis accelerometer, deriving heart rate, heart-rate variability, skin temperature, sleep staging, activity, snore detection, and (with cycle-tracking) menstrual-cycle predictions.",
        creator="Samsung Electronics Co., Ltd.",
        creator_country="KR",
        form_factor="ring",
        contact_surface="skin",
        anatomical_target=["finger"],
        sensors=["sensor-ppg", "sensor-skin-temperature", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-sleep-staging", "algo-snore-detection", "algo-step-count"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "skin-temperature", "sleep", "menstrual-cycle"],
        lineage_ancestors=["oura-ring-gen1-2015"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a smart ring with infrared PPG, IR skin-temperature, and "
            "accelerometer, deriving HR/HRV, sleep, snore detection, activity, and "
            "menstrual-cycle prediction — a Samsung entry directly in the wake of "
            "[[oura-ring-gen1-2015]] and the [[asada-mit-wearable-ring-sensor-2003]] "
            "academic root. Product-side reference in the ring × PPG × HRV cross-cut "
            "alongside Oura."
        ),
        sources=["Samsung Electronics, Galaxy Ring (product, 2024)."],
        cpc_classifications=["A61B 5/02427", "A61B 5/01", "A61B 5/4812", "A61B 5/681"],
    ),
    E(
        id="ultrahuman-ring-air-2023",
        canonical_name="Ultrahuman Ring AIR (2023) — smart ring with metabolic-focus tracking (PPG, skin temperature, IMU)",
        aliases=["Ultrahuman Ring", "Ultrahuman Ring AIR"],
        first_disclosure_date="2023",
        disclosure_citation="Ultrahuman Healthcare Pvt. Ltd. 'Ultrahuman Ring AIR', launched 2023 — a titanium smart ring with infrared photoplethysmography, IR skin-temperature, and a 6-axis IMU, deriving HR, HRV, skin temperature, sleep staging, activity, and metabolic-health framing (paired with the company's CGM-based metabolism platform).",
        creator="Ultrahuman Healthcare Pvt. Ltd.",
        creator_country="IN",
        form_factor="ring",
        contact_surface="skin",
        anatomical_target=["finger"],
        sensors=["sensor-ppg", "sensor-skin-temperature", "sensor-accelerometer", "sensor-gyroscope"],
        algorithms=["algo-hr", "algo-hrv", "algo-sleep-staging", "algo-respiratory-rate"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "skin-temperature", "sleep"],
        lineage_ancestors=["oura-ring-gen1-2015"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a smart ring with IR PPG, skin-temperature, and a 6-axis IMU, "
            "deriving HR/HRV, sleep, and activity, packaged with a metabolic-health "
            "platform (CGM-linked). Product-side reference in the ring × PPG cross-cut "
            "alongside [[oura-ring-gen1-2015]] and [[samsung-galaxy-ring-2024]]."
        ),
        sources=["Ultrahuman Healthcare, Ring AIR (product, 2023)."],
        cpc_classifications=["A61B 5/02427", "A61B 5/01", "A61B 5/4812", "A61B 5/681"],
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
    print(f"  real products r7: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
