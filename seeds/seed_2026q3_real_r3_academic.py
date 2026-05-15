#!/usr/bin/env python3
"""seed_2026q3_real_r3_academic.py — more academic foundations.

Reflectance pulse oximetry; cuffless blood pressure (volume-clamp / PTT);
epidermal electronics and wearable electrochemical (sweat) sensors;
wrist-actigraphy sleep scoring; surface-EMG gesture control; around-ear and
in-ear EEG; wearable-health-systems surveys.

Run from repo root:  python3 seeds/seed_2026q3_real_r3_academic.py
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
    kw.setdefault("corpus", "academic")
    kw.setdefault("ip_status", "public-domain")
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    # ---------------- PULSE OXIMETRY (REFLECTANCE) ----------------
    E(
        id="mendelson-ochs-1988-reflectance-pulse-oximetry",
        canonical_name="Mendelson & Ochs (1988) — reflectance-mode pulse oximetry / skin-reflectance PPG",
        aliases=["reflectance pulse oximetry", "reflectance PPG SpO2"],
        first_disclosure_date="1988-10",
        disclosure_citation="Mendelson Y, Ochs BD. 'Noninvasive pulse oximetry utilizing skin reflectance photoplethysmography.' IEEE Transactions on Biomedical Engineering 1988;35(10):798-805.",
        creator="Yitzhak Mendelson / Burt D. Ochs",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["patch", "watch"],
        contact_surface="skin",
        sensors=["sensor-ppg", "sensor-spo2", "sensor-multi-wavelength-ppg"],
        algorithms=["algo-spo2-estimation", "algo-hr"],
        clinical_endpoints=["blood-oxygen", "heart-rate"],
        prior_art_notes=(
            "Establishes pulse oximetry by reflectance (light source and detector on the "
            "same side of the tissue) rather than transmission — the geometry every "
            "wrist, forehead, ring, chest, and earbud PPG/SpO2 wearable uses, since those "
            "sites cannot be transilluminated. Any wearable-SpO2 claim reciting "
            "'a reflectance photoplethysmography sensor' or 'a light source and "
            "photodetector arranged on a common surface against the skin' reads on "
            "Mendelson & Ochs 1988. Anchor for the reflectance-PPG/SpO2 cross-cut on "
            "non-fingertip sites."
        ),
        sources=["Mendelson Y, Ochs BD. IEEE Trans Biomed Eng 1988;35(10):798-805."],
        cpc_classifications=["A61B 5/14552", "A61B 5/02427", "A61B 5/1455"],
    ),
    E(
        id="webster-1997-design-of-pulse-oximeters",
        canonical_name="Webster (ed.) (1997) — 'Design of Pulse Oximeters'",
        aliases=["Design of Pulse Oximeters"],
        first_disclosure_date="1997",
        disclosure_citation="Webster JG (ed). 'Design of Pulse Oximeters.' Series in Medical Physics and Biomedical Engineering, IOP Publishing / Institute of Physics, 1997. ISBN 0-7503-0467-7.",
        creator="John G. Webster (ed.)",
        creator_country="US",
        form_factor="other",
        sensors=["sensor-spo2", "sensor-ppg"],
        algorithms=["algo-spo2-estimation", "algo-hr"],
        clinical_endpoints=["blood-oxygen", "heart-rate"],
        prior_art_notes=(
            "The standard engineering reference on pulse oximeter design as of 1997 — LED "
            "selection and drive, photodiode front-ends, the ratio-of-ratios calibration, "
            "motion-artifact handling, low-perfusion behavior, calibration-curve "
            "construction. Prior art for wearable-SpO2 claims to the extent they recite "
            "implementation details (wavelength choice, AC/DC ratio computation, "
            "calibration-curve mapping, artifact rejection) covered here; these were "
            "textbook-level public knowledge by 1997."
        ),
        sources=["Webster JG (ed). Design of Pulse Oximeters. IOP Publishing, 1997."],
        cpc_classifications=["A61B 5/1455", "A61B 5/14551", "A61B 5/02416"],
    ),
    # ---------------- CUFFLESS BLOOD PRESSURE ----------------
    E(
        id="penaz-1973-volume-clamp-finger-bp",
        canonical_name="Peñáz (1973) — the volume-clamp (vascular unloading) method of continuous finger blood pressure",
        aliases=["Peñáz method", "volume clamp", "vascular unloading", "Finapres principle"],
        first_disclosure_date="1973",
        disclosure_citation="Peñáz J. 'Photoelectric measurement of blood pressure, volume and flow in the finger.' Digest of the 10th International Conference on Medical and Biological Engineering, Dresden, 1973, p. 104. (Basis of the Finapres / volume-clamp continuous BP monitors.)",
        creator="Jan Peñáz",
        creator_country="CZ",
        form_factor="other",
        form_factor_tags=["ring"],
        contact_surface="skin",
        anatomical_target=["finger"],
        sensors=["sensor-ppg", "sensor-cuffless-bp-volume-clamp", "sensor-pressure-skin"],
        algorithms=["algo-pwv-bp-estimation"],
        clinical_endpoints=["blood-pressure"],
        prior_art_notes=(
            "Discloses the volume-clamp / vascular-unloading method: a finger cuff "
            "servo-controlled by a photoplethysmographic feedback loop to hold the "
            "arterial volume constant, so the applied counter-pressure tracks the arterial "
            "pressure waveform continuously and non-invasively. Any cuffless/continuous-BP "
            "wearable claim reciting 'a photoplethysmographic feedback loop controlling an "
            "applied pressure to maintain constant vascular volume' reads on Peñáz 1973. "
            "Anchor for the volume-clamp cuffless-BP cross-cut (the finger/ring form-factor "
            "variants are obvious combinations under [[obviousness-template]])."
        ),
        sources=["Peñáz J. Dig 10th Int Conf Med Biol Eng, Dresden, 1973, p.104."],
        cpc_classifications=["A61B 5/02233", "A61B 5/0225", "A61B 5/021"],
    ),
    E(
        id="geddes-1981-pulse-transit-time-bp",
        canonical_name="Geddes et al. (1981) — pulse transit time as an indicator of arterial blood pressure",
        aliases=["pulse transit time blood pressure", "PTT-BP", "PWV-BP"],
        first_disclosure_date="1981-01",
        disclosure_citation="Geddes LA, Voelz MH, Babbs CF, Bourland JD, Tacker WA. 'Pulse transit time as an indicator of arterial blood pressure.' Psychophysiology 1981;18(1):71-74.",
        creator="Leslie A. Geddes et al. (Purdue)",
        creator_country="US",
        form_factor="other",
        contact_surface="skin",
        sensors=["sensor-ecg", "sensor-ppg", "sensor-cuffless-bp-ptt"],
        algorithms=["algo-pwv-bp-estimation"],
        clinical_endpoints=["blood-pressure"],
        prior_art_notes=(
            "Establishes that pulse transit time — the delay between a proximal timing "
            "reference (e.g. the ECG R-wave) and the arrival of the pulse at a distal site "
            "(e.g. a finger PPG) — varies inversely with arterial blood pressure, and can "
            "therefore be used to estimate BP without a cuff. Any cuffless-BP wearable "
            "claim reciting 'estimating blood pressure from a pulse transit time (or pulse "
            "arrival time / pulse wave velocity) derived from two physiological signals' "
            "reads on Geddes 1981. Earliest anchor for the PTT-cuffless-BP cross-cut; "
            "[[mukkamala-2015-ptt-cuffless-bp-review]] is the modern survey."
        ),
        sources=["Geddes LA, et al. Psychophysiology 1981;18(1):71-74."],
        cpc_classifications=["A61B 5/02125", "A61B 5/02108", "A61B 5/021"],
    ),
    E(
        id="mukkamala-2015-ptt-cuffless-bp-review",
        canonical_name="Mukkamala et al. (2015) — 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice'",
        aliases=["Mukkamala PTT-BP review", "ubiquitous blood pressure monitoring review"],
        first_disclosure_date="2015-08",
        disclosure_citation="Mukkamala R, Hahn J-O, Inan OT, Mestha LK, Kim C-S, Töreyin H, Kyal S. 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice.' IEEE Transactions on Biomedical Engineering 2015;62(8):1879-1901.",
        creator="Ramakrishna Mukkamala et al.",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["watch", "bracelet", "ring", "patch"],
        contact_surface="skin",
        sensors=["sensor-ecg", "sensor-ppg", "sensor-cuffless-bp-ptt", "sensor-cuffless-bp-tonometry"],
        algorithms=["algo-pwv-bp-estimation"],
        clinical_endpoints=["blood-pressure", "arterial-stiffness"],
        prior_art_notes=(
            "Canonical 2015 review of cuffless blood-pressure estimation by pulse transit "
            "time / pulse arrival time / pulse wave velocity: the physiological models, "
            "the practical sensor configurations (ECG+PPG, dual PPG, ballistocardiogram+"
            "PPG), the calibration strategies, and the accuracy limitations. Prior art for "
            "cuffless-BP wearable claims reciting any of the configurations or calibration "
            "approaches surveyed here — they were collected, modeled, and published by "
            "2015. Combined with watch/ring/patch form-factor disclosures, makes wearable "
            "PTT-based BP an obvious combination under [[obviousness-template]]."
        ),
        sources=["Mukkamala R, et al. IEEE Trans Biomed Eng 2015;62(8):1879-1901."],
        cpc_classifications=["A61B 5/02125", "A61B 5/021", "A61B 5/0285"],
    ),
    # ---------------- EPIDERMAL ELECTRONICS & WEARABLE ELECTROCHEMICAL SENSORS ----------------
    E(
        id="kim-rogers-2011-epidermal-electronics",
        canonical_name="Kim et al. (Rogers group) (2011) — 'Epidermal Electronics' (electronic-tattoo skin-mounted devices)",
        aliases=["epidermal electronics", "electronic tattoo", "EES"],
        first_disclosure_date="2011-08-12",
        disclosure_citation="Kim D-H, Lu N, Ma R, Kim Y-S, Kim R-H, Wang S, et al. (Rogers JA). 'Epidermal Electronics.' Science 2011;333(6044):838-843.",
        creator="Dae-Hyeong Kim et al. / John A. Rogers group (Illinois)",
        creator_country="US",
        form_factor="tattoo-electronic",
        contact_surface="skin",
        anatomical_target=["skin"],
        sensors=["sensor-ecg", "sensor-emg", "sensor-eeg", "sensor-skin-temperature", "sensor-strain-gauge"],
        clinical_endpoints=["electrocardiogram", "electromyogram", "electroencephalogram", "skin-temperature", "skin-strain"],
        prior_art_notes=(
            "Discloses ultrathin, skin-conformal ('epidermal') electronic devices laminated "
            "directly onto the skin like a temporary tattoo, integrating electrodes, "
            "sensors (ECG, EMG, EEG, temperature, strain), interconnects, and even "
            "wireless components, mechanically matched to the skin so they move with it. "
            "The foundational disclosure of the 'electronic skin / electronic tattoo' "
            "form factor. Any claim reciting 'an ultrathin stretchable electronic device "
            "conformally mounted on the skin' for physiological sensing reads on Kim/Rogers "
            "2011. Anchor for the tattoo-electronic form-factor cross-cut on the real side."
        ),
        sources=["Kim D-H, et al. Science 2011;333(6044):838-843."],
        cpc_classifications=["A61B 5/259", "A61B 5/263", "A61B 5/6833", "H05K 1/028"],
    ),
    E(
        id="koh-rogers-2016-soft-microfluidic-sweat-device",
        canonical_name="Koh et al. (Rogers group) (2016) — soft wearable microfluidic device for sweat capture, storage, and colorimetric sensing",
        aliases=["epidermal microfluidic sweat patch", "sweat sticker", "Rogers sweat microfluidics"],
        first_disclosure_date="2016-11-23",
        disclosure_citation="Koh A, Kang D, Xue Y, Lee S, Pielak RM, Kim J, et al. (Rogers JA). 'A soft, wearable microfluidic device for the capture, storage, and colorimetric sensing of sweat.' Science Translational Medicine 2016;8(366):366ra165.",
        creator="Ahyeon Koh et al. / John A. Rogers group (Northwestern)",
        creator_country="US",
        form_factor="patch",
        form_factor_tags=["tattoo-electronic"],
        contact_surface="skin",
        anatomical_target=["skin", "forearm", "back"],
        sensors=["sensor-microfluidic-sweat-collection", "sensor-sweat-rate", "sensor-ph", "sensor-lactate", "sensor-electrolyte", "sensor-glucose-cgm"],
        algorithms=["algo-hydration-status", "algo-electrolyte-trend"],
        clinical_endpoints=["sweat-rate", "sweat-pH", "sweat-lactate", "sweat-chloride", "sweat-glucose"],
        prior_art_notes=(
            "Discloses a soft, skin-mounted microfluidic 'sticker' that wicks sweat from "
            "the skin into a network of microchannels and reservoirs, measures sweat rate "
            "and total sweat loss, and performs colorimetric assays (pH, chloride, "
            "lactate, glucose) read out by eye or smartphone camera. Any wearable claim "
            "reciting 'a skin-mounted patch with microfluidic channels collecting "
            "perspiration' combined with 'rate measurement' and/or 'colorimetric or "
            "electrochemical analysis of constituents' reads on Koh/Rogers 2016. Anchor "
            "for the patch × microfluidic-sweat-collection cross-cut on the real side; "
            "[[dune-stillsuit]] (1965) is the fictional antecedent."
        ),
        sources=["Koh A, et al. Sci Transl Med 2016;8(366):366ra165."],
        cpc_classifications=["A61B 10/0064", "A61B 5/4266", "B01L 3/502707", "A61B 5/1486"],
    ),
    E(
        id="gao-javey-2016-wearable-sweat-sensor-array",
        canonical_name="Gao et al. (Javey group) (2016) — fully integrated wearable sensor array for multiplexed in-situ perspiration analysis",
        aliases=["Berkeley sweat sensor", "multiplexed sweat sensor wristband", "Javey sweatband"],
        first_disclosure_date="2016-01-28",
        disclosure_citation="Gao W, Emaminejad S, Nyein HYY, Challa S, Chen K, Peck A, et al. (Javey A). 'Fully integrated wearable sensor arrays for multiplexed in situ perspiration analysis.' Nature 2016;529(7587):509-514.",
        creator="Wei Gao et al. / Ali Javey group (UC Berkeley)",
        creator_country="US",
        form_factor="headband",
        form_factor_tags=["bracelet", "patch"],
        contact_surface="skin",
        anatomical_target=["forehead", "wrist", "skin"],
        sensors=["sensor-lactate", "sensor-glucose-cgm", "sensor-electrolyte", "sensor-ph", "sensor-skin-temperature", "sensor-microfluidic-sweat-collection"],
        algorithms=["algo-electrolyte-trend", "algo-hydration-status"],
        clinical_endpoints=["sweat-glucose", "sweat-lactate", "sweat-sodium", "sweat-potassium", "skin-temperature"],
        prior_art_notes=(
            "Discloses a fully integrated wearable (wristband / headband) with an array of "
            "electrochemical sensors measuring multiple sweat analytes simultaneously "
            "(glucose, lactate, Na+, K+) plus skin temperature for real-time signal "
            "compensation, with on-board signal conditioning, microcontroller, and "
            "wireless transmission to a phone — i.e. a complete in-situ sweat biochemistry "
            "monitor. Any wearable claim reciting 'a band-form device with an array of two "
            "or more electrochemical sweat-analyte sensors plus a temperature sensor for "
            "compensation, with integrated electronics and wireless output' reads on "
            "Gao/Javey 2016. Anchor for the sweat-electrochemical-sensing cross-cuts on "
            "the real side; [[bandodkar-wang-2014-wearable-electrochemical-sensors-review]] "
            "is the contemporaneous review."
        ),
        sources=["Gao W, et al. Nature 2016;529(7587):509-514."],
        cpc_classifications=["A61B 5/14546", "A61B 5/1468", "A61B 5/4266", "G01N 27/327"],
    ),
    E(
        id="bandodkar-wang-2014-wearable-electrochemical-sensors-review",
        canonical_name="Bandodkar & Wang (2014) — 'Non-invasive wearable electrochemical sensors: a review'",
        aliases=["wearable electrochemical sensors review", "Bandodkar-Wang review"],
        first_disclosure_date="2014-07",
        disclosure_citation="Bandodkar AJ, Wang J. 'Non-invasive wearable electrochemical sensors: a review.' Trends in Biotechnology 2014;32(7):363-371.",
        creator="Amay J. Bandodkar / Joseph Wang (UC San Diego)",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["patch", "tattoo-electronic", "garment", "contact-lens", "dental"],
        contact_surface="skin",
        sensors=["sensor-lactate", "sensor-electrolyte", "sensor-ph", "sensor-glucose-cgm", "sensor-alcohol-transdermal", "sensor-uric-acid", "sensor-cortisol"],
        algorithms=["algo-electrolyte-trend", "algo-hydration-status"],
        clinical_endpoints=["sweat-analytes", "saliva-analytes", "tear-analytes", "interstitial-glucose"],
        prior_art_notes=(
            "Surveys, as of 2014, wearable non-invasive electrochemical biosensors across "
            "body fluids and form factors — temporary-tattoo electrodes on the skin "
            "(sweat lactate, Na+, ammonium, pH), textile-integrated sensors, mouthguard "
            "(saliva) sensors, contact-lens (tear glucose) sensors, and the transdermal/"
            "interstitial route — including the sampling, transduction, and on-body "
            "electronics issues. Prior art for wearable-electrochemical-sensing claims "
            "reciting any of the analyte/form-factor combinations collected here; the "
            "approaches were published by 2014. General anchor for the electrochemical "
            "wearable cross-cuts."
        ),
        sources=["Bandodkar AJ, Wang J. Trends Biotechnol 2014;32(7):363-371."],
        cpc_classifications=["A61B 5/1468", "A61B 5/14546", "A61B 5/14507", "G01N 27/327"],
    ),
    # ---------------- WRIST ACTIGRAPHY / SLEEP ----------------
    E(
        id="cole-kripke-1992-wrist-actigraphy-sleep",
        canonical_name="Cole & Kripke et al. (1992) — automatic sleep/wake identification from wrist activity (the Cole-Kripke algorithm)",
        aliases=["Cole-Kripke algorithm", "wrist actigraphy sleep scoring"],
        first_disclosure_date="1992",
        disclosure_citation="Cole RJ, Kripke DF, Gruen W, Mullaney DJ, Gillin JC. 'Automatic sleep/wake identification from wrist activity.' Sleep 1992;15(5):461-469.",
        creator="Roger J. Cole / Daniel F. Kripke et al.",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-sleep-staging", "algo-activity-classification"],
        clinical_endpoints=["sleep", "sleep-wake-state"],
        prior_art_notes=(
            "Discloses an algorithm that classifies each epoch as sleep or wake from a "
            "wrist-worn activity (accelerometer) recording, validated against "
            "polysomnography — i.e. wrist actigraphy as a wearable sleep monitor. Any "
            "consumer-wearable claim reciting 'estimating sleep/wake state from a "
            "wrist-worn accelerometer signal' (the method underlying Fitbit/Jawbone-class "
            "sleep tracking) reads on Cole-Kripke 1992. Anchor for the accelerometry "
            "sleep-staging cross-cut; combined with the wrist form factor it makes "
            "wristworn sleep tracking obvious under [[obviousness-template]]."
        ),
        sources=["Cole RJ, Kripke DF, et al. Sleep 1992;15(5):461-469."],
        cpc_classifications=["A61B 5/4812", "A61B 5/1118", "A61B 5/6824"],
    ),
    E(
        id="sadeh-1994-actigraphy-sleep-wake-algorithm",
        canonical_name="Sadeh et al. (1994) — activity-based sleep-wake identification (the Sadeh algorithm)",
        aliases=["Sadeh algorithm", "actigraphy sleep algorithm"],
        first_disclosure_date="1994",
        disclosure_citation="Sadeh A, Sharkey KM, Carskadon MA. 'Activity-based sleep-wake identification: an empirical test of methodological issues.' Sleep 1994;17(3):201-207.",
        creator="Avi Sadeh / Katherine M. Sharkey / Mary A. Carskadon",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-sleep-staging", "algo-activity-classification"],
        clinical_endpoints=["sleep", "sleep-wake-state"],
        prior_art_notes=(
            "A second widely-used wrist-actigraphy sleep/wake scoring algorithm, with "
            "explicit treatment of the methodological choices (epoch length, scoring "
            "window, scaling). Prior art alongside [[cole-kripke-1992-wrist-actigraphy-sleep]] "
            "for any wearable claim reciting an actigraphy-based sleep-detection method or "
            "its parameters; both were published and validated by 1994."
        ),
        sources=["Sadeh A, Sharkey KM, Carskadon MA. Sleep 1994;17(3):201-207."],
        cpc_classifications=["A61B 5/4812", "A61B 5/1118", "A61B 5/6824"],
    ),
    E(
        id="ancoli-israel-2003-actigraphy-review",
        canonical_name="Ancoli-Israel et al. (2003) — 'The role of actigraphy in the study of sleep and circadian rhythms'",
        aliases=["actigraphy review", "Ancoli-Israel actigraphy"],
        first_disclosure_date="2003-05",
        disclosure_citation="Ancoli-Israel S, Cole R, Alessi C, Chambers M, Moorcroft W, Pollak CP. 'The role of actigraphy in the study of sleep and circadian rhythms.' Sleep 2003;26(3):342-392.",
        creator="Sonia Ancoli-Israel et al. (American Academy of Sleep Medicine review)",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["bracelet"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-sleep-staging"],
        clinical_endpoints=["sleep", "circadian-rhythm"],
        prior_art_notes=(
            "Authoritative review establishing wrist actigraphy — a wrist-worn "
            "accelerometer/activity recorder analyzed by validated algorithms — as an "
            "accepted method for estimating sleep parameters and circadian rhythm. Prior "
            "art for the proposition that a wrist-worn motion sensor with appropriate "
            "scoring yields clinically meaningful sleep metrics; the field, methods, and "
            "validation were settled and reviewed by 2003."
        ),
        sources=["Ancoli-Israel S, et al. Sleep 2003;26(3):342-392."],
        cpc_classifications=["A61B 5/4812", "A61B 5/1118", "A61B 5/4806"],
    ),
    # ---------------- SURFACE EMG / GESTURE CONTROL ----------------
    E(
        id="englehart-hudgins-2003-myoelectric-control",
        canonical_name="Englehart & Hudgins (2003) — robust real-time multifunction myoelectric (surface-EMG) control",
        aliases=["myoelectric control", "surface EMG gesture recognition", "Englehart-Hudgins"],
        first_disclosure_date="2003-07",
        disclosure_citation="Englehart K, Hudgins B. 'A robust, real-time control scheme for multifunction myoelectric control.' IEEE Transactions on Biomedical Engineering 2003;50(7):848-854.",
        creator="Kevin Englehart / Bernard Hudgins (UNB)",
        creator_country="CA",
        form_factor="armband",
        form_factor_tags=["garment"],
        contact_surface="skin",
        anatomical_target=["forearm", "upper-limb"],
        sensors=["sensor-emg"],
        algorithms=["algo-hand-gesture-emg", "algo-keystroke-emg"],
        clinical_endpoints=["electromyogram", "motor-intent", "gesture-class"],
        prior_art_notes=(
            "Discloses a real-time scheme that classifies the intended hand/finger action "
            "from multi-channel surface EMG (feature extraction over short windows, "
            "pattern-recognition classifier, continuous decision streaming) — the basis "
            "of EMG gesture-control wristbands/armbands. Any wearable claim reciting "
            "'classifying a hand gesture or movement intent from surface electromyography "
            "electrodes worn around the forearm/wrist' reads on Englehart & Hudgins 2003 "
            "for the classification method; combined with the armband form factor it makes "
            "an EMG gesture-control band obvious under [[obviousness-template]]. Anchor for "
            "the EMG × gesture-recognition cross-cut; [[myo-armband-2014]] is the product."
        ),
        sources=["Englehart K, Hudgins B. IEEE Trans Biomed Eng 2003;50(7):848-854."],
        cpc_classifications=["A61B 5/389", "G06F 3/015", "A61B 5/1118", "A61F 2/72"],
    ),
    # ---------------- AROUND-EAR / IN-EAR EEG ----------------
    E(
        id="looney-mandic-2012-in-ear-eeg",
        canonical_name="Looney et al. (2012) — 'The in-the-ear recording concept' (ear-EEG)",
        aliases=["ear-EEG", "in-ear EEG", "ITE EEG"],
        first_disclosure_date="2012-11",
        disclosure_citation="Looney D, Kidmose P, Park C, Ungstrup M, Rank ML, Rosenkranz K, Mandic DP. 'The in-the-ear recording concept: user-centered and wearable brain monitoring.' IEEE Pulse 2012;3(6):32-42. (See also Kidmose P, et al. 'A study of evoked potentials from ear-EEG.' IEEE Trans Biomed Eng 2013;60(10):2824-2830.)",
        creator="David Looney / Preben Kidmose / Danilo P. Mandic et al.",
        creator_country="GB",
        form_factor="earbud",
        form_factor_tags=["hearing-aid"],
        contact_surface="ear",
        anatomical_target=["ear-canal", "concha"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-drowsiness-detection", "algo-sleep-staging", "algo-bci-ssvep", "algo-erp-classification"],
        clinical_endpoints=["electroencephalogram", "auditory-evoked-potential", "alpha-rhythm"],
        prior_art_notes=(
            "Discloses recording EEG from electrodes placed inside the ear canal / concha "
            "of an individually-fitted earpiece — i.e. EEG in an earbud / hearing-aid form "
            "factor, demonstrated to capture alpha modulation, auditory steady-state and "
            "evoked responses. Any wearable claim reciting 'EEG electrodes disposed on an "
            "in-ear earpiece to measure an electroencephalographic signal of the wearer' "
            "reads on Looney et al. 2012. Anchor for the earbud/hearing-aid × EEG "
            "cross-cut; complementary to [[debener-2015-ceegrid-around-ear-eeg]] and "
            "[[zanetti-aminifar-atienza-eglass-2025]] (around-ear / temporal pickup)."
        ),
        sources=["Looney D, et al. IEEE Pulse 2012;3(6):32-42.", "Kidmose P, et al. IEEE Trans Biomed Eng 2013;60(10):2824-2830."],
        cpc_classifications=["A61B 5/24", "A61B 5/291", "A61B 5/378", "H04R 1/10"],
    ),
    E(
        id="debener-2015-ceegrid-around-ear-eeg",
        canonical_name="Debener et al. (2015) — cEEGrid: unobtrusive around-the-ear EEG with flexible printed electrodes",
        aliases=["cEEGrid", "around-ear EEG", "behind-the-ear EEG"],
        first_disclosure_date="2015-11-17",
        disclosure_citation="Debener S, Emkes R, De Vos M, Bleichner MG. 'Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear.' Scientific Reports 2015;5:16743.",
        creator="Stefan Debener / Martin G. Bleichner et al. (Oldenburg)",
        creator_country="DE",
        form_factor="patch",
        form_factor_tags=["headband", "glasses", "earbud"],
        contact_surface="skin",
        anatomical_target=["around-ear", "mastoid", "TP9", "TP10"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        algorithms=["algo-erp-classification", "algo-sleep-staging", "algo-drowsiness-detection"],
        clinical_endpoints=["electroencephalogram", "event-related-potential"],
        prior_art_notes=(
            "Discloses a flexible, printed, C-shaped electrode array worn around the ear "
            "(behind and below the auricle) for unobtrusive ambulatory EEG, recorded to a "
            "smartphone-class device. Any wearable claim reciting 'an array of EEG "
            "electrodes arranged around/behind the ear of the wearer' (the geometry used "
            "by EEG glasses, EEG earbuds, and EEG behind-the-ear stickers) reads on "
            "Debener et al. 2015. Directly relevant prior art for "
            "[[zanetti-aminifar-atienza-eglass-2025]] (which uses temporal/around-ear "
            "pickup) and for around-ear-EEG hearable claims; anchor for that cross-cut."
        ),
        sources=["Debener S, Emkes R, De Vos M, Bleichner MG. Sci Rep 2015;5:16743."],
        cpc_classifications=["A61B 5/24", "A61B 5/263", "A61B 5/291", "A61B 5/378"],
    ),
    # ---------------- WEARABLE-SYSTEMS REVIEWS ----------------
    E(
        id="pantelopoulos-bourbakis-2010-wearable-health-survey",
        canonical_name="Pantelopoulos & Bourbakis (2010) — survey on wearable sensor-based systems for health monitoring and prognosis",
        aliases=["wearable health monitoring survey 2010"],
        first_disclosure_date="2010-01",
        disclosure_citation="Pantelopoulos A, Bourbakis NG. 'A survey on wearable sensor-based systems for health monitoring and prognosis.' IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 2010;40(1):1-12.",
        creator="Alexandros Pantelopoulos / Nikolaos G. Bourbakis",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["watch", "garment", "patch", "bracelet"],
        contact_surface="skin",
        sensors=["sensor-ecg", "sensor-ppg", "sensor-spo2", "sensor-accelerometer", "sensor-skin-temperature", "sensor-respiration-impedance"],
        algorithms=["algo-hr", "algo-arrhythmia-classification", "algo-spo2-estimation", "algo-fall-detection", "algo-activity-classification"],
        clinical_endpoints=["multi-parameter-vitals"],
        prior_art_notes=(
            "Surveys, as of 2010, the architecture and components of wearable health-"
            "monitoring systems — sensors (ECG, PPG, SpO2, accelerometry, temperature, "
            "respiration), garment- and patch- and watch-based form factors, on-body "
            "processing, wireless body-area networking, and the analytics (arrhythmia, "
            "fall, activity, deterioration prediction). Prior art establishing that the "
            "general 'multi-sensor wearable + body-area network + cloud analytics' system "
            "architecture and its building blocks were collected and published by 2010 — "
            "useful against later claims to the bare system architecture. General anchor."
        ),
        sources=["Pantelopoulos A, Bourbakis NG. IEEE Trans Syst Man Cybern C 2010;40(1):1-12."],
        cpc_classifications=["A61B 5/0006", "A61B 5/00", "G16H 40/67", "H04W 84/18"],
    ),
    E(
        id="patel-bonato-2012-wearable-sensors-rehab-review",
        canonical_name="Patel et al. (2012) — 'A review of wearable sensors and systems with application in rehabilitation'",
        aliases=["wearable sensors rehabilitation review", "Patel-Bonato review"],
        first_disclosure_date="2012-04-20",
        disclosure_citation="Patel S, Park H, Bonato P, Chan L, Rodgers M. 'A review of wearable sensors and systems with application in rehabilitation.' Journal of NeuroEngineering and Rehabilitation 2012;9:21.",
        creator="Shyamal Patel / Hyung Park / Paolo Bonato et al.",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["garment", "patch", "watch", "shoe", "armband"],
        contact_surface="skin",
        sensors=["sensor-accelerometer", "sensor-gyroscope", "sensor-emg", "sensor-ecg", "sensor-ppg", "sensor-pressure-skin"],
        algorithms=["algo-gait-analysis", "algo-activity-classification", "algo-fall-detection", "algo-tremor-detection", "algo-bradykinesia-detection", "algo-posture-detection"],
        clinical_endpoints=["gait", "motor-function", "tremor", "activity"],
        prior_art_notes=(
            "Reviews, as of 2012, wearable inertial/EMG/pressure sensor systems for "
            "movement and physiological monitoring in rehabilitation and chronic-disease "
            "management — gait analysis, activity and posture classification, fall "
            "detection, tremor and bradykinesia quantification (Parkinson's), with the "
            "sensor placements (foot/insole, shank, thigh, trunk, wrist, forearm) and "
            "algorithms. Prior art for wearable movement-disorder and gait-monitoring "
            "claims reciting any of the placements/analytics surveyed; collected and "
            "published by 2012. General anchor for the gait / tremor / activity cross-cuts."
        ),
        sources=["Patel S, Park H, Bonato P, Chan L, Rodgers M. J NeuroEng Rehabil 2012;9:21."],
        cpc_classifications=["A61B 5/1124", "A61B 5/1101", "A61B 5/4082", "A61B 5/1117"],
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
    print(f"  real academic r3: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
