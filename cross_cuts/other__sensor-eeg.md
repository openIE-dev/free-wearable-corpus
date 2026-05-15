---
title: other ∩ sensor-eeg
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `sensor-eeg`

Axes: **form_factor × sensors**

**6 corpus entries disclose both tags.**

Earliest disclosure: 1929

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

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

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.
