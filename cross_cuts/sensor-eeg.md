---
title: sensor-eeg
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-eeg`

Axis: **sensors**

**15 corpus entries disclose this tag.**

Earliest disclosure: 1929

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Berger (1929) — first recording of the human electroencephalogram (1929)

- **id**: `berger-1929-human-eeg`
- **corpus**: academic
- **form factor**: other
- **creator**: Hans Berger
- **disclosure**: Berger H. 'Über das Elektrenkephalogramm des Menschen.' Archiv für Psychiatrie und Nervenkrankheiten 1929;87:527-570 (recordings made from 1924).
- **ip status**: public-domain
- **sensors**: sensor-eeg
- **prior art notes**: First demonstration of the human EEG and of the alpha rhythm — the disclosure root of all scalp EEG measurement. Any wearable claim reciting 'scalp electrodes positioned to measure an electroencephalographic signal' rests on a technique public since 1929. § 102 prior art for the EEG principle; the headband / cap / glasses / earbud EEG variants are obvious combinations under [[obviousness-template]].

## Aserinsky & Kleitman (1953) — discovery of REM sleep via electrooculography (1953-09-04)

- **id**: `aserinsky-kleitman-1953-rem-sleep`
- **corpus**: academic
- **form factor**: other
- **creator**: Eugene Aserinsky / Nathaniel Kleitman (University of Chicago)
- **disclosure**: Aserinsky E, Kleitman N. 'Regularly occurring periods of eye motility, and concomitant phenomena, during sleep.' Science 1953;118(3062):273-274.
- **ip status**: public-domain
- **sensors**: sensor-eog, sensor-eeg
- **algorithms**: algo-sleep-staging
- **prior art notes**: Establishes that sleep is not homogeneous — that there are recurring periods of rapid eye movement detectable by electrooculography (with concomitant EEG changes) — i.e. the existence of distinguishable sleep states detectable from ocular/cortical electrophysiology. Foundational prior art for any sleep-staging wearable: the premise that sleep states are detectable from EOG/EEG signals is public since 1953. Anchor for the sleep-staging cross-cut.

## Rechtschaffen & Kales (1968) — standardized sleep-stage scoring manual (1968)

- **id**: `rechtschaffen-kales-1968-sleep-scoring-manual`
- **corpus**: standards
- **form factor**: other
- **creator**: Allan Rechtschaffen / Anthony Kales (eds), for the UCLA Brain Information Service
- **disclosure**: Rechtschaffen A, Kales A (eds). 'A Manual of Standardized Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects.' Public Health Service / U.S. Government Printing Office / UCLA Brain Information Service, NIH Publication No. 204, 1968.
- **ip status**: standards
- **sensors**: sensor-eeg, sensor-eog, sensor-emg
- **algorithms**: algo-sleep-staging
- **prior art notes**: Standardizes the definition of sleep stages and the rules for scoring them from EEG + EOG + EMG (polysomnography). Any wearable claim reciting 'classifying sleep into stages from electrophysiological/physiological signals' rests on the staging framework standardized here. Combined with [[muse-headband-2014]]-type form-factor disclosures, makes wearable automated sleep-staging an obvious combination under [[obviousness-template]].

## Strange Days — SQUID head-worn neural experience recorder (1995-10-13)

- **id**: `strange-days-squid-recorder`
- **corpus**: fictional
- **form factor**: cap
- **creator**: Kathryn Bigelow / James Cameron (writer) / Lightstorm
- **disclosure**: Strange Days (Lightstorm Entertainment / 20th Century Fox), released October 13, 1995; the 'SQUID' — a fine wire-mesh cap worn under a hat that records the wearer's full multisensory and emotional experience directly from the cerebral cortex for later playback into another person's cortex.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **prior art notes**: Discloses a head-worn mesh of scalp electrodes that records a rich, multi-channel signal of the wearer's perceptual and affective experience for storage and later replay. Relevant to wearable neural-recording claims combining 'a head-worn array of scalp electrodes', 'acquisition of a multi-channel cortical signal', 'encoding of perceptual/affective content', and 'storage for later playback'. § 103 motivation that the wearable experience-recording headset was an articulated objective by 1995. Non-enabling on the encoding/playback; pair with enabling EEG/BCI art.

## Wolpaw et al. (2002) — 'Brain-computer interfaces for communication and control' (2002-06)

- **id**: `wolpaw-2002-bci-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jonathan R. Wolpaw et al.
- **disclosure**: Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM. 'Brain-computer interfaces for communication and control.' Clinical Neurophysiology 2002;113(6):767-791.
- **ip status**: public-domain
- **sensors**: sensor-eeg
- **algorithms**: algo-bci-p300, algo-bci-ssvep, algo-bci-motor-imagery, algo-erp-classification
- **prior art notes**: Canonical review establishing, as of 2002, the major non-invasive EEG-based BCI paradigms (sensorimotor rhythms / motor imagery, P300 evoked potentials, SSVEP, slow cortical potentials) and the signal-processing pipeline for translating EEG into control output. Prior art for wearable-BCI claims reciting any of these paradigms with scalp EEG: the paradigms and methods were published and enabled by 2002. Anchor for the BCI algorithm cross-cuts.

## Surrogates — head-worn neural interface rig for robot-body telepresence (2005-08-17)

- **id**: `surrogates-neural-teleoperation-rig`
- **corpus**: fictional
- **form factor**: headband
- **creator**: Robert Venditti and Brett Weldele
- **disclosure**: Venditti, Robert; Weldele, Brett. The Surrogates #1. Top Shelf Productions, 2005 (film adaptation: Touchstone Pictures, 2009); operators recline in a chair wearing a head-mounted neural interface that captures their volition and sensory channels to remotely embody and control a humanoid robot 'surrogate', receiving its sensory feedback in return.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **prior art notes**: Discloses a head-worn neural-interface rig that reads the wearer's motor intent and routes sensory feedback, used to teleoperate a humanoid robot with the operator perceiving through the robot's sensors. Relevant to wearable-BCI teleoperation claims combining 'a head-worn neural sensor array', 'decoding of motor intent', 'transmission of commands to a remote robot', and 'return of the robot's sensory data to the wearer'. § 103 motivation that the wearable neural-interface telepresence rig was an articulated objective by 2005. Non-enabling; pair with enabling BCI/teleop art.

## NeuroSky MindSet / MindWave (2007) — single dry-electrode consumer EEG headset (2007)

- **id**: `neurosky-mindset-2007`
- **corpus**: private
- **form factor**: headband
- **creator**: NeuroSky, Inc.
- **disclosure**: NeuroSky, Inc. 'MindSet' (and later 'MindWave') consumer EEG headset, with the 'ThinkGear' single dry forehead (Fp1) electrode and ear-clip reference, output as 'eSense' attention and meditation metrics plus raw EEG, first shown 2007.
- **ip status**: patented
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-attention-state, algo-cognitive-workload
- **prior art notes**: Discloses a low-cost head-worn single-channel dry-electrode EEG device (forehead pickup, ear reference) outputting raw EEG plus derived 'attention' and 'meditation/relaxation' metrics to a paired device. Anticipates consumer-EEG-headband claims combining 'a head-worn dry forehead electrode with an ear reference', 'on-device band-power feature extraction', and 'a derived attention/relaxation index' from 2007. Product-side anchor for the headband × EEG cross-cut; predates Muse (2014) and Emotiv EPOC (2009).

## CHB-MIT Scalp EEG Database (Shoeb, 2009) — benchmark seizure-detection dataset (2009-08)

- **id**: `chb-mit-scalp-eeg-database-2009`
- **corpus**: academic
- **form factor**: other
- **creator**: Ali H. Shoeb (MIT / Boston Children's Hospital)
- **disclosure**: Shoeb AH. 'Application of Machine Learning to Epileptic Seizure Onset Detection and Treatment.' PhD thesis, MIT, 2009 (the CHB-MIT Scalp EEG Database, distributed via PhysioNet, physionet.org/content/chbmit).
- **ip status**: public-domain
- **sensors**: sensor-eeg, sensor-saline-eeg-electrode
- **algorithms**: algo-seizure-detection
- **prior art notes**: Publishes a labelled scalp-EEG corpus and a machine-learning method for patient-specific seizure-onset detection, establishing the public benchmark and the patient-calibrated detection paradigm used by subsequent wearable seizure detectors. Relevant to seizure-detection-wearable claims reciting 'a classifier trained on EEG to detect seizure onset', particularly 'patient-specific' or 'per-subject calibrated' variants — the paradigm and a reference implementation were public by 2009. Anchor for the EEG × seizure-detection cross-cut; [[zanetti-aminifar-atienza-eglass-2025]] reports against it.

## Emotiv EPOC (2009) — 14-channel wireless saline-electrode consumer EEG headset (2009-12)

- **id**: `emotiv-epoc-2009`
- **corpus**: private
- **form factor**: headband
- **creator**: Emotiv Systems
- **disclosure**: Emotiv Systems. 'EPOC' EEG headset, released December 2009 — a 14-channel (plus 2 reference) wireless headset with saline-felt electrodes covering frontal/temporal/parietal/occipital sites, with SDKs for mental-command, facial-expression and 'affective' detections.
- **ip status**: patented
- **sensors**: sensor-saline-eeg-electrode, sensor-eeg
- **algorithms**: algo-cognitive-workload, algo-emotion-recognition, algo-bci-motor-imagery
- **prior art notes**: Discloses a wireless multi-channel (14+2) consumer EEG headset with saline-wetted contact electrodes at standard scalp sites and on-device/SDK classifiers for mental commands, facial expressions, and affective states. Anticipates multi-channel consumer-EEG-headset claims combining 'a wireless head-worn array of ≥8 contact electrodes', 'wet/saline electrode coupling', and 'classification of cognitive/affective state or intent' from 2009. Product-side anchor for the headband/cap × EEG cross-cut.

## Kim et al. (Rogers group) (2011) — 'Epidermal Electronics' (electronic-tattoo skin-mounted devices) (2011-08-12)

- **id**: `kim-rogers-2011-epidermal-electronics`
- **corpus**: academic
- **form factor**: tattoo-electronic
- **creator**: Dae-Hyeong Kim et al. / John A. Rogers group (Illinois)
- **disclosure**: Kim D-H, Lu N, Ma R, Kim Y-S, Kim R-H, Wang S, et al. (Rogers JA). 'Epidermal Electronics.' Science 2011;333(6044):838-843.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-emg, sensor-eeg, sensor-skin-temperature, sensor-strain-gauge
- **prior art notes**: Discloses ultrathin, skin-conformal ('epidermal') electronic devices laminated directly onto the skin like a temporary tattoo, integrating electrodes, sensors (ECG, EMG, EEG, temperature, strain), interconnects, and even wireless components, mechanically matched to the skin so they move with it. The foundational disclosure of the 'electronic skin / electronic tattoo' form factor. Any claim reciting 'an ultrathin stretchable electronic device conformally mounted on the skin' for physiological sensing reads on Kim/Rogers 2011. Anchor for the tattoo-electronic form-factor cross-cut on the real side.

## Looney et al. (2012) — 'The in-the-ear recording concept' (ear-EEG) (2012-11)

- **id**: `looney-mandic-2012-in-ear-eeg`
- **corpus**: academic
- **form factor**: earbud
- **creator**: David Looney / Preben Kidmose / Danilo P. Mandic et al.
- **disclosure**: Looney D, Kidmose P, Park C, Ungstrup M, Rank ML, Rosenkranz K, Mandic DP. 'The in-the-ear recording concept: user-centered and wearable brain monitoring.' IEEE Pulse 2012;3(6):32-42. (See also Kidmose P, et al. 'A study of evoked potentials from ear-EEG.' IEEE Trans Biomed Eng 2013;60(10):2824-2830.)
- **ip status**: public-domain
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-drowsiness-detection, algo-sleep-staging, algo-bci-ssvep, algo-erp-classification
- **prior art notes**: Discloses recording EEG from electrodes placed inside the ear canal / concha of an individually-fitted earpiece — i.e. EEG in an earbud / hearing-aid form factor, demonstrated to capture alpha modulation, auditory steady-state and evoked responses. Any wearable claim reciting 'EEG electrodes disposed on an in-ear earpiece to measure an electroencephalographic signal of the wearer' reads on Looney et al. 2012. Anchor for the earbud/hearing-aid × EEG cross-cut; complementary to [[debener-2015-ceegrid-around-ear-eeg]] and [[zanetti-aminifar-atienza-eglass-2025]] (around-ear / temporal pickup).

## Muse headband (InteraXon, 2014) — multi-channel dry-electrode EEG headband for meditation and sleep (2014-05)

- **id**: `muse-headband-2014`
- **corpus**: private
- **form factor**: headband
- **creator**: InteraXon Inc.
- **disclosure**: InteraXon Inc. 'Muse' brain-sensing headband, shipped 2014 — a forehead-band EEG device with frontal (AF7/AF8/Fp1/Fp2-region) and behind-the-ear (TP9/TP10) dry/conductive-rubber electrodes, giving real-time neurofeedback for meditation (and, in 'Muse S', sleep tracking).
- **ip status**: patented
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-attention-state, algo-cognitive-workload, algo-sleep-staging
- **prior art notes**: Discloses a forehead-band wearable EEG device with frontal and behind-the-ear (TP9/TP10) dry electrodes providing real-time neurofeedback for meditation training and (later) sleep staging. Anticipates EEG-headband claims combining 'a forehead band', 'frontal and mastoid/behind-ear dry electrodes', and 'real-time feedback on a meditation or sleep state' from 2014. Note: its TP9/TP10 around-ear pickup is the same general region used by [[zanetti-aminifar-atienza-eglass-2025]] — relevant prior art for around-ear-EEG wearable claims. Product-side anchor for the headband × EEG cross-cut.

## Debener et al. (2015) — cEEGrid: unobtrusive around-the-ear EEG with flexible printed electrodes (2015-11-17)

- **id**: `debener-2015-ceegrid-around-ear-eeg`
- **corpus**: academic
- **form factor**: patch
- **creator**: Stefan Debener / Martin G. Bleichner et al. (Oldenburg)
- **disclosure**: Debener S, Emkes R, De Vos M, Bleichner MG. 'Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear.' Scientific Reports 2015;5:16743.
- **ip status**: public-domain
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-erp-classification, algo-sleep-staging, algo-drowsiness-detection
- **prior art notes**: Discloses a flexible, printed, C-shaped electrode array worn around the ear (behind and below the auricle) for unobtrusive ambulatory EEG, recorded to a smartphone-class device. Any wearable claim reciting 'an array of EEG electrodes arranged around/behind the ear of the wearer' (the geometry used by EEG glasses, EEG earbuds, and EEG behind-the-ear stickers) reads on Debener et al. 2015. Directly relevant prior art for [[zanetti-aminifar-atienza-eglass-2025]] (which uses temporal/around-ear pickup) and for around-ear-EEG hearable claims; anchor for that cross-cut.

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.

## e-Glass (Zanetti, Aminifar, Atienza; EPFL, 2025) — wearable EEG eyeglasses (2025-11-29)

- **id**: `zanetti-aminifar-atienza-eglass-2025`
- **corpus**: academic
- **form factor**: glasses
- **creator**: Renato Zanetti / Amir Aminifar / David Atienza (EPFL ESL)
- **disclosure**: Zanetti R, Aminifar A, Atienza D, et al. 'e-Glass: ...' (wearable EEG monitoring in an eyeglasses form factor with edge ML for seizure detection and cognitive-workload monitoring). Scientific Reports 2025. doi:10.1038/s41598-025-29893-4.
- **ip status**: unknown
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-seizure-detection, algo-cognitive-workload
- **prior art notes**: Discloses an eyeglasses-form-factor wearable EEG monitor with dry electrodes at the temples / around the ears (temporal/occipital pickup, validated against a reference montage at r≈0.93) and on-device machine learning for two applications — ambulatory seizure detection and cognitive-workload monitoring. Relevant to AR-glasses / smart-eyewear claims reciting 'EEG electrodes integrated into an eyeglasses frame' and 'an on-device classifier operating on the EEG'. Anchor for the glasses × EEG cross-cut. Bounds the application space: temple/around-ear contact supports seizure, drowsiness, attention, SSVEP — not frontal ERP or motor-imagery BCI.
