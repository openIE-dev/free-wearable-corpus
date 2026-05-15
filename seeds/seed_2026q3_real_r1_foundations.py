#!/usr/bin/env python3
"""seed_2026q3_real_r1_foundations.py — academic / open-hardware / standards foundations.

The canonical primary-source anchors for the major sensor and algorithm
cross-cuts: PPG (Hertzman 1937), pulse oximetry, ECG (Einthoven 1903,
Holter 1961), EEG (Berger 1929), sleep staging (Aserinsky-Kleitman 1953,
Rechtschaffen-Kales 1968), HRV (ESC/NASPE 1996), electrochemical glucose
sensing (Clark-Lyons 1962, Updike-Hicks 1967), wearable CGM (Shichiri 1982),
fall detection, BCI (Wolpaw 2002), wearable EEG glasses (e-Glass 2025),
the MIT wearable ring sensor, open-source biosignal hardware (OpenBCI),
and the relevant Bluetooth SIG / IEEE 11073 / ISO 80601 / Continua standards.

These are the entries with real invalidity-contention bite — every one is
a primary disclosure verifiable by a third party.

Run from repo root:  python3 seeds/seed_2026q3_real_r1_foundations.py
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
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    # ---------------- PPG / PULSE OXIMETRY ----------------
    E(
        id="hertzman-1937-photoplethysmography",
        canonical_name="Hertzman (1937) — photoelectric plethysmography (the origin of PPG)",
        aliases=["photoelectric plethysmograph", "Hertzman PPG"],
        corpus="academic",
        first_disclosure_date="1937",
        disclosure_citation="Hertzman AB. 'Photoelectric plethysmography of the fingers and toes in man.' Proceedings of the Society for Experimental Biology and Medicine 1937;37(3):529-534.",
        creator="Alrick B. Hertzman",
        creator_country="US",
        form_factor="other",
        contact_surface="skin",
        anatomical_target=["finger", "toe"],
        sensors=["sensor-ppg"],
        clinical_endpoints=["blood-volume-pulse"],
        ip_status="public-domain",
        notes="Form factor 'other' — the original apparatus was a finger/toe photocell probe, not a body-worn device; it is the disclosure root for every wrist/finger/ear/forehead PPG wearable that followed.",
        prior_art_notes=(
            "Coins and demonstrates 'photoelectric plethysmography' — measuring the "
            "pulsatile change in transmitted/reflected light through perfused tissue to "
            "track blood volume pulse. This is the disclosure root of the entire PPG "
            "wearable space: every claim reciting 'a photoplethysmography sensor' or "
            "'a light source and a photodetector arranged to measure a blood volume pulse "
            "in tissue' reads on Hertzman 1937. As § 102 prior art for the bare PPG "
            "principle it is dispositive; combined with any form-factor disclosure it "
            "renders the form-factor+PPG combination obvious under "
            "[[obviousness-template]]."
        ),
        sources=["Hertzman AB. Proc Soc Exp Biol Med 1937;37:529-534."],
        cpc_classifications=["A61B 5/02416", "A61B 5/024", "A61B 5/1455"],
    ),
    E(
        id="allen-2007-ppg-review",
        canonical_name="Allen (2007) — 'Photoplethysmography and its application in clinical physiological measurement'",
        aliases=["Allen PPG review"],
        corpus="academic",
        first_disclosure_date="2007-02-20",
        disclosure_citation="Allen J. 'Photoplethysmography and its application in clinical physiological measurement.' Physiological Measurement 2007;28(3):R1-R39. doi:10.1088/0967-3334/28/3/R01.",
        creator="John Allen (Freeman Hospital / Newcastle)",
        creator_country="GB",
        form_factor="other",
        contact_surface="skin",
        sensors=["sensor-ppg"],
        algorithms=["algo-hr", "algo-hrv", "algo-respiratory-rate", "algo-spo2-estimation", "algo-pwv-bp-estimation"],
        clinical_endpoints=["heart-rate", "respiratory-rate", "blood-oxygen", "blood-pressure", "arterial-stiffness"],
        ip_status="public-domain",
        prior_art_notes=(
            "Canonical review collecting the state of PPG measurement and the physiological "
            "parameters derivable from a PPG signal as of 2007 — heart rate, HRV, "
            "respiratory rate, SpO2, blood-pressure surrogates, arterial-stiffness/aging "
            "indices, vasomotor assessment. Relevant to wearable claims that recite "
            "'deriving [parameter X] from a photoplethysmography signal' for any X covered "
            "here: the derivation was a published, enabled technique by 2007, defeating "
            "novelty of the bare derivation and supplying § 103 motivation for the "
            "form-factor+PPG+algorithm combinations. The single most-cited anchor for "
            "PPG-derived-metric wearable patents."
        ),
        sources=["Allen J. Physiol Meas 2007;28(3):R1-R39."],
        cpc_classifications=["A61B 5/02416", "A61B 5/024", "A61B 5/1455", "A61B 5/021"],
    ),
    E(
        id="aoyagi-1974-two-wavelength-pulse-oximetry",
        canonical_name="Aoyagi (1974) — two-wavelength pulse oximetry principle",
        aliases=["Aoyagi pulse oximeter", "ratio-of-ratios oximetry"],
        corpus="private",
        first_disclosure_date="1974",
        disclosure_citation="Aoyagi T, et al. — the pulsatile two-wavelength (red/infrared) ratio method for non-invasive arterial oxygen saturation, presented at the 13th Annual Meeting of the Japan Society of Medical Electronics and Biological Engineering (1974); commercialized as the Nihon Kohden 'Ear Oximeter OLV-5100' (1975) and Minolta 'Oximet MET-1471' (1977). History documented in Severinghaus JW, Honda Y. 'History of blood gas analysis. VII. Pulse oximetry.' J Clin Monit 1987;3(2):135-138.",
        creator="Takuo Aoyagi (Nihon Kohden)",
        creator_country="JP",
        form_factor="other",
        form_factor_tags=["earbud"],
        contact_surface="ear",
        anatomical_target=["earlobe", "finger"],
        sensors=["sensor-spo2", "sensor-ppg", "sensor-multi-wavelength-ppg"],
        algorithms=["algo-spo2-estimation"],
        clinical_endpoints=["blood-oxygen"],
        ip_status="patented",
        draft=True,
        notes="Draft: ip_status patented but the Aoyagi/Nihon Kohden 1974 Japanese patent number(s) need enumeration. Disclosure citation (the 1974 conference presentation, the 1975/1977 products, and the Severinghaus-Honda 1987 history) is solid. Form factor 'other' — the original was an earlobe probe; modern descendants are wrist/ring/earbud SpO2.",
        prior_art_notes=(
            "Discloses the pulsatile two-wavelength ratiometric method that underlies every "
            "non-invasive SpO2 device: comparing the AC/DC ratios of light absorbance at "
            "(typically) red ~660 nm and infrared ~940 nm through pulsatile tissue to "
            "compute arterial oxygen saturation. Any wearable claim reciting 'a first and "
            "second light source at distinct wavelengths and a photodetector configured to "
            "compute oxygen saturation from a ratio of pulsatile components' reads on this. "
            "§ 102 prior art for the SpO2 principle from 1974; the wrist/ring/earbud "
            "form-factor variants are obvious combinations under [[obviousness-template]]."
        ),
        sources=[
            "Severinghaus JW, Honda Y. J Clin Monit 1987;3(2):135-138.",
            "Nihon Kohden Ear Oximeter OLV-5100 (product, 1975).",
        ],
        cpc_classifications=["A61B 5/14551", "A61B 5/1455", "A61B 5/02416"],
    ),
    E(
        id="asada-mit-wearable-ring-sensor-2003",
        canonical_name="MIT wearable ring sensor (Rhee, Yang, Asada) — finger-ring PPG for ambulatory monitoring",
        aliases=["MIT ring sensor", "Asada ring sensor", "finger-ring photoplethysmographic sensor"],
        corpus="academic",
        first_disclosure_date="2001-07",
        disclosure_citation="Rhee S, Yang B-H, Asada HH. 'Artifact-resistant power-efficient design of finger-ring plethysmographic sensors.' IEEE Transactions on Biomedical Engineering 2001;48(7):795-805 (and Asada HH, Shaltis P, Reisner A, Rhee S, Hutchinson RC. 'Mobile monitoring with wearable photoplethysmographic biosensors.' IEEE Engineering in Medicine and Biology Magazine 2003;22(3):28-40).",
        creator="Sokwoo Rhee / Boo-Ho Yang / Haruhiko Harry Asada (MIT d'Arbeloff Lab)",
        creator_country="US",
        form_factor="ring",
        contact_surface="skin",
        anatomical_target=["finger"],
        sensors=["sensor-ppg", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-spo2-estimation"],
        clinical_endpoints=["heart-rate", "blood-oxygen", "blood-volume-pulse"],
        ip_status="patented",
        notes="MIT holds patents on the ring-sensor design (Rhee/Yang/Asada); specific patent numbers TODO. Disclosure citations (IEEE T-BME 2001, IEEE EMB Mag 2003) fully resolve, so the entry is commons-grade for prior-art purposes; the ip_citations enumeration is a follow-up.",
        prior_art_notes=(
            "Discloses a finger-ring-form-factor wearable PPG sensor with motion-artifact-"
            "resistant optical/mechanical design, low-power operation, on-body processing, "
            "and wireless telemetry of heart rate and SpO2 for ambulatory monitoring — "
            "i.e. the smart-ring physiological monitor, ~14 years before the commercial "
            "smart-ring wave. Directly anticipates ring-form claims combining 'a ring "
            "body', 'a PPG emitter/detector at the inner ring surface', 'motion-artifact "
            "compensation', and 'wireless transmission of derived vitals'. Anchor for the "
            "ring × PPG cross-cut; [[oura-ring-gen1-2015]] and similar products descend "
            "from it."
        ),
        sources=[
            "Rhee S, Yang B-H, Asada HH. IEEE Trans Biomed Eng 2001;48(7):795-805.",
            "Asada HH, et al. IEEE Eng Med Biol Mag 2003;22(3):28-40.",
        ],
        cpc_classifications=["A61B 5/02427", "A61B 5/681", "A61B 5/02416", "A61B 5/6826"],
    ),
    # ---------------- ECG ----------------
    E(
        id="einthoven-1903-string-galvanometer-ecg",
        canonical_name="Einthoven (1903) — the string galvanometer electrocardiogram",
        aliases=["Einthoven ECG", "string galvanometer", "Einthoven's triangle"],
        corpus="academic",
        first_disclosure_date="1903",
        disclosure_citation="Einthoven W. 'Die galvanometrische Registrirung des menschlichen Elektrokardiogramms, zugleich eine Beurtheilung der Anwendung des Capillar-Elektrometers in der Physiologie.' Pflügers Archiv 1903;99:472-480. (Nobel Prize in Physiology or Medicine, 1924.)",
        creator="Willem Einthoven",
        creator_country="NL",
        form_factor="other",
        contact_surface="skin",
        anatomical_target=["limbs", "chest"],
        sensors=["sensor-ecg"],
        clinical_endpoints=["electrocardiogram"],
        ip_status="public-domain",
        notes="Form factor 'other' — a laboratory instrument with limb electrodes, not worn. The disclosure root for every wearable single-/multi-lead ECG device.",
        prior_art_notes=(
            "First practical recording of the human electrocardiogram and the foundational "
            "lead concept (Einthoven's triangle, the limb leads). The disclosure root of "
            "all ECG measurement: any wearable claim reciting 'electrodes positioned to "
            "measure an electrocardiographic signal of the wearer' rests on a technique "
            "public since 1903. § 102 prior art for the ECG principle; the wristworn / "
            "patch / garment single-lead variants are obvious combinations under "
            "[[obviousness-template]]."
        ),
        sources=["Einthoven W. Pflügers Arch 1903;99:472-480."],
        cpc_classifications=["A61B 5/318", "A61B 5/25", "A61B 5/282"],
    ),
    E(
        id="holter-1961-ambulatory-ecg",
        canonical_name="Holter (1961) — continuous ambulatory electrocardiography (the Holter monitor)",
        aliases=["Holter monitor", "ambulatory ECG", "AECG"],
        corpus="academic",
        first_disclosure_date="1961-04-21",
        disclosure_citation="Holter NJ. 'New method for heart studies: continuous electrocardiography of active subjects over long periods is now practical.' Science 1961;134(3486):1214-1220.",
        creator="Norman J. Holter",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["patch"],
        contact_surface="skin",
        anatomical_target=["chest"],
        sensors=["sensor-ecg"],
        algorithms=["algo-arrhythmia-classification"],
        clinical_endpoints=["electrocardiogram"],
        ip_status="public-domain",
        notes="Form factor 'garment'/'patch' — Holter's original was a body-worn recorder on a harness; the modern descendants are adhesive ECG patches (Zio etc.). In scope as wearable continuous ECG.",
        prior_art_notes=(
            "Establishes continuous, ambulatory, body-worn recording of the ECG over hours "
            "to days while the subject is active, for later analysis — the foundational "
            "'wearable continuous ECG monitor'. Any claim reciting 'a body-worn device "
            "configured to continuously record an electrocardiographic signal of the "
            "wearer over an extended period for subsequent arrhythmia analysis' reads on "
            "Holter 1961. Anchor for the ambulatory-ECG / ECG-patch cross-cut; "
            "[[zio-patch-irhythm-2009]] and Apple Watch's ECG history both build on it."
        ),
        sources=["Holter NJ. Science 1961;134(3486):1214-1220."],
        cpc_classifications=["A61B 5/333", "A61B 5/282", "A61B 5/0006"],
    ),
    # ---------------- EEG ----------------
    E(
        id="berger-1929-human-eeg",
        canonical_name="Berger (1929) — first recording of the human electroencephalogram",
        aliases=["Berger rhythm", "Berger EEG", "alpha rhythm"],
        corpus="academic",
        first_disclosure_date="1929",
        disclosure_citation="Berger H. 'Über das Elektrenkephalogramm des Menschen.' Archiv für Psychiatrie und Nervenkrankheiten 1929;87:527-570 (recordings made from 1924).",
        creator="Hans Berger",
        creator_country="DE",
        form_factor="other",
        contact_surface="scalp",
        anatomical_target=["scalp"],
        sensors=["sensor-eeg"],
        clinical_endpoints=["electroencephalogram", "alpha-rhythm"],
        ip_status="public-domain",
        notes="Recordings date to 1924; published 1929. Form factor 'other' — scalp electrodes wired to a galvanometer, not worn. The disclosure root for every wearable EEG device.",
        prior_art_notes=(
            "First demonstration of the human EEG and of the alpha rhythm — the disclosure "
            "root of all scalp EEG measurement. Any wearable claim reciting 'scalp "
            "electrodes positioned to measure an electroencephalographic signal' rests on "
            "a technique public since 1929. § 102 prior art for the EEG principle; the "
            "headband / cap / glasses / earbud EEG variants are obvious combinations under "
            "[[obviousness-template]]."
        ),
        sources=["Berger H. Arch Psychiatr Nervenkr 1929;87:527-570."],
        cpc_classifications=["A61B 5/24", "A61B 5/369", "A61B 5/372"],
    ),
    E(
        id="chb-mit-scalp-eeg-database-2009",
        canonical_name="CHB-MIT Scalp EEG Database (Shoeb, 2009) — benchmark seizure-detection dataset",
        aliases=["CHB-MIT database", "Shoeb seizure dataset"],
        corpus="academic",
        first_disclosure_date="2009-08",
        disclosure_citation="Shoeb AH. 'Application of Machine Learning to Epileptic Seizure Onset Detection and Treatment.' PhD thesis, MIT, 2009 (the CHB-MIT Scalp EEG Database, distributed via PhysioNet, physionet.org/content/chbmit).",
        creator="Ali H. Shoeb (MIT / Boston Children's Hospital)",
        creator_country="US",
        form_factor="other",
        contact_surface="scalp",
        sensors=["sensor-eeg", "sensor-saline-eeg-electrode"],
        algorithms=["algo-seizure-detection"],
        clinical_endpoints=["seizure-onset"],
        ip_status="public-domain",
        notes="Open dataset (PhysioNet, ODC). Form factor 'other' — clinical scalp montage; relevant because it is the public benchmark on which wearable-EEG seizure-detection algorithms (e.g. e-Glass) are trained and reported.",
        prior_art_notes=(
            "Publishes a labelled scalp-EEG corpus and a machine-learning method for "
            "patient-specific seizure-onset detection, establishing the public benchmark "
            "and the patient-calibrated detection paradigm used by subsequent wearable "
            "seizure detectors. Relevant to seizure-detection-wearable claims reciting "
            "'a classifier trained on EEG to detect seizure onset', particularly "
            "'patient-specific' or 'per-subject calibrated' variants — the paradigm and a "
            "reference implementation were public by 2009. Anchor for the EEG × "
            "seizure-detection cross-cut; [[zanetti-aminifar-atienza-eglass-2025]] reports "
            "against it."
        ),
        sources=["Shoeb AH. PhD thesis, MIT, 2009.", "CHB-MIT Scalp EEG Database, PhysioNet."],
        cpc_classifications=["A61B 5/369", "A61B 5/316", "G16H 50/20"],
    ),
    E(
        id="zanetti-aminifar-atienza-eglass-2025",
        canonical_name="e-Glass (Zanetti, Aminifar, Atienza; EPFL, 2025) — wearable EEG eyeglasses",
        aliases=["e-Glass", "EPFL EEG glasses"],
        corpus="academic",
        first_disclosure_date="2025",
        disclosure_citation="Zanetti R, Aminifar A, Atienza D, et al. 'e-Glass: ...' (wearable EEG monitoring in an eyeglasses form factor with edge ML for seizure detection and cognitive-workload monitoring). Scientific Reports 2025. doi:10.1038/s41598-025-29893-4.",
        creator="Renato Zanetti / Amir Aminifar / David Atienza (EPFL ESL)",
        creator_country="CH",
        form_factor="glasses",
        contact_surface="skin",
        anatomical_target=["temple", "around-ear", "TP9", "TP10"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-seizure-detection", "algo-cognitive-workload"],
        clinical_endpoints=["electroencephalogram", "seizure-onset", "cognitive-load"],
        ip_status="unknown",
        notes="ip_status unknown — EPFL may hold patents; to investigate. This is the paper that seeded the Free Wearable Corpus project.",
        prior_art_notes=(
            "Discloses an eyeglasses-form-factor wearable EEG monitor with dry electrodes "
            "at the temples / around the ears (temporal/occipital pickup, validated "
            "against a reference montage at r≈0.93) and on-device machine learning for "
            "two applications — ambulatory seizure detection and cognitive-workload "
            "monitoring. Relevant to AR-glasses / smart-eyewear claims reciting 'EEG "
            "electrodes integrated into an eyeglasses frame' and 'an on-device classifier "
            "operating on the EEG'. Anchor for the glasses × EEG cross-cut. Bounds the "
            "application space: temple/around-ear contact supports seizure, drowsiness, "
            "attention, SSVEP — not frontal ERP or motor-imagery BCI."
        ),
        sources=["Zanetti R, et al. Sci Rep 2025. doi:10.1038/s41598-025-29893-4."],
        cpc_classifications=["A61B 5/24", "A61B 5/369", "G02C 11/00", "G16H 50/20"],
    ),
    # ---------------- SLEEP STAGING ----------------
    E(
        id="aserinsky-kleitman-1953-rem-sleep",
        canonical_name="Aserinsky & Kleitman (1953) — discovery of REM sleep via electrooculography",
        aliases=["REM sleep discovery", "Aserinsky-Kleitman"],
        corpus="academic",
        first_disclosure_date="1953-09-04",
        disclosure_citation="Aserinsky E, Kleitman N. 'Regularly occurring periods of eye motility, and concomitant phenomena, during sleep.' Science 1953;118(3062):273-274.",
        creator="Eugene Aserinsky / Nathaniel Kleitman (University of Chicago)",
        creator_country="US",
        form_factor="other",
        contact_surface="skin",
        anatomical_target=["periorbital", "scalp"],
        sensors=["sensor-eog", "sensor-eeg"],
        algorithms=["algo-sleep-staging"],
        clinical_endpoints=["sleep-stage", "rem-sleep"],
        ip_status="public-domain",
        prior_art_notes=(
            "Establishes that sleep is not homogeneous — that there are recurring periods "
            "of rapid eye movement detectable by electrooculography (with concomitant EEG "
            "changes) — i.e. the existence of distinguishable sleep states detectable from "
            "ocular/cortical electrophysiology. Foundational prior art for any "
            "sleep-staging wearable: the premise that sleep states are detectable from "
            "EOG/EEG signals is public since 1953. Anchor for the sleep-staging cross-cut."
        ),
        sources=["Aserinsky E, Kleitman N. Science 1953;118:273-274."],
        cpc_classifications=["A61B 5/4812", "A61B 5/398", "A61B 5/369"],
    ),
    E(
        id="rechtschaffen-kales-1968-sleep-scoring-manual",
        canonical_name="Rechtschaffen & Kales (1968) — standardized sleep-stage scoring manual",
        aliases=["R&K rules", "Rechtschaffen-Kales manual", "standard sleep scoring"],
        corpus="standards",
        first_disclosure_date="1968",
        disclosure_citation="Rechtschaffen A, Kales A (eds). 'A Manual of Standardized Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects.' Public Health Service / U.S. Government Printing Office / UCLA Brain Information Service, NIH Publication No. 204, 1968.",
        creator="Allan Rechtschaffen / Anthony Kales (eds), for the UCLA Brain Information Service",
        creator_country="US",
        form_factor="other",
        contact_surface="skin",
        sensors=["sensor-eeg", "sensor-eog", "sensor-emg"],
        algorithms=["algo-sleep-staging"],
        clinical_endpoints=["sleep-stage"],
        ip_status="standards",
        notes="Standards/reference document — the canonical sleep-stage scoring rules (superseded operationally by the AASM 2007 manual but still the methodological root). Form factor 'other'.",
        prior_art_notes=(
            "Standardizes the definition of sleep stages and the rules for scoring them "
            "from EEG + EOG + EMG (polysomnography). Any wearable claim reciting "
            "'classifying sleep into stages from electrophysiological/physiological "
            "signals' rests on the staging framework standardized here. Combined with "
            "[[muse-headband-2014]]-type form-factor disclosures, makes wearable "
            "automated sleep-staging an obvious combination under [[obviousness-template]]."
        ),
        sources=["Rechtschaffen A, Kales A (eds). NIH Publication No. 204, 1968."],
        cpc_classifications=["A61B 5/4812", "A61B 5/369", "G16H 50/20"],
    ),
    # ---------------- HRV ----------------
    E(
        id="esc-naspe-1996-hrv-standards",
        canonical_name="Task Force of the ESC and NASPE (1996) — heart rate variability: standards of measurement",
        aliases=["HRV Task Force 1996", "ESC/NASPE HRV standards"],
        corpus="standards",
        first_disclosure_date="1996-03",
        disclosure_citation="Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. 'Heart rate variability: standards of measurement, physiological interpretation, and clinical use.' Circulation 1996;93(5):1043-1065 (also European Heart Journal 1996;17:354-381).",
        creator="Task Force of the ESC and NASPE",
        creator_country="EU",
        form_factor="other",
        sensors=["sensor-ecg", "sensor-ppg"],
        algorithms=["algo-hrv", "algo-stress-index"],
        clinical_endpoints=["heart-rate-variability"],
        ip_status="standards",
        notes="Standards document. Form factor 'other'.",
        prior_art_notes=(
            "Standardizes the time-domain (SDNN, RMSSD, pNN50, ...) and frequency-domain "
            "(VLF/LF/HF, LF/HF ratio) measures of heart rate variability, their "
            "computation from an interbeat-interval series, and their physiological "
            "interpretation. Any wearable claim reciting 'computing a heart-rate-"
            "variability metric (e.g. RMSSD, LF/HF) from a sequence of interbeat "
            "intervals' rests on metrics standardized here. Anchor for the HRV cross-cut; "
            "applicable whether the interbeat intervals come from ECG or PPG."
        ),
        sources=["Task Force ESC/NASPE. Circulation 1996;93:1043-1065."],
        cpc_classifications=["A61B 5/02405", "A61B 5/352", "A61B 5/16"],
    ),
    # ---------------- GLUCOSE / CGM ----------------
    E(
        id="clark-lyons-1962-enzyme-electrode",
        canonical_name="Clark & Lyons (1962) — the enzyme electrode (basis of the amperometric glucose biosensor)",
        aliases=["Clark electrode (enzyme)", "first glucose biosensor concept"],
        corpus="academic",
        first_disclosure_date="1962",
        disclosure_citation="Clark LC Jr, Lyons C. 'Electrode systems for continuous monitoring in cardiovascular surgery.' Annals of the New York Academy of Sciences 1962;102(1):29-45.",
        creator="Leland C. Clark Jr. / Champ Lyons",
        creator_country="US",
        form_factor="other",
        contact_surface="vascular",
        sensors=["sensor-glucose-cgm"],
        clinical_endpoints=["glucose"],
        ip_status="public-domain",
        prior_art_notes=(
            "Proposes coupling an enzyme (glucose oxidase) to an oxygen electrode so that "
            "the electrode current reports glucose concentration — the founding concept of "
            "the amperometric enzyme biosensor and hence of every electrochemical "
            "continuous glucose monitor. Any CGM claim reciting 'an enzyme electrode "
            "configured to generate a current dependent on glucose concentration' rests on "
            "a concept public since 1962. § 102 prior art for the electrochemical-glucose-"
            "sensing principle."
        ),
        sources=["Clark LC Jr, Lyons C. Ann N Y Acad Sci 1962;102:29-45."],
        cpc_classifications=["A61B 5/14532", "C12Q 1/006", "G01N 27/327"],
    ),
    E(
        id="updike-hicks-1967-enzyme-electrode",
        canonical_name="Updike & Hicks (1967) — the practical glucose enzyme electrode",
        aliases=["Updike-Hicks enzyme electrode"],
        corpus="academic",
        first_disclosure_date="1967-06-03",
        disclosure_citation="Updike SJ, Hicks GP. 'The enzyme electrode.' Nature 1967;214(5092):986-988.",
        creator="Stuart J. Updike / George P. Hicks",
        creator_country="US",
        form_factor="other",
        sensors=["sensor-glucose-cgm"],
        clinical_endpoints=["glucose"],
        ip_status="public-domain",
        prior_art_notes=(
            "Reduces Clark & Lyons's concept to a working device — an immobilized-enzyme "
            "membrane on an electrode giving a glucose-dependent signal — the practical "
            "ancestor of the implantable/subcutaneous glucose sensor. Prior art for CGM "
            "claims reciting 'a membrane-immobilized glucose oxidase layer on an "
            "electrode'. Combined with [[shichiri-1982-wearable-needle-glucose-sensor]] "
            "it establishes both the chemistry and the wearable form."
        ),
        sources=["Updike SJ, Hicks GP. Nature 1967;214:986-988."],
        cpc_classifications=["A61B 5/14532", "C12Q 1/006", "G01N 27/327"],
    ),
    E(
        id="shichiri-1982-wearable-needle-glucose-sensor",
        canonical_name="Shichiri et al. (1982) — wearable artificial pancreas with needle-type subcutaneous glucose sensor",
        aliases=["Shichiri needle-type glucose sensor", "first wearable CGM"],
        corpus="academic",
        first_disclosure_date="1982-11-20",
        disclosure_citation="Shichiri M, Kawamori R, Yamasaki Y, Hakui N, Abe H. 'Wearable artificial endocrine pancreas with needle-type glucose sensor.' The Lancet 1982;320(8308):1129-1131.",
        creator="Motoaki Shichiri et al. (Osaka University)",
        creator_country="JP",
        form_factor="patch",
        form_factor_tags=["implantable"],
        contact_surface="sub-dermal",
        anatomical_target=["subcutaneous-tissue", "abdomen"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-cgm-readout"],
        clinical_endpoints=["interstitial-glucose"],
        ip_status="unknown",
        notes="ip_status unknown — possible patents to investigate. Form factor 'patch'/'implantable' — a body-worn unit with a subcutaneously inserted needle-type sensor; the direct ancestor of Medtronic/Dexcom/Abbott CGM hardware.",
        prior_art_notes=(
            "Discloses a body-worn device with a needle-type electrochemical glucose sensor "
            "inserted into subcutaneous tissue, continuously transducing interstitial "
            "glucose and (in the closed-loop variant) driving insulin delivery — i.e. the "
            "wearable continuous glucose monitor, ~24 years before commercial CGM. Directly "
            "anticipates CGM claims combining 'a wearable housing', 'a percutaneous "
            "needle-type enzyme-electrode sensor in subcutaneous tissue', and 'continuous "
            "transduction of interstitial glucose'. Anchor for the patch × glucose-CGM "
            "cross-cut; Medtronic MiniMed (1999), Dexcom (2006), Abbott Libre (2014) "
            "all descend from this form."
        ),
        sources=["Shichiri M, et al. Lancet 1982;320:1129-1131."],
        cpc_classifications=["A61B 5/14532", "A61B 5/1486", "A61M 5/142"],
    ),
    # ---------------- FALL DETECTION ----------------
    E(
        id="williams-1998-automatic-fall-detector",
        canonical_name="Williams et al. (1998) — accelerometer-based automatic fall and activity monitor for telecare",
        aliases=["smart fall monitor 1998", "telecare fall detector"],
        corpus="academic",
        first_disclosure_date="1998-10",
        disclosure_citation="Williams G, Doughty K, Cameron K, Bradley DA. 'A smart fall and activity monitor for telecare applications.' Proceedings of the 20th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBS), Hong Kong, 1998, pp. 1151-1154.",
        creator="G. Williams / K. Doughty / K. Cameron / D.A. Bradley",
        creator_country="GB",
        form_factor="belt",
        form_factor_tags=["pendant"],
        contact_surface="skin",
        anatomical_target=["waist", "trunk"],
        sensors=["sensor-accelerometer", "sensor-piezoelectric"],
        algorithms=["algo-fall-detection", "algo-activity-classification"],
        clinical_endpoints=["fall-event"],
        ip_status="unknown",
        notes="ip_status unknown — patents possible. An early disclosure of automatic (not button-press) fall detection from a body-worn inertial/impact sensor.",
        prior_art_notes=(
            "Discloses a body-worn (waist/trunk) device that automatically detects a fall "
            "from accelerometer/impact signals — distinguishing falls from normal activity "
            "— and raises a telecare alarm, without requiring the wearer to press a button. "
            "Anticipates automatic-fall-detection wearable claims combining 'a body-worn "
            "inertial sensor', 'a classifier distinguishing a fall from activities of "
            "daily living', and 'an automatic alert on detection'. Anchor for the "
            "fall-detection cross-cut; combined with watch/pendant form-factor disclosures, "
            "makes wristworn/pendant automatic fall detection obvious under "
            "[[obviousness-template]]."
        ),
        sources=["Williams G, Doughty K, Cameron K, Bradley DA. Proc 20th IEEE EMBS, 1998."],
        cpc_classifications=["A61B 5/1117", "G08B 21/04", "A61B 5/0022"],
    ),
    # ---------------- BCI ----------------
    E(
        id="wolpaw-2002-bci-review",
        canonical_name="Wolpaw et al. (2002) — 'Brain-computer interfaces for communication and control'",
        aliases=["Wolpaw BCI review", "BCI 2002 review"],
        corpus="academic",
        first_disclosure_date="2002-06",
        disclosure_citation="Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM. 'Brain-computer interfaces for communication and control.' Clinical Neurophysiology 2002;113(6):767-791.",
        creator="Jonathan R. Wolpaw et al.",
        creator_country="US",
        form_factor="other",
        contact_surface="scalp",
        sensors=["sensor-eeg"],
        algorithms=["algo-bci-p300", "algo-bci-ssvep", "algo-bci-motor-imagery", "algo-erp-classification"],
        clinical_endpoints=["bci-control-signal"],
        ip_status="public-domain",
        prior_art_notes=(
            "Canonical review establishing, as of 2002, the major non-invasive EEG-based "
            "BCI paradigms (sensorimotor rhythms / motor imagery, P300 evoked potentials, "
            "SSVEP, slow cortical potentials) and the signal-processing pipeline for "
            "translating EEG into control output. Prior art for wearable-BCI claims "
            "reciting any of these paradigms with scalp EEG: the paradigms and methods "
            "were published and enabled by 2002. Anchor for the BCI algorithm cross-cuts."
        ),
        sources=["Wolpaw JR, et al. Clin Neurophysiol 2002;113(6):767-791."],
        cpc_classifications=["A61B 5/372", "G06F 3/015", "A61B 5/378"],
    ),
    # ---------------- OPEN HARDWARE ----------------
    E(
        id="openbci-cyton-2014",
        canonical_name="OpenBCI Cyton — open-source 8-channel biosignal (EEG/EMG/ECG) acquisition board and 3D-printed headset",
        aliases=["OpenBCI", "OpenBCI Cyton", "Ultracortex"],
        corpus="open",
        first_disclosure_date="2014-01-22",
        disclosure_citation="OpenBCI (Joel Murphy, Conor Russomanno). 'OpenBCI: An Open Source Brain-Computer Interface For Makers.' Kickstarter campaign launched 22 January 2014; hardware designs and firmware released open source at github.com/OpenBCI (Cyton board, Ganglion board, Ultracortex Mark IV 3D-printed headset).",
        creator="Joel Murphy / Conor Russomanno (OpenBCI)",
        creator_country="US",
        form_factor="cap",
        form_factor_tags=["headband"],
        contact_surface="scalp",
        anatomical_target=["scalp"],
        sensors=["sensor-saline-eeg-electrode", "sensor-dry-eeg-electrode", "sensor-emg", "sensor-ecg"],
        algorithms=["algo-bci-p300", "algo-bci-ssvep", "algo-bci-motor-imagery"],
        clinical_endpoints=["electroencephalogram", "electromyogram", "electrocardiogram"],
        ip_status="open-permissive",
        notes="Hardware released under permissive/open-hardware terms; firmware MIT-licensed; designs on GitHub. Already-public, already-unencumbered prior art.",
        prior_art_notes=(
            "An openly-published, openly-licensed wearable biosignal acquisition system: "
            "a multi-channel ADS1299-based board, electrodes, and a 3D-printed head-worn "
            "frame for EEG/EMG/ECG, with reference firmware and BCI demonstrations. As "
            "open-hardware prior art it is unencumbered: any claim reciting a "
            "multi-channel head-worn biopotential acquisition device with the features "
            "published here (since 2014) reads on OpenBCI. Anchors the `open` bucket for "
            "biosignal wearables; relevant to headband/cap EEG and to EMG/ECG wearable "
            "claims."
        ),
        sources=[
            "OpenBCI Kickstarter, January 2014.",
            "github.com/OpenBCI (hardware and firmware repositories).",
        ],
        cpc_classifications=["A61B 5/24", "A61B 5/389", "A61B 5/282", "A61B 5/256"],
    ),
    # ---------------- STANDARDS ----------------
    E(
        id="bluetooth-sig-heart-rate-profile-2011",
        canonical_name="Bluetooth SIG — Heart Rate Profile / Heart Rate Service (2011)",
        aliases=["Bluetooth Heart Rate Profile", "HRP", "Heart Rate Service 0x180D"],
        corpus="standards",
        first_disclosure_date="2011-07-12",
        disclosure_citation="Bluetooth SIG. 'Heart Rate Profile' specification v1.0 and 'Heart Rate Service' (GATT service UUID 0x180D, characteristics: Heart Rate Measurement 0x2A37, Body Sensor Location 0x2A38, Heart Rate Control Point 0x2A39), adopted 12 July 2011; available at bluetooth.com/specifications.",
        creator="Bluetooth Special Interest Group",
        creator_country="US",
        form_factor="other",
        sensors=["sensor-ppg", "sensor-ecg"],
        algorithms=["algo-hr"],
        clinical_endpoints=["heart-rate"],
        ip_status="standards",
        connectivity="ble",
        notes="Standards document. Form factor 'other' — but the profile's stated use is body-worn heart-rate sensors (chest straps, wrist devices).",
        prior_art_notes=(
            "A publicly-adopted standard defining how a body-worn heart-rate sensor "
            "advertises, structures, and transmits heart-rate measurements (including "
            "energy expended and RR-interval data) over Bluetooth Low Energy to a "
            "collector, with a defined sensor-location enumeration including wrist, finger, "
            "ear, chest, foot, hand. Prior art for wearable-HR claims reciting 'a "
            "BLE-advertised heart-rate measurement characteristic', 'transmission of RR "
            "intervals from a body-worn sensor', or a 'body sensor location' field — these "
            "were standardized and public from 2011. Relevant to PPG and ECG HR wearables "
            "alike."
        ),
        sources=["Bluetooth SIG. Heart Rate Profile v1.0; Heart Rate Service. Adopted 2011."],
        cpc_classifications=["A61B 5/0006", "A61B 5/024", "H04W 4/80"],
    ),
    E(
        id="ieee-11073-10406-basic-ecg-2011",
        canonical_name="IEEE Std 11073-10406-2011 — personal health device communication: basic electrocardiograph (1- to 3-lead ECG)",
        aliases=["IEEE 11073-10406", "11073 basic ECG device specialization"],
        corpus="standards",
        first_disclosure_date="2011-12-30",
        disclosure_citation="IEEE Std 11073-10406-2011. 'Health informatics — Personal health device communication — Part 10406: Device specialization — Basic electrocardiograph (ECG) (1- to 3-lead ECG).' IEEE, 2011.",
        creator="IEEE / ISO/IEEE 11073 Personal Health Devices Working Group",
        creator_country="US",
        form_factor="other",
        sensors=["sensor-ecg"],
        algorithms=["algo-hr", "algo-arrhythmia-classification"],
        clinical_endpoints=["electrocardiogram", "heart-rate"],
        ip_status="standards",
        notes="Standards document. Form factor 'other' — defines the data model for a personal (consumer/home) 1-to-3-lead ECG device.",
        prior_art_notes=(
            "A publicly-adopted standard defining the device model and data exchange for a "
            "personal/consumer 1-to-3-lead electrocardiograph — including reporting of the "
            "ECG waveform, derived heart rate, and rhythm/event annotations from a "
            "body-worn or handheld single-lead ECG device. Prior art for "
            "consumer-single-lead-ECG-wearable claims reciting the device model, lead "
            "configuration, or data fields standardized here (public from 2011, predating "
            "the Apple Watch / AliveCor consumer-ECG patent wave's later filings)."
        ),
        sources=["IEEE Std 11073-10406-2011. IEEE, 2011."],
        cpc_classifications=["A61B 5/318", "A61B 5/333", "G16H 40/63"],
    ),
    E(
        id="iso-80601-2-61-pulse-oximeter-equipment-2011",
        canonical_name="ISO 80601-2-61 — particular requirements for basic safety and essential performance of pulse oximeter equipment (2011/2017)",
        aliases=["ISO 80601-2-61", "pulse oximeter equipment standard"],
        corpus="standards",
        first_disclosure_date="2011-08-15",
        disclosure_citation="ISO 80601-2-61:2011 (revised 2017). 'Medical electrical equipment — Part 2-61: Particular requirements for basic safety and essential performance of pulse oximeter equipment.' ISO, 2011.",
        creator="ISO/IEC (TC 121/SC 3 and IEC SC 62D)",
        creator_country="CH",
        form_factor="other",
        sensors=["sensor-spo2", "sensor-ppg", "sensor-multi-wavelength-ppg"],
        algorithms=["algo-spo2-estimation"],
        clinical_endpoints=["blood-oxygen", "pulse-rate"],
        ip_status="standards",
        notes="Standards document. Defines what pulse oximeter equipment is and how its SpO2 accuracy is specified and tested; applies to wearable pulse oximeters.",
        prior_art_notes=(
            "Publicly-adopted standard defining pulse oximeter equipment (a device "
            "estimating SpO2 and pulse rate from light at two or more wavelengths through "
            "perfused tissue) and the accuracy/validation requirements for it. Prior art "
            "for wearable-SpO2 claims to the extent they recite the multi-wavelength "
            "pulsatile method or the SpO2-and-pulse-rate output described here; the "
            "equipment definition and method have been a published standard since 2011 "
            "(building on the [[aoyagi-1974-two-wavelength-pulse-oximetry]] principle)."
        ),
        sources=["ISO 80601-2-61:2011 (and :2017). ISO."],
        cpc_classifications=["A61B 5/1455", "A61B 5/14551", "A61B 5/02416"],
    ),
    E(
        id="continua-design-guidelines-2007",
        canonical_name="Continua Health Alliance — Design Guidelines (first edition, 2007)",
        aliases=["Continua Design Guidelines", "Continua interoperability guidelines", "PCHA guidelines"],
        corpus="standards",
        first_disclosure_date="2007",
        disclosure_citation="Continua Health Alliance (later Personal Connected Health Alliance). 'Continua Design Guidelines' (first edition published 2007; subsequently maintained, ITU-T H.810 series). Specifies end-to-end interoperability for personal connected health devices, profiling IEEE 11073, Bluetooth, USB, ZigBee, HL7/IHE.",
        creator="Continua Health Alliance",
        creator_country="US",
        form_factor="other",
        sensors=["sensor-ppg", "sensor-ecg", "sensor-glucose-cgm", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-step-count", "algo-glucose-cgm-readout"],
        ip_status="standards",
        notes="Standards/profile document — the umbrella interoperability framework for personal connected health (wearable) devices. Form factor 'other'.",
        prior_art_notes=(
            "Publicly-published end-to-end interoperability framework for personal "
            "connected health devices — defining how a body-worn sensor (weight scale, "
            "blood-pressure cuff, glucose meter, pulse oximeter, activity monitor, ECG, "
            "etc.) connects to an application hub and onward to health-record systems, "
            "profiling the underlying transport and data standards. Prior art for "
            "connected-wearable-system claims reciting the architecture, the "
            "device-to-hub-to-record data flow, or the standard profiles assembled here, "
            "public from 2007."
        ),
        sources=["Continua Health Alliance. Design Guidelines, 2007 (and successors; ITU-T H.810)."],
        cpc_classifications=["G16H 40/67", "G16H 40/63", "H04L 67/12"],
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
    print(f"  real foundations r1: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
