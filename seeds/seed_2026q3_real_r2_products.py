#!/usr/bin/env python3
"""seed_2026q3_real_r2_products.py — iconic commercial wearable products (draft tier).

These are real products whose launch dates are well documented and which
are clearly patent-protected, but whose specific patent numbers (and, for
the regulated ones, exact 510(k)/De Novo/PMA identifiers) still need
enumeration. They are merged as draft:true per the corpus quality bar:
the slug is reserved, the prior-art-relevant date (the product launch /
regulatory clearance) is captured, and the follow-up work is documented
in each entry's notes.

Run from repo root:  python3 seeds/seed_2026q3_real_r2_products.py
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


WORK = ("Draft: enumerate patent numbers (search assignee in USPTO/Google Patents) "
        "and, where applicable, the exact FDA 510(k)/De Novo/PMA identifiers; then "
        "promote to commons-grade.")


ENTRIES = [
    E(
        id="polar-sport-tester-pe2000-1982",
        canonical_name="Polar Sport Tester PE2000 — first wireless wrist heart-rate monitor",
        aliases=["Polar PE2000", "Polar Sport Tester"],
        first_disclosure_date="1982",
        disclosure_citation="Polar Electro Oy. 'Sport Tester PE2000' wrist heart-rate monitor, introduced 1982 — a chest electrode strap transmitting ECG-derived heart rate wirelessly to a wrist-worn receiver/display. Underlying invention: Seppo Säynäjäkangas, wireless heart-rate measurement, patents filed from c. 1977 (Polar Electro).",
        creator="Polar Electro Oy (Seppo Säynäjäkangas)",
        creator_country="FI",
        form_factor="watch",
        form_factor_tags=["garment", "armband"],
        contact_surface="skin",
        anatomical_target=["chest", "wrist"],
        sensors=["sensor-ecg"],
        algorithms=["algo-hr"],
        clinical_endpoints=["heart-rate"],
        notes="Draft. " + WORK + " First commercial wristworn HR monitor; the wrist unit is a receiver/display, the sensing is a chest ECG strap.",
        prior_art_notes=(
            "Discloses a body-worn heart-rate monitoring system: a chest strap with "
            "electrodes deriving heart rate from the ECG and transmitting it wirelessly to "
            "a wrist-worn receiver that displays it. Anticipates claims combining 'a "
            "chest-worn electrode assembly sensing heart rate' and 'wireless transmission "
            "to a wrist-worn display' (the chest-strap-plus-watch architecture), and the "
            "bare 'wristworn heart-rate display' concept, from 1982 (invention c. 1977). "
            "Anchor for the wristworn-HR cross-cut on the product side; "
            "[[bluetooth-sig-heart-rate-profile-2011]] later standardized the comms link."
        ),
        sources=["Polar Electro Oy, Sport Tester PE2000 (product, 1982)."],
        cpc_classifications=["A61B 5/0006", "A61B 5/333", "A61B 5/02438", "G04G 21/04"],
    ),
    E(
        id="fitbit-tracker-2009",
        canonical_name="Fitbit Tracker (2009) — clip-on accelerometer activity and sleep monitor",
        aliases=["Fitbit", "Fitbit Tracker", "first Fitbit"],
        first_disclosure_date="2009-10",
        disclosure_citation="Fitbit, Inc. 'Fitbit Tracker', launched October 2009 — a clip-worn device with a 3-axis accelerometer estimating steps, distance, calories burned, active minutes, and sleep quality, syncing wirelessly to a web dashboard. (The wrist PPG heart-rate variant, Fitbit Charge HR, followed in January 2015.)",
        creator="Fitbit, Inc. (James Park, Eric Friedman)",
        creator_country="US",
        form_factor="pendant",
        form_factor_tags=["bracelet", "watch"],
        contact_surface="skin",
        anatomical_target=["waistband", "wrist"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-step-count", "algo-calorie-estimation", "algo-activity-classification", "algo-sleep-staging"],
        clinical_endpoints=["activity", "sleep"],
        notes="Draft. " + WORK + " The 2009 product is a clip; the wrist + PPG variants came 2013-2015 (note them when promoting).",
        prior_art_notes=(
            "Discloses a small body-worn (clip) device with a 3-axis accelerometer that "
            "estimates step count, distance, calories, active minutes, and sleep quality "
            "on-device and syncs wirelessly to a cloud dashboard. Anticipates "
            "consumer-activity-tracker claims combining 'a body-worn accelerometer', "
            "'on-device estimation of steps/calories/activity/sleep', and 'wireless sync "
            "to a remote service' from 2009. Anchor for the step-count and consumer-"
            "sleep-tracking cross-cuts on the product side."
        ),
        sources=["Fitbit, Inc., Fitbit Tracker (product, 2009)."],
        cpc_classifications=["A61B 5/1118", "A61B 5/4866", "G06F 1/163", "A61B 5/0024"],
    ),
    E(
        id="nike-plus-ipod-sport-kit-2006",
        canonical_name="Nike+iPod Sport Kit (2006) — instrumented-shoe accelerometer pod",
        aliases=["Nike+", "Nike Plus", "Nike+iPod"],
        first_disclosure_date="2006-05-23",
        disclosure_citation="Nike, Inc. and Apple Inc. 'Nike+iPod Sport Kit', announced 23 May 2006 — an accelerometer pod that sits in a cavity in a Nike+ running shoe and transmits pace, distance, and calories wirelessly to an iPod nano.",
        creator="Nike, Inc. / Apple Inc.",
        creator_country="US",
        form_factor="shoe",
        form_factor_tags=["insole"],
        contact_surface="textile-mediated",
        anatomical_target=["foot"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-step-count", "algo-activity-classification", "algo-calorie-estimation"],
        clinical_endpoints=["activity", "running-pace"],
        notes="Draft. " + WORK + " Opens the shoe/insole form factor on the real-product side (fiction had only Mercury's sandals, seven-league boots, ruby slippers, BTTF power-laces, Portal long-fall boots).",
        prior_art_notes=(
            "Discloses an accelerometer module integrated into the structure of a running "
            "shoe that derives pace, distance, and calories and transmits them wirelessly "
            "to a paired device. Anticipates instrumented-footwear claims combining 'an "
            "inertial sensor housed in a shoe', 'derivation of gait/running metrics', and "
            "'wireless transmission to a companion device' from 2006. Anchor for the "
            "shoe/insole × accelerometer cross-cut on the product side; predates the "
            "smart-insole patent wave."
        ),
        sources=["Nike, Inc. / Apple Inc., Nike+iPod Sport Kit (product, 2006)."],
        cpc_classifications=["A43B 3/34", "A61B 5/1038", "A61B 5/1118", "A43B 3/00"],
    ),
    E(
        id="apple-watch-original-2015",
        canonical_name="Apple Watch (1st generation, 2015) — wrist green-PPG heart rate and activity",
        aliases=["Apple Watch", "Apple Watch Series 0"],
        first_disclosure_date="2015-04-24",
        disclosure_citation="Apple Inc. 'Apple Watch', announced September 2014, available 24 April 2015 — a wrist-worn device with a green/infrared photoplethysmography heart-rate sensor against the dorsal wrist, accelerometer and gyroscope, and activity/exercise tracking.",
        creator="Apple Inc.",
        creator_country="US",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-multi-wavelength-ppg", "sensor-accelerometer", "sensor-gyroscope"],
        algorithms=["algo-hr", "algo-step-count", "algo-calorie-estimation", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "activity"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a wristworn device with a dorsal-wrist green-LED photoplethysmography "
            "heart-rate sensor (with IR for low-perfusion conditions), inertial sensors, "
            "and continuous HR/activity tracking. Anticipates wristworn-PPG-HR claims to "
            "the extent they postdate April 2015; combined with the much earlier PPG "
            "principle ([[hertzman-1937-photoplethysmography]]) and wrist form factor, the "
            "combination is in any case obvious under [[obviousness-template]]. Product-"
            "side anchor for the watch × PPG cross-cut."
        ),
        sources=["Apple Inc., Apple Watch (product, 2015)."],
        cpc_classifications=["A61B 5/02416", "A61B 5/681", "A61B 5/1118", "G04G 21/04"],
    ),
    E(
        id="apple-watch-series4-ecg-2018",
        canonical_name="Apple Watch Series 4 (2018) — wrist single-lead ECG and PPG-based irregular-rhythm notification",
        aliases=["Apple Watch ECG", "Apple Watch Series 4", "ECG app"],
        first_disclosure_date="2018-09-12",
        disclosure_citation="Apple Inc. 'Apple Watch Series 4', announced 12 September 2018 (ECG app and irregular rhythm notification feature enabled later in 2018) — a wristworn device taking a single-lead (Lead I) ECG between a back-crystal electrode and a Digital Crown electrode touched by the opposite hand, with on-device AF/sinus classification, plus a PPG-based irregular-rhythm (possible-AF) notification algorithm. FDA cleared via De Novo (ECG app: DEN180044; irregular rhythm notification: DEN180042).",
        creator="Apple Inc.",
        creator_country="US",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist", "fingertip"],
        sensors=["sensor-ecg", "sensor-ppg"],
        algorithms=["algo-afib-detection", "algo-arrhythmia-classification", "algo-hr"],
        clinical_endpoints=["electrocardiogram", "atrial-fibrillation", "heart-rate"],
        regulatory_pathway="fda-de-novo",
        ip_status="patented",
        notes="Draft. " + WORK + " De Novo identifiers DEN180044 (ECG app) and DEN180042 (irregular rhythm notification) cited from memory — verify against the FDA De Novo database before promoting.",
        prior_art_notes=(
            "Discloses a wristworn device that records a single-lead ECG between a "
            "watch-back electrode and a crown electrode touched by the contralateral "
            "hand, classifies the rhythm (AF vs. sinus) on-device, and separately runs a "
            "PPG-based background algorithm flagging possible atrial fibrillation. "
            "Anticipates wristworn-ECG and watch-AF-detection claims postdating September "
            "2018; the underlying single-lead ECG and PPG-rhythm-screening techniques are "
            "much older ([[einthoven-1903-string-galvanometer-ecg]], "
            "[[holter-1961-ambulatory-ecg]], [[allen-2007-ppg-review]], "
            "[[ieee-11073-10406-basic-ecg-2011]]). Product-side anchor for the watch × ECG "
            "and watch × PPG × AF-detection cross-cuts."
        ),
        sources=["Apple Inc., Apple Watch Series 4 (product, 2018); FDA De Novo DEN180044, DEN180042."],
        cpc_classifications=["A61B 5/318", "A61B 5/333", "A61B 5/352", "A61B 5/02416"],
    ),
    E(
        id="alivecor-kardiamobile-2012",
        canonical_name="AliveCor Heart Monitor / KardiaMobile (2012) — smartphone-coupled single-lead ECG",
        aliases=["AliveCor", "KardiaMobile", "AliveCor Heart Monitor", "Kardia Band"],
        first_disclosure_date="2012-12",
        disclosure_citation="AliveCor, Inc. 'AliveCor Heart Monitor' (later 'KardiaMobile'), FDA-cleared December 2012 — a card-sized two-electrode module that records a single-lead ECG via dry electrodes touched by the fingers (or pressed to the chest) and streams it to a smartphone app for AF detection. (The 'Kardia Band' wrist-strap ECG accessory for Apple Watch followed in 2017, FDA cleared.)",
        creator="AliveCor, Inc. (David Albert)",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["watch"],
        contact_surface="skin",
        anatomical_target=["fingertip", "chest", "wrist"],
        sensors=["sensor-ecg"],
        algorithms=["algo-afib-detection", "algo-arrhythmia-classification", "algo-hr"],
        clinical_endpoints=["electrocardiogram", "atrial-fibrillation"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK + " Exact 510(k) numbers (KardiaMobile c. K122356, 2012; Kardia Band c. K171816, 2017) cited from memory — verify against the FDA 510(k) database. Form factor 'other' for the card module; the Kardia Band variant is 'watch'.",
        prior_art_notes=(
            "Discloses a portable two-dry-electrode single-lead ECG recorder that the user "
            "contacts with the fingers (or chest) and that streams the trace to a "
            "smartphone for automated atrial-fibrillation detection — and, in the 2017 "
            "Kardia Band variant, the same dry-electrode single-lead ECG integrated into a "
            "wrist strap. Anticipates consumer single-lead-ECG and wrist-strap-ECG "
            "AF-detection claims from 2012/2017 — predating the Apple Watch Series 4 "
            "ECG (2018). Product-side anchor for the consumer-ECG cross-cut."
        ),
        sources=["AliveCor, Inc., AliveCor Heart Monitor / KardiaMobile (product, 2012); Kardia Band (product, 2017)."],
        cpc_classifications=["A61B 5/318", "A61B 5/333", "A61B 5/282", "A61B 5/352"],
    ),
    E(
        id="whoop-strap-2015",
        canonical_name="WHOOP Strap (2015) — display-less wrist/bicep PPG band for continuous HR/HRV, sleep and recovery",
        aliases=["WHOOP", "WHOOP Strap 2.0"],
        first_disclosure_date="2015",
        disclosure_citation="WHOOP, Inc. 'WHOOP Strap', launched 2015 — a screenless band worn on the wrist or upper arm with photoplethysmography, a 3-axis accelerometer, and skin-temperature sensing, providing continuous heart rate, heart-rate variability, respiratory rate, sleep staging, and a derived 'recovery' score, with no on-device display.",
        creator="WHOOP, Inc. (Will Ahmed)",
        creator_country="US",
        form_factor="bracelet",
        form_factor_tags=["armband"],
        contact_surface="skin",
        anatomical_target=["wrist", "upper-arm"],
        sensors=["sensor-ppg", "sensor-accelerometer", "sensor-skin-temperature"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-sleep-staging", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "respiratory-rate", "sleep", "skin-temperature"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a display-less band worn on the wrist or upper arm with PPG, "
            "accelerometry, and skin-temperature sensing that continuously derives HR, "
            "HRV, respiratory rate, and sleep stages and combines them into a daily "
            "'recovery' index, with no screen (companion-app readout). Anticipates "
            "screenless-band claims and PPG-derived-HRV/recovery-score claims from 2015. "
            "Product-side anchor for the bracelet × PPG cross-cut and the HRV cross-cut."
        ),
        sources=["WHOOP, Inc., WHOOP Strap (product, 2015)."],
        cpc_classifications=["A61B 5/02438", "A61B 5/02405", "A61B 5/4812", "A61B 5/681"],
    ),
    E(
        id="oura-ring-gen1-2015",
        canonical_name="Oura Ring (Gen 1, 2015) — finger-ring PPG, skin-temperature and accelerometer for HRV, sleep and body temperature",
        aliases=["Oura Ring", "Oura"],
        first_disclosure_date="2015-08",
        disclosure_citation="Oura Health Oy. 'Oura Ring' (1st generation), crowdfunded 2015, shipped 2016 — a titanium finger ring with infrared photoplethysmography, an NTC skin-temperature sensor, and a 3-axis accelerometer, deriving resting heart rate, heart-rate variability, respiratory rate, sleep staging, and body-temperature trend.",
        creator="Oura Health Oy",
        creator_country="FI",
        form_factor="ring",
        contact_surface="skin",
        anatomical_target=["finger"],
        sensors=["sensor-ppg", "sensor-skin-temperature", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-sleep-staging"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "respiratory-rate", "sleep", "skin-temperature"],
        lineage_ancestors=["asada-mit-wearable-ring-sensor-2003"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a finger-ring wearable with infrared PPG, a skin-temperature "
            "sensor, and an accelerometer, deriving resting HR, HRV, respiratory rate, "
            "sleep stages, and a body-temperature trend, with companion-app readout. A "
            "commercial realization, ~12-16 years later, of the MIT ring-sensor concept "
            "([[asada-mit-wearable-ring-sensor-2003]]); to the extent later claims recite "
            "ring-form PPG + skin-temperature + HRV/sleep, both Asada 2003 and Oura 2015 "
            "are prior art. Product-side anchor for the ring × PPG × HRV and ring × "
            "skin-temperature cross-cuts."
        ),
        sources=["Oura Health Oy, Oura Ring Gen 1 (product, 2015/2016)."],
        cpc_classifications=["A61B 5/02427", "A61B 5/01", "A61B 5/4812", "A61B 5/681"],
    ),
    E(
        id="neurosky-mindset-2007",
        canonical_name="NeuroSky MindSet / MindWave (2007) — single dry-electrode consumer EEG headset",
        aliases=["NeuroSky", "MindSet", "MindWave", "ThinkGear"],
        first_disclosure_date="2007",
        disclosure_citation="NeuroSky, Inc. 'MindSet' (and later 'MindWave') consumer EEG headset, with the 'ThinkGear' single dry forehead (Fp1) electrode and ear-clip reference, output as 'eSense' attention and meditation metrics plus raw EEG, first shown 2007.",
        creator="NeuroSky, Inc.",
        creator_country="US",
        form_factor="headband",
        contact_surface="skin",
        anatomical_target=["forehead", "Fp1", "ear"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-attention-state", "algo-cognitive-workload"],
        clinical_endpoints=["electroencephalogram", "attention", "relaxation"],
        notes="Draft. " + WORK + " Among the earliest mass-market consumer EEG headsets.",
        prior_art_notes=(
            "Discloses a low-cost head-worn single-channel dry-electrode EEG device "
            "(forehead pickup, ear reference) outputting raw EEG plus derived 'attention' "
            "and 'meditation/relaxation' metrics to a paired device. Anticipates "
            "consumer-EEG-headband claims combining 'a head-worn dry forehead electrode "
            "with an ear reference', 'on-device band-power feature extraction', and "
            "'a derived attention/relaxation index' from 2007. Product-side anchor for the "
            "headband × EEG cross-cut; predates Muse (2014) and Emotiv EPOC (2009)."
        ),
        sources=["NeuroSky, Inc., MindSet / MindWave (product, 2007)."],
        cpc_classifications=["A61B 5/24", "A61B 5/375", "A61B 5/16", "A61B 5/372"],
    ),
    E(
        id="emotiv-epoc-2009",
        canonical_name="Emotiv EPOC (2009) — 14-channel wireless saline-electrode consumer EEG headset",
        aliases=["Emotiv EPOC", "Emotiv", "EPOC headset"],
        first_disclosure_date="2009-12",
        disclosure_citation="Emotiv Systems. 'EPOC' EEG headset, released December 2009 — a 14-channel (plus 2 reference) wireless headset with saline-felt electrodes covering frontal/temporal/parietal/occipital sites, with SDKs for mental-command, facial-expression and 'affective' detections.",
        creator="Emotiv Systems",
        creator_country="AU",
        form_factor="headband",
        form_factor_tags=["cap"],
        contact_surface="scalp",
        anatomical_target=["scalp", "AF3", "AF4", "F7", "F8", "T7", "T8", "O1", "O2"],
        sensors=["sensor-saline-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-cognitive-workload", "algo-emotion-recognition", "algo-bci-motor-imagery"],
        clinical_endpoints=["electroencephalogram", "affective-state", "mental-command"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a wireless multi-channel (14+2) consumer EEG headset with saline-"
            "wetted contact electrodes at standard scalp sites and on-device/SDK "
            "classifiers for mental commands, facial expressions, and affective states. "
            "Anticipates multi-channel consumer-EEG-headset claims combining 'a wireless "
            "head-worn array of ≥8 contact electrodes', 'wet/saline electrode coupling', "
            "and 'classification of cognitive/affective state or intent' from 2009. "
            "Product-side anchor for the headband/cap × EEG cross-cut."
        ),
        sources=["Emotiv Systems, EPOC (product, 2009)."],
        cpc_classifications=["A61B 5/24", "A61B 5/372", "A61B 5/16", "G06F 3/015"],
    ),
    E(
        id="muse-headband-2014",
        canonical_name="Muse headband (InteraXon, 2014) — multi-channel dry-electrode EEG headband for meditation and sleep",
        aliases=["Muse", "InteraXon Muse", "Muse S"],
        first_disclosure_date="2014-05",
        disclosure_citation="InteraXon Inc. 'Muse' brain-sensing headband, shipped 2014 — a forehead-band EEG device with frontal (AF7/AF8/Fp1/Fp2-region) and behind-the-ear (TP9/TP10) dry/conductive-rubber electrodes, giving real-time neurofeedback for meditation (and, in 'Muse S', sleep tracking).",
        creator="InteraXon Inc.",
        creator_country="CA",
        form_factor="headband",
        contact_surface="skin",
        anatomical_target=["forehead", "AF7", "AF8", "TP9", "TP10", "behind-ear"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-attention-state", "algo-cognitive-workload", "algo-sleep-staging"],
        clinical_endpoints=["electroencephalogram", "meditation-state", "sleep"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a forehead-band wearable EEG device with frontal and behind-the-ear "
            "(TP9/TP10) dry electrodes providing real-time neurofeedback for meditation "
            "training and (later) sleep staging. Anticipates EEG-headband claims combining "
            "'a forehead band', 'frontal and mastoid/behind-ear dry electrodes', and "
            "'real-time feedback on a meditation or sleep state' from 2014. Note: its "
            "TP9/TP10 around-ear pickup is the same general region used by "
            "[[zanetti-aminifar-atienza-eglass-2025]] — relevant prior art for "
            "around-ear-EEG wearable claims. Product-side anchor for the headband × EEG "
            "cross-cut."
        ),
        sources=["InteraXon Inc., Muse (product, 2014)."],
        cpc_classifications=["A61B 5/24", "A61B 5/375", "A61B 5/4812", "A61B 5/16"],
    ),
    E(
        id="medtronic-minimed-cgms-1999",
        canonical_name="Medtronic MiniMed CGMS (1999) — first FDA-cleared continuous glucose monitoring system",
        aliases=["MiniMed CGMS", "CGMS System Gold", "Medtronic CGMS"],
        first_disclosure_date="1999-06",
        disclosure_citation="MiniMed Inc. (later Medtronic Diabetes). 'Continuous Glucose Monitoring System (CGMS)', FDA-cleared June 1999 — the first commercial CGM: a subcutaneous needle-type amperometric glucose sensor coupled to a body-worn recorder logging interstitial-glucose readings for retrospective ('professional') review. (Real-time display followed with the Guardian RT, 2005.)",
        creator="MiniMed Inc. / Medtronic Diabetes",
        creator_country="US",
        form_factor="patch",
        form_factor_tags=["implantable", "belt"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "abdomen"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-pma",
        notes="Draft. " + WORK + " Exact PMA/clearance identifier to verify against the FDA database. The direct commercialization of the Shichiri 1982 needle-type wearable-CGM concept.",
        prior_art_notes=(
            "Discloses the first commercial continuous glucose monitor: a percutaneous "
            "needle-type amperometric glucose sensor in subcutaneous tissue feeding a "
            "body-worn recorder that logs interstitial glucose over days for review. "
            "Anticipates CGM-system claims combining 'a wearable housing', 'a subcutaneous "
            "needle-type enzyme-electrode glucose sensor', and 'logging/transmission of "
            "interstitial-glucose readings' from 1999 — a commercial realization of "
            "[[shichiri-1982-wearable-needle-glucose-sensor]] (1982). Product-side anchor "
            "for the patch × glucose-CGM cross-cut; Dexcom (2006) and Abbott Libre (2014) "
            "follow."
        ),
        sources=["MiniMed Inc. / Medtronic, Continuous Glucose Monitoring System (product, 1999)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61B 5/0002"],
    ),
    E(
        id="dexcom-sts-2006",
        canonical_name="Dexcom STS (2006) — early real-time continuous glucose monitoring system",
        aliases=["Dexcom STS", "Dexcom Seven", "Dexcom"],
        first_disclosure_date="2006-03",
        disclosure_citation="DexCom, Inc. 'STS Continuous Glucose Monitoring System', FDA-approved March 2006 — a subcutaneously inserted wire-type amperometric glucose sensor transmitting interstitial-glucose readings every few minutes to a small wireless receiver with trend display and alerts (7-day wear in the successor 'Seven').",
        creator="DexCom, Inc.",
        creator_country="US",
        form_factor="patch",
        form_factor_tags=["implantable"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "abdomen"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-pma",
        notes="Draft. " + WORK + " Exact PMA identifier to verify against the FDA database.",
        prior_art_notes=(
            "Discloses a real-time CGM: a subcutaneously inserted wire-type amperometric "
            "glucose sensor with a body-worn transmitter sending readings every few "
            "minutes to a wireless receiver showing the current value, trend arrow, and "
            "alerts. Anticipates real-time-CGM claims combining 'a subcutaneous glucose "
            "sensor with a wearable transmitter', 'periodic wireless transmission of "
            "glucose values', and 'a receiver presenting current value, trend, and "
            "threshold alerts' from 2006. Product-side anchor for the patch × glucose-CGM "
            "cross-cut alongside [[medtronic-minimed-cgms-1999]]."
        ),
        sources=["DexCom, Inc., STS Continuous Glucose Monitoring System (product, 2006)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61B 5/0031", "A61B 5/746"],
    ),
    E(
        id="abbott-freestyle-libre-2014",
        canonical_name="Abbott FreeStyle Libre (2014) — factory-calibrated flash glucose monitoring",
        aliases=["FreeStyle Libre", "Libre", "flash glucose monitoring"],
        first_disclosure_date="2014-09",
        disclosure_citation="Abbott Diabetes Care. 'FreeStyle Libre' flash glucose monitoring system, CE-marked / launched in Europe September 2014 (US clearance: FreeStyle Libre Pro 2016; consumer FreeStyle Libre 2017) — a small adhesive coin-sized patch with a subcutaneous wire-type glucose sensor, factory-calibrated (no fingerstick calibration), 14-day wear, read on demand by NFC-scanning the patch with a reader or phone (later 'Libre 2'/'Libre 3' add real-time Bluetooth streaming and alarms).",
        creator="Abbott Diabetes Care",
        creator_country="US",
        form_factor="patch",
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "upper-arm"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-de-novo",
        connectivity="nfc",
        notes="Draft. " + WORK + " Exact FDA identifiers (Libre Pro 2016 510(k); consumer Libre 2017; Libre 2 De Novo 2018) to verify.",
        prior_art_notes=(
            "Discloses a coin-sized adhesive patch with a subcutaneous wire-type glucose "
            "sensor that is factory-calibrated (eliminating fingerstick calibration), worn "
            "up to 14 days, and read on demand by NFC-scanning the patch (with later "
            "variants adding continuous Bluetooth streaming and threshold alarms). "
            "Anticipates flash/CGM claims combining 'a low-profile adhesive patch sensor', "
            "'factory calibration without user blood-glucose calibration', 'extended "
            "(≥14-day) wear', and 'on-demand NFC readout' from 2014. Product-side anchor "
            "for the patch × glucose-CGM cross-cut."
        ),
        sources=["Abbott Diabetes Care, FreeStyle Libre (product, 2014/2017)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61B 5/0008", "A61B 5/7475"],
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
    print(f"  real products r2: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
