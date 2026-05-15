#!/usr/bin/env python3
"""seed_2026q3_real_r4_products.py — more commercial wearable products (draft tier).

GPS running watches; sensor-packed wristbands; smartwatch ECG/BP; cuffless
BP devices; the first true hearables; AirPods hearing health; long-term
implantable and patch CGM; the first FDA-cleared seizure-monitoring
smartwatch; the EMG gesture armband.

All draft:true (ip_status patented) — patent numbers and, where applicable,
exact FDA identifiers still need enumeration; the slug, the prior-art date,
and the follow-up work are captured per the corpus quality bar.

Run from repo root:  python3 seeds/seed_2026q3_real_r4_products.py
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
        id="garmin-forerunner-201-2003",
        canonical_name="Garmin Forerunner 201 (2003) — wristworn GPS running watch with pace/distance and heart-rate (strap) integration",
        aliases=["Garmin Forerunner", "Forerunner 201", "Forerunner 101"],
        first_disclosure_date="2003",
        disclosure_citation="Garmin Ltd. 'Forerunner 101/201', introduced 2003 — a wrist-worn GPS receiver/watch logging pace, distance, route, and (with a paired chest strap) heart rate, with workout history and a web/PC sync. Later Garmin watches (Fenix/Forerunner with the 'Elevate' optical sensor, c. 2015) moved heart rate, and subsequently SpO2 (pulse ox) and respiration, onto the wrist.",
        creator="Garmin Ltd.",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["garment"],
        contact_surface="skin",
        anatomical_target=["wrist", "chest"],
        sensors=["sensor-accelerometer", "sensor-ecg", "sensor-ppg"],
        algorithms=["algo-hr", "algo-step-count", "algo-calorie-estimation", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "running-pace", "activity"],
        notes="Draft. " + WORK + " The 2003 product is GPS + strap-HR; on-wrist optical HR (Garmin Elevate) is c. 2015, wrist pulse-ox later — note when promoting.",
        prior_art_notes=(
            "Discloses a wrist-worn GPS sport watch deriving pace, distance, and route, "
            "integrating heart rate from a paired electrode chest strap, and syncing "
            "workout history to a host — and, in later Garmin models, on-wrist optical-PPG "
            "heart rate, SpO2, and respiration. Anticipates GPS-sport-watch claims from "
            "2003 and (for the later models) wrist-optical-vitals claims. Product-side "
            "anchor for the watch × GPS-fitness cross-cut."
        ),
        sources=["Garmin Ltd., Forerunner 101/201 (product, 2003)."],
        cpc_classifications=["A61B 5/02438", "G01S 19/19", "A61B 5/1118", "G04G 21/04"],
    ),
    E(
        id="fitbit-charge-hr-2015",
        canonical_name="Fitbit Charge HR (2015) — wristband with continuous wrist-PPG heart rate ('PurePulse')",
        aliases=["Fitbit Charge HR", "PurePulse"],
        first_disclosure_date="2015-01-06",
        disclosure_citation="Fitbit, Inc. 'Fitbit Charge HR', announced January 2015 — a wristband with 'PurePulse' continuous optical (green-LED PPG) heart rate, a 3-axis accelerometer, steps/distance/floors/calories/active-minutes, automatic sleep tracking, and call/text notifications.",
        creator="Fitbit, Inc.",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-accelerometer", "sensor-barometer"],
        algorithms=["algo-hr", "algo-step-count", "algo-calorie-estimation", "algo-activity-classification", "algo-sleep-staging"],
        clinical_endpoints=["heart-rate", "activity", "sleep"],
        lineage_ancestors=["fitbit-tracker-2009"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a wristband with continuous green-LED reflectance-PPG heart rate "
            "plus accelerometry and an altimeter, deriving HR, steps, floors, calories, "
            "and sleep, with phone notifications. A mainstream realization of "
            "[[mendelson-ochs-1988-reflectance-pulse-oximetry]]-geometry wrist PPG; "
            "anticipates wrist-PPG-HR-band claims from January 2015. Product-side anchor "
            "for the watch × PPG cross-cut alongside [[apple-watch-original-2015]]."
        ),
        sources=["Fitbit, Inc., Fitbit Charge HR (product, 2015)."],
        cpc_classifications=["A61B 5/02416", "A61B 5/681", "A61B 5/1118", "G04G 21/04"],
    ),
    E(
        id="microsoft-band-2014",
        canonical_name="Microsoft Band (2014) — ten-sensor wristband (optical HR, GPS, GSR, UV, skin temp, barometer, ambient light, capacitive, microphone, IMU)",
        aliases=["Microsoft Band", "MS Band", "Microsoft Band 2"],
        first_disclosure_date="2014-10-30",
        disclosure_citation="Microsoft Corp. 'Microsoft Band', released 30 October 2014 — a wristband integrating ten sensors: an optical (PPG) heart-rate sensor, a 3-axis accelerometer/gyroscope, GPS, an ambient-light sensor, a skin-temperature sensor, a UV sensor, a capacitive (wear-detection) sensor, a galvanic-skin-response sensor, a microphone, and a barometer (added in Band 2).",
        creator="Microsoft Corp.",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-accelerometer", "sensor-gyroscope", "sensor-skin-temperature", "sensor-uv", "sensor-gsr", "sensor-barometer", "sensor-photodiode-ambient", "sensor-microphone-air"],
        algorithms=["algo-hr", "algo-step-count", "algo-calorie-estimation", "algo-sleep-staging", "algo-stress-index", "algo-uv-dose-tracking"],
        clinical_endpoints=["heart-rate", "skin-temperature", "uv-exposure", "electrodermal-activity", "sleep", "activity"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a single wristband integrating an unusually broad sensor suite — "
            "reflectance-PPG HR, IMU, GPS, skin temperature, UV exposure, galvanic skin "
            "response (electrodermal activity), barometer, ambient light, capacitive "
            "wear-detection, and a microphone — feeding HR, activity, sleep, UV dose, and "
            "stress-index estimations. Prior art for multi-sensor-wristband claims "
            "reciting combinations of these sensors (notably wrist GSR/EDA + PPG + skin "
            "temperature for stress) from October 2014. Product-side anchor for the "
            "multi-sensor wristband cross-cut."
        ),
        sources=["Microsoft Corp., Microsoft Band (product, 2014)."],
        cpc_classifications=["A61B 5/02438", "A61B 5/0531", "A61B 5/01", "A61B 5/1118"],
    ),
    E(
        id="bragi-dash-2014",
        canonical_name="Bragi Dash (2014) — the first true 'hearable': in-ear PPG heart rate, accelerometer, storage and touch control inside wireless earbuds",
        aliases=["Bragi Dash", "The Dash", "hearable"],
        first_disclosure_date="2014-02-25",
        disclosure_citation="Bragi GmbH. 'The Dash' wireless smart earphones, crowdfunded February 2014 (shipped 2016) — fully wireless in-ear earbuds with a reflectance-PPG heart-rate sensor and oxygen-saturation estimation against the ear-canal wall, a 3-axis accelerometer (head-gesture and step/activity tracking), 4 GB onboard music storage, bone-conduction microphone, and capacitive touch control.",
        creator="Bragi GmbH",
        creator_country="DE",
        form_factor="earbud",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        sensors=["sensor-ppg", "sensor-spo2", "sensor-accelerometer", "sensor-microphone-bone"],
        algorithms=["algo-hr", "algo-spo2-estimation", "algo-step-count", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "blood-oxygen", "activity"],
        notes="Draft. " + WORK + " Widely regarded as the first 'hearable' — biosensors inside fully-wireless earbuds.",
        prior_art_notes=(
            "Discloses fully-wireless in-ear earbuds with a reflectance-PPG heart-rate and "
            "SpO2 sensor against the ear-canal wall, an accelerometer for head-gesture and "
            "step/activity tracking, onboard music storage, a bone-conduction microphone, "
            "and capacitive touch control — i.e. physiological sensing integrated into "
            "wireless earbuds. Anticipates hearable claims combining 'a wireless earbud "
            "housing', 'an in-ear PPG/SpO2 sensor', 'an accelerometer for activity or "
            "head gesture', and 'on-device media and controls' from 2014. Product-side "
            "anchor for the earbud × PPG cross-cut."
        ),
        sources=["Bragi GmbH, The Dash (product, 2014/2016)."],
        cpc_classifications=["A61B 5/02416", "H04R 1/10", "A61B 5/1118", "A61B 5/14552"],
    ),
    E(
        id="apple-airpods-pro-2-hearing-health-2024",
        canonical_name="Apple AirPods Pro 2 Hearing Health (2024) — earbuds as a clinical hearing test, OTC hearing aid, and hearing protection",
        aliases=["AirPods Pro 2 hearing aid", "AirPods Hearing Test", "AirPods hearing health"],
        first_disclosure_date="2024-09-09",
        disclosure_citation="Apple Inc. 'AirPods Pro 2' Hearing Health features, announced 9 September 2024 (FDA-authorized hearing-aid software, October 2024) — the earbuds perform an audiogram-style hearing test, then function as a software over-the-counter hearing aid (frequency-specific amplification tuned to the test result, with real-time conversation enhancement), plus passive/active hearing protection that attenuates loud environmental sound.",
        creator="Apple Inc.",
        creator_country="US",
        form_factor="earbud",
        form_factor_tags=["hearing-aid"],
        contact_surface="ear",
        anatomical_target=["ear-canal", "ear"],
        sensors=["sensor-microphone-air"],
        clinical_endpoints=["audiogram", "hearing-threshold", "auditory-perception"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK + " 2024 hearing-health software authorized by FDA (OTC hearing aid pathway) — verify the exact authorization identifier. The base AirPods Pro 2 hardware launched 2022; the hearing-aid/hearing-test software is 2024.",
        prior_art_notes=(
            "Discloses consumer earbuds that (a) administer an audiogram-style pure-tone "
            "hearing test to the wearer, (b) operate as a software over-the-counter "
            "hearing aid applying the resulting frequency-specific gain (with "
            "conversation/speech enhancement and directional processing), and (c) provide "
            "loud-sound hearing protection. Anticipates earbud/hearing-aid claims "
            "combining 'a self-administered hearing assessment by the worn device', "
            "'configuration of the device's amplification from that assessment', and "
            "'protective attenuation of loud environmental sound' from 2024. Product-side "
            "anchor for the earbud-as-hearing-aid cross-cut; cf. [[bionic-woman-bionic-ear]] "
            "(the fictional antecedent of steerable/frequency-selective augmented hearing)."
        ),
        sources=["Apple Inc., AirPods Pro 2 Hearing Health (product/software, 2024)."],
        cpc_classifications=["H04R 25/70", "H04R 25/00", "A61B 5/12", "H04R 1/10"],
    ),
    E(
        id="samsung-galaxy-watch-bp-ecg-2020",
        canonical_name="Samsung Galaxy Watch3 / Samsung Health Monitor (2020) — wrist single-lead ECG and optical-PPG cuffless blood pressure",
        aliases=["Samsung Health Monitor", "Galaxy Watch ECG", "Galaxy Watch blood pressure"],
        first_disclosure_date="2020-08",
        disclosure_citation="Samsung Electronics. 'Samsung Health Monitor' app on Galaxy Watch3 / Watch Active2, 2020 — wrist single-lead ECG (between a back-crystal electrode and a side-button electrode touched by the opposite hand, with AF/sinus classification) and a cuffless blood-pressure feature using the optical (PPG) pulse-wave signal calibrated against a periodic conventional cuff reading. (Cleared in Korea 2020; subsequently in other markets.)",
        creator="Samsung Electronics Co., Ltd.",
        creator_country="KR",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist", "fingertip"],
        sensors=["sensor-ecg", "sensor-ppg", "sensor-cuffless-bp-ptt"],
        algorithms=["algo-afib-detection", "algo-arrhythmia-classification", "algo-pwv-bp-estimation", "algo-hr"],
        clinical_endpoints=["electrocardiogram", "atrial-fibrillation", "blood-pressure", "heart-rate"],
        regulatory_pathway="ce-mdr",
        notes="Draft. " + WORK + " Verify the regulatory clearance identifiers (Korea MFDS 2020; CE; later FDA for ECG/IRN).",
        prior_art_notes=(
            "Discloses a wristworn device that takes a single-lead ECG with on-device "
            "AF classification and, separately, estimates blood pressure from the wrist "
            "optical-PPG pulse waveform after calibration against a periodic conventional "
            "cuff measurement (a calibrated-cuffless approach). Anticipates wrist-cuffless-"
            "BP claims reciting 'estimating blood pressure from a wrist photoplethysmography "
            "signal calibrated by a reference cuff reading' from 2020 — the underlying "
            "PTT/PWV-BP technique is much older ([[geddes-1981-pulse-transit-time-bp]], "
            "[[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the "
            "watch × cuffless-BP cross-cut."
        ),
        sources=["Samsung Electronics, Samsung Health Monitor on Galaxy Watch3 (product, 2020)."],
        cpc_classifications=["A61B 5/318", "A61B 5/02125", "A61B 5/021", "A61B 5/352"],
    ),
    E(
        id="omron-heartguide-2019",
        canonical_name="Omron HeartGuide (2019) — wristwatch with an inflatable oscillometric blood-pressure cuff in the band",
        aliases=["Omron HeartGuide", "HeartGuide BP watch", "Omron Project Zero"],
        first_disclosure_date="2019-01-08",
        disclosure_citation="Omron Healthcare. 'HeartGuide' (model BP8000-M), announced January 2019, FDA-cleared — a wristwatch whose band contains an inflatable cuff and an oscillometric pressure transducer, taking a clinically-validated brachial-style blood-pressure measurement at the wrist on demand, alongside heart rate, steps, and sleep.",
        creator="Omron Healthcare Co., Ltd.",
        creator_country="JP",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-pressure-skin", "sensor-accelerometer", "sensor-ppg"],
        algorithms=["algo-hr", "algo-step-count", "algo-sleep-staging"],
        clinical_endpoints=["blood-pressure", "heart-rate", "activity", "sleep"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK + " Verify the exact FDA 510(k) number for the BP8000-M (HeartGuide).",
        prior_art_notes=(
            "Discloses a wristwatch whose strap incorporates an inflatable cuff and "
            "pressure transducer, performing an oscillometric blood-pressure measurement "
            "at the wrist (occlude-and-release, automatically positioned at heart level by "
            "the wearer) in a watch form factor, plus activity and sleep tracking. Distinct "
            "from cuffless-PPG approaches: it is a true oscillometric cuff miniaturized "
            "into a watch band. Anticipates watch-with-integrated-inflatable-cuff BP "
            "claims from 2019. Product-side anchor for the watch × oscillometric-BP "
            "cross-cut (vs. the cuffless-PPG variant in "
            "[[samsung-galaxy-watch-bp-ecg-2020]] and [[aktiia-bracelet-cuffless-bp-2021]])."
        ),
        sources=["Omron Healthcare, HeartGuide BP8000-M (product, 2019)."],
        cpc_classifications=["A61B 5/02233", "A61B 5/0225", "A61B 5/022", "G04G 21/04"],
    ),
    E(
        id="aktiia-bracelet-cuffless-bp-2021",
        canonical_name="Aktiia bracelet (2021) — optical-PPG-based continuous cuffless blood-pressure monitoring bracelet",
        aliases=["Aktiia", "Aktiia bracelet", "Hilo (Aktiia)"],
        first_disclosure_date="2021-01",
        disclosure_citation="Aktiia SA. 'Aktiia bracelet' (later 'Hilo'), CE-marked and launched in Europe January 2021 — a slim wristband with optical photoplethysmography that, after a one-time initialization against a conventional cuff (and periodic re-calibration), estimates systolic and diastolic blood pressure several times a day automatically, day and night, from the wrist PPG pulse waveform.",
        creator="Aktiia SA",
        creator_country="CH",
        form_factor="bracelet",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-cuffless-bp-ptt", "sensor-accelerometer"],
        algorithms=["algo-pwv-bp-estimation", "algo-hr"],
        clinical_endpoints=["blood-pressure", "heart-rate"],
        regulatory_pathway="ce-mdr",
        notes="Draft. " + WORK + " Verify the CE certificate and any FDA submission identifiers.",
        prior_art_notes=(
            "Discloses a slim wristband that, after a one-time cuff initialization (and "
            "periodic re-calibration), automatically estimates systolic and diastolic "
            "blood pressure multiple times per day and night purely from the wrist "
            "optical-PPG pulse waveform — i.e. continuous, fully cuffless, "
            "calibration-initialized wrist BP monitoring. Anticipates continuous-cuffless-"
            "wrist-BP claims from 2021; the PPG-pulse-feature-to-BP mapping rests on the "
            "much older PTT/PWV-BP and pulse-contour literature "
            "([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). "
            "Product-side anchor for the bracelet × cuffless-BP cross-cut."
        ),
        sources=["Aktiia SA, Aktiia bracelet (product, 2021)."],
        cpc_classifications=["A61B 5/02125", "A61B 5/021", "A61B 5/02416", "A61B 5/681"],
    ),
    E(
        id="withings-scanwatch-2020",
        canonical_name="Withings ScanWatch (2020) — hybrid analog watch with PPG, SpO2 pulse oximetry, single-lead ECG, and accelerometer",
        aliases=["Withings ScanWatch", "ScanWatch"],
        first_disclosure_date="2020-01-05",
        disclosure_citation="Withings (Nokia/Withings). 'ScanWatch', announced January 2020 (CE-marked 2020; FDA cleared 2022) — a hybrid analog wristwatch integrating a reflectance-PPG sensor (heart rate, irregular-rhythm screening), an SpO2 (pulse-oximetry) measurement, a single-lead ECG (back electrode plus a bezel electrode touched by the opposite hand, with AF detection), a 3-axis accelerometer, and an altimeter — with sleep and activity tracking.",
        creator="Withings SA",
        creator_country="FR",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist", "fingertip"],
        sensors=["sensor-ppg", "sensor-spo2", "sensor-ecg", "sensor-accelerometer", "sensor-barometer"],
        algorithms=["algo-hr", "algo-spo2-estimation", "algo-afib-detection", "algo-arrhythmia-classification", "algo-sleep-staging", "algo-step-count", "algo-respiratory-rate"],
        clinical_endpoints=["heart-rate", "blood-oxygen", "electrocardiogram", "atrial-fibrillation", "sleep", "activity"],
        regulatory_pathway="ce-mdr",
        notes="Draft. " + WORK + " Verify CE certificate and FDA 510(k) identifiers (ScanWatch SpO2 / ECG, 2020-2022).",
        prior_art_notes=(
            "Discloses a wristwatch combining reflectance-PPG heart rate, pulse-oximetry "
            "SpO2, a single-lead ECG with AF detection, accelerometry, and an altimeter, "
            "with sleep-apnea screening (from the SpO2/respiration signals) — multiple "
            "regulated cardiorespiratory measurements in one consumer watch. Anticipates "
            "multi-modal medical-smartwatch claims reciting combinations of wrist PPG-HR "
            "+ wrist SpO2 + single-lead ECG from 2020. Product-side anchor for the "
            "watch × {PPG, SpO2, ECG} multi-sensor cross-cut."
        ),
        sources=["Withings SA, ScanWatch (product, 2020)."],
        cpc_classifications=["A61B 5/02416", "A61B 5/14552", "A61B 5/318", "A61B 5/4818"],
    ),
    E(
        id="empatica-embrace2-seizure-watch-2018",
        canonical_name="Empatica Embrace2 (2018) — first FDA-cleared seizure-monitoring smartwatch (accelerometer + electrodermal activity)",
        aliases=["Empatica Embrace", "Embrace2", "Embrace smartwatch"],
        first_disclosure_date="2018-01-31",
        disclosure_citation="Empatica Inc. 'Embrace2' smartwatch, FDA-cleared January 2018 — a wrist-worn device with a 3-axis accelerometer/gyroscope, an electrodermal-activity (EDA) sensor, and a peripheral skin-temperature sensor, running an on-device classifier that detects probable generalized tonic-clonic seizures from the combined motion + EDA signature and alerts caregivers; the first FDA-cleared smartwatch for seizure monitoring. (Descends from the MIT Media Lab 'iCalm'/'Q sensor' EDA wristband research, Picard et al.)",
        creator="Empatica Inc. (Rosalind Picard, Matteo Lai, et al.)",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-accelerometer", "sensor-gyroscope", "sensor-gsr", "sensor-skin-temperature"],
        algorithms=["algo-seizure-detection", "algo-stress-index", "algo-activity-classification"],
        clinical_endpoints=["seizure-event", "electrodermal-activity", "skin-temperature", "activity"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK + " Verify the exact FDA clearance identifier (Embrace, 2018). Lineage from the MIT Media Lab EDA-wristband work (iCalm/Q sensor).",
        prior_art_notes=(
            "Discloses a wristworn device that detects probable generalized tonic-clonic "
            "seizures by combining a motion (accelerometer/gyroscope) signature with an "
            "electrodermal-activity (sympathetic-surge) signature in an on-device "
            "classifier, and alerts caregivers — i.e. multimodal wrist-based seizure "
            "detection, distinct from the EEG-based approach. Anticipates wrist-seizure-"
            "detection claims combining 'a wrist-worn accelerometer and an electrodermal-"
            "activity sensor' and 'a classifier flagging a seizure from their combined "
            "signal' from 2018. Product-side anchor for the wrist × seizure-detection "
            "cross-cut; complementary to the EEG route in "
            "[[zanetti-aminifar-atienza-eglass-2025]] and [[chb-mit-scalp-eeg-database-2009]]."
        ),
        sources=["Empatica Inc., Embrace2 (product, 2018)."],
        cpc_classifications=["A61B 5/4094", "A61B 5/0531", "A61B 5/1117", "A61B 5/01"],
    ),
    E(
        id="eversense-implantable-cgm-2018",
        canonical_name="Senseonics Eversense (2018) — first long-term implantable continuous glucose monitor (fluorescence sensor + on-skin transmitter)",
        aliases=["Eversense", "Senseonics Eversense", "implantable CGM"],
        first_disclosure_date="2018-06",
        disclosure_citation="Senseonics, Inc. 'Eversense Continuous Glucose Monitoring System', FDA-approved June 2018 (CE-marked earlier) — a small fluorescence-based glucose sensor implanted subcutaneously in the upper arm for 90 days (later 180+ days), read by a removable transmitter worn on the skin over it that powers the sensor inductively, computes glucose, and streams it to a phone with on-body vibratory alerts.",
        creator="Senseonics, Inc.",
        creator_country="US",
        form_factor="implantable",
        form_factor_tags=["patch"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "upper-arm"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-pma",
        notes="Draft. " + WORK + " Verify the exact FDA PMA identifier (Eversense, 2018).",
        prior_art_notes=(
            "Discloses a long-term (months) implantable glucose sensor — a fluorescence-"
            "chemistry sensor implanted subcutaneously — paired with a removable on-skin "
            "transmitter that inductively powers and reads the sensor, derives glucose, "
            "streams it wirelessly, and gives on-body vibratory alerts. Distinct from the "
            "needle/wire-type CGMs ([[shichiri-1982-wearable-needle-glucose-sensor]], "
            "[[dexcom-sts-2006]], [[abbott-freestyle-libre-2014]]): a fully implanted, "
            "wirelessly-powered, fluorescence-based long-term sensor with a separable "
            "wearable reader. Anticipates implantable-CGM claims reciting that "
            "architecture from 2018. Product-side anchor for the implantable × glucose-CGM "
            "cross-cut."
        ),
        sources=["Senseonics, Inc., Eversense CGM System (product, 2018)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1473", "A61B 5/0031", "A61B 5/1486"],
    ),
    E(
        id="dexcom-g6-2018",
        canonical_name="Dexcom G6 (2018) — no-calibration real-time CGM with predictive low-glucose alert and direct phone streaming",
        aliases=["Dexcom G6", "Dexcom G7"],
        first_disclosure_date="2018-03",
        disclosure_citation="DexCom, Inc. 'Dexcom G6 Continuous Glucose Monitoring System', FDA-cleared March 2018 — a subcutaneous wire-type glucose sensor with a low-profile on-skin transmitter, factory-calibrated (no fingerstick calibration), 10-day wear, 5-minute readings streamed directly to a phone or receiver, with customizable alerts and a predictive 'urgent low soon' alarm; the successor Dexcom G7 (2022) is smaller with a faster warm-up.",
        creator="DexCom, Inc.",
        creator_country="US",
        form_factor="patch",
        form_factor_tags=["implantable"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "abdomen", "upper-arm"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-de-novo",
        lineage_ancestors=["dexcom-sts-2006"],
        notes="Draft. " + WORK + " Verify the exact FDA identifiers (G6 510(k)/De Novo 2018; iCGM De Novo DEN170088 cited from memory — verify).",
        prior_art_notes=(
            "Discloses a real-time CGM that is factory-calibrated (no user blood-glucose "
            "calibration), worn 10 days, streams 5-minute glucose values directly to a "
            "phone, and provides a predictive low-glucose alert ('urgent low soon') in "
            "addition to threshold and rate alarms. Anticipates CGM claims reciting "
            "'factory calibration without user calibration', 'direct streaming to a "
            "general-purpose mobile device', and 'a predictive (forecast-based) "
            "hypoglycemia alert' from 2018. Product-side anchor for the patch × "
            "glucose-CGM cross-cut alongside [[abbott-freestyle-libre-2014]]."
        ),
        sources=["DexCom, Inc., Dexcom G6 CGM System (product, 2018)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61B 5/746", "G16H 50/20"],
    ),
    E(
        id="abbott-freestyle-libre-2-2018",
        canonical_name="Abbott FreeStyle Libre 2 (2018) — factory-calibrated CGM patch with real-time Bluetooth streaming and optional glucose alarms",
        aliases=["FreeStyle Libre 2", "Libre 2", "Libre 3"],
        first_disclosure_date="2018-10",
        disclosure_citation="Abbott Diabetes Care. 'FreeStyle Libre 2', CE-marked October 2018 (US clearance 2020) — the FreeStyle Libre patch sensor (coin-sized adhesive, subcutaneous wire-type sensor, factory-calibrated, 14-day wear) augmented with continuous Bluetooth transmission to the reader/phone and optional real-time high/low/signal-loss glucose alarms (no scan required for alerts); FreeStyle Libre 3 (2020-2022) is smaller with continuous minute-by-minute streaming.",
        creator="Abbott Diabetes Care",
        creator_country="US",
        form_factor="patch",
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "upper-arm"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        regulatory_pathway="fda-de-novo",
        lineage_ancestors=["abbott-freestyle-libre-2014"],
        notes="Draft. " + WORK + " Verify CE/FDA identifiers (Libre 2, 2018/2020; Libre 3).",
        prior_art_notes=(
            "Discloses the small adhesive factory-calibrated CGM patch (14-day, subcutaneous "
            "wire sensor) extended with continuous Bluetooth transmission and optional "
            "real-time glucose alarms without requiring a scan — closing the gap to "
            "alarm-capable real-time CGM at a low-profile patch form factor. Anticipates "
            "patch-CGM claims reciting 'a factory-calibrated adhesive patch sensor with "
            "continuous wireless streaming and configurable real-time alarms' from 2018. "
            "Product-side anchor for the patch × glucose-CGM cross-cut."
        ),
        sources=["Abbott Diabetes Care, FreeStyle Libre 2 (product, 2018/2020)."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61B 5/0008", "A61B 5/746"],
    ),
    E(
        id="myo-armband-2014",
        canonical_name="Thalmic Labs Myo armband (2014) — consumer surface-EMG gesture-control armband",
        aliases=["Myo armband", "Thalmic Myo", "Myo"],
        first_disclosure_date="2013-02-25",
        disclosure_citation="Thalmic Labs Inc. 'Myo gesture control armband', announced February 2013, shipped 2014 — a forearm-worn band of eight medical-grade stainless-steel surface-EMG electrode segments plus a 9-axis IMU, recognizing hand and finger gestures from the forearm-muscle electrical activity and arm orientation/motion, and transmitting them over Bluetooth as input to computers/devices.",
        creator="Thalmic Labs Inc. (later North)",
        creator_country="CA",
        form_factor="armband",
        contact_surface="skin",
        anatomical_target=["forearm"],
        sensors=["sensor-emg", "sensor-accelerometer", "sensor-gyroscope", "sensor-magnetometer"],
        algorithms=["algo-hand-gesture-emg", "algo-keystroke-emg"],
        clinical_endpoints=["electromyogram", "gesture-class", "arm-orientation"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a forearm-worn band with an array of eight surface-EMG electrodes "
            "plus a 9-axis IMU that recognizes hand/finger gestures from forearm-muscle "
            "EMG combined with arm motion/orientation and transmits them wirelessly as a "
            "control input. A consumer realization of the myoelectric pattern-recognition "
            "approach ([[englehart-hudgins-2003-myoelectric-control]]); anticipates "
            "EMG-gesture-armband claims combining 'a band of surface-EMG electrodes worn "
            "around the forearm', 'an inertial sensor', and 'a classifier mapping the "
            "combined signal to a hand gesture / control command' from 2014. Product-side "
            "anchor for the armband × EMG cross-cut (the only `armband` form-factor entry "
            "besides [[mass-effect-omni-tool]] and [[fallout-pip-boy]])."
        ),
        sources=["Thalmic Labs Inc., Myo gesture control armband (product, 2013/2014)."],
        cpc_classifications=["A61B 5/389", "G06F 3/015", "G06F 3/017", "A61B 5/1118"],
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
    print(f"  real products r4: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
