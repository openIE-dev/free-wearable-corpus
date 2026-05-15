---
title: other ∩ sensor-ecg
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `sensor-ecg`

Axes: **form_factor × sensors**

**11 corpus entries disclose both tags.**

Earliest disclosure: 1903

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Einthoven (1903) — the string galvanometer electrocardiogram (1903)

- **id**: `einthoven-1903-string-galvanometer-ecg`
- **corpus**: academic
- **form factor**: other
- **creator**: Willem Einthoven
- **disclosure**: Einthoven W. 'Die galvanometrische Registrirung des menschlichen Elektrokardiogramms, zugleich eine Beurtheilung der Anwendung des Capillar-Elektrometers in der Physiologie.' Pflügers Archiv 1903;99:472-480. (Nobel Prize in Physiology or Medicine, 1924.)
- **ip status**: public-domain
- **sensors**: sensor-ecg
- **prior art notes**: First practical recording of the human electrocardiogram and the foundational lead concept (Einthoven's triangle, the limb leads). The disclosure root of all ECG measurement: any wearable claim reciting 'electrodes positioned to measure an electrocardiographic signal of the wearer' rests on a technique public since 1903. § 102 prior art for the ECG principle; the wristworn / patch / garment single-lead variants are obvious combinations under [[obviousness-template]].

## Geddes et al. (1981) — pulse transit time as an indicator of arterial blood pressure (1981-01)

- **id**: `geddes-1981-pulse-transit-time-bp`
- **corpus**: academic
- **form factor**: other
- **creator**: Leslie A. Geddes et al. (Purdue)
- **disclosure**: Geddes LA, Voelz MH, Babbs CF, Bourland JD, Tacker WA. 'Pulse transit time as an indicator of arterial blood pressure.' Psychophysiology 1981;18(1):71-74.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Establishes that pulse transit time — the delay between a proximal timing reference (e.g. the ECG R-wave) and the arrival of the pulse at a distal site (e.g. a finger PPG) — varies inversely with arterial blood pressure, and can therefore be used to estimate BP without a cuff. Any cuffless-BP wearable claim reciting 'estimating blood pressure from a pulse transit time (or pulse arrival time / pulse wave velocity) derived from two physiological signals' reads on Geddes 1981. Earliest anchor for the PTT-cuffless-BP cross-cut; [[mukkamala-2015-ptt-cuffless-bp-review]] is the modern survey.

## Task Force of the ESC and NASPE (1996) — heart rate variability: standards of measurement (1996-03)

- **id**: `esc-naspe-1996-hrv-standards`
- **corpus**: standards
- **form factor**: other
- **creator**: Task Force of the ESC and NASPE
- **disclosure**: Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. 'Heart rate variability: standards of measurement, physiological interpretation, and clinical use.' Circulation 1996;93(5):1043-1065 (also European Heart Journal 1996;17:354-381).
- **ip status**: standards
- **sensors**: sensor-ecg, sensor-ppg
- **algorithms**: algo-hrv, algo-stress-index
- **prior art notes**: Standardizes the time-domain (SDNN, RMSSD, pNN50, ...) and frequency-domain (VLF/LF/HF, LF/HF ratio) measures of heart rate variability, their computation from an interbeat-interval series, and their physiological interpretation. Any wearable claim reciting 'computing a heart-rate-variability metric (e.g. RMSSD, LF/HF) from a sequence of interbeat intervals' rests on metrics standardized here. Anchor for the HRV cross-cut; applicable whether the interbeat intervals come from ECG or PPG.

## Continua Health Alliance — Design Guidelines (first edition, 2007) (2007)

- **id**: `continua-design-guidelines-2007`
- **corpus**: standards
- **form factor**: other
- **creator**: Continua Health Alliance
- **disclosure**: Continua Health Alliance (later Personal Connected Health Alliance). 'Continua Design Guidelines' (first edition published 2007; subsequently maintained, ITU-T H.810 series). Specifies end-to-end interoperability for personal connected health devices, profiling IEEE 11073, Bluetooth, USB, ZigBee, HL7/IHE.
- **ip status**: standards
- **sensors**: sensor-ppg, sensor-ecg, sensor-glucose-cgm, sensor-accelerometer
- **algorithms**: algo-hr, algo-step-count, algo-glucose-cgm-readout
- **prior art notes**: Publicly-published end-to-end interoperability framework for personal connected health devices — defining how a body-worn sensor (weight scale, blood-pressure cuff, glucose meter, pulse oximeter, activity monitor, ECG, etc.) connects to an application hub and onward to health-record systems, profiling the underlying transport and data standards. Prior art for connected-wearable-system claims reciting the architecture, the device-to-hub-to-record data flow, or the standard profiles assembled here, public from 2007.

## Pantelopoulos & Bourbakis (2010) — survey on wearable sensor-based systems for health monitoring and prognosis (2010-01)

- **id**: `pantelopoulos-bourbakis-2010-wearable-health-survey`
- **corpus**: academic
- **form factor**: other
- **creator**: Alexandros Pantelopoulos / Nikolaos G. Bourbakis
- **disclosure**: Pantelopoulos A, Bourbakis NG. 'A survey on wearable sensor-based systems for health monitoring and prognosis.' IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 2010;40(1):1-12.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-skin-temperature, sensor-respiration-impedance
- **algorithms**: algo-hr, algo-arrhythmia-classification, algo-spo2-estimation, algo-fall-detection, algo-activity-classification
- **prior art notes**: Surveys, as of 2010, the architecture and components of wearable health-monitoring systems — sensors (ECG, PPG, SpO2, accelerometry, temperature, respiration), garment- and patch- and watch-based form factors, on-body processing, wireless body-area networking, and the analytics (arrhythmia, fall, activity, deterioration prediction). Prior art establishing that the general 'multi-sensor wearable + body-area network + cloud analytics' system architecture and its building blocks were collected and published by 2010 — useful against later claims to the bare system architecture. General anchor.

## Bluetooth SIG — Heart Rate Profile / Heart Rate Service (2011) (2011-07-12)

- **id**: `bluetooth-sig-heart-rate-profile-2011`
- **corpus**: standards
- **form factor**: other
- **creator**: Bluetooth Special Interest Group
- **disclosure**: Bluetooth SIG. 'Heart Rate Profile' specification v1.0 and 'Heart Rate Service' (GATT service UUID 0x180D, characteristics: Heart Rate Measurement 0x2A37, Body Sensor Location 0x2A38, Heart Rate Control Point 0x2A39), adopted 12 July 2011; available at bluetooth.com/specifications.
- **ip status**: standards
- **sensors**: sensor-ppg, sensor-ecg
- **algorithms**: algo-hr
- **prior art notes**: A publicly-adopted standard defining how a body-worn heart-rate sensor advertises, structures, and transmits heart-rate measurements (including energy expended and RR-interval data) over Bluetooth Low Energy to a collector, with a defined sensor-location enumeration including wrist, finger, ear, chest, foot, hand. Prior art for wearable-HR claims reciting 'a BLE-advertised heart-rate measurement characteristic', 'transmission of RR intervals from a body-worn sensor', or a 'body sensor location' field — these were standardized and public from 2011. Relevant to PPG and ECG HR wearables alike.

## IEEE Std 11073-10406-2011 — personal health device communication: basic electrocardiograph (1- to 3-lead ECG) (2011-12-30)

- **id**: `ieee-11073-10406-basic-ecg-2011`
- **corpus**: standards
- **form factor**: other
- **creator**: IEEE / ISO/IEEE 11073 Personal Health Devices Working Group
- **disclosure**: IEEE Std 11073-10406-2011. 'Health informatics — Personal health device communication — Part 10406: Device specialization — Basic electrocardiograph (ECG) (1- to 3-lead ECG).' IEEE, 2011.
- **ip status**: standards
- **sensors**: sensor-ecg
- **algorithms**: algo-hr, algo-arrhythmia-classification
- **prior art notes**: A publicly-adopted standard defining the device model and data exchange for a personal/consumer 1-to-3-lead electrocardiograph — including reporting of the ECG waveform, derived heart rate, and rhythm/event annotations from a body-worn or handheld single-lead ECG device. Prior art for consumer-single-lead-ECG-wearable claims reciting the device model, lead configuration, or data fields standardized here (public from 2011, predating the Apple Watch / AliveCor consumer-ECG patent wave's later filings).

## Patel et al. (2012) — 'A review of wearable sensors and systems with application in rehabilitation' (2012-04-20)

- **id**: `patel-bonato-2012-wearable-sensors-rehab-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Shyamal Patel / Hyung Park / Paolo Bonato et al.
- **disclosure**: Patel S, Park H, Bonato P, Chan L, Rodgers M. 'A review of wearable sensors and systems with application in rehabilitation.' Journal of NeuroEngineering and Rehabilitation 2012;9:21.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-emg, sensor-ecg, sensor-ppg, sensor-pressure-skin
- **algorithms**: algo-gait-analysis, algo-activity-classification, algo-fall-detection, algo-tremor-detection, algo-bradykinesia-detection, algo-posture-detection
- **prior art notes**: Reviews, as of 2012, wearable inertial/EMG/pressure sensor systems for movement and physiological monitoring in rehabilitation and chronic-disease management — gait analysis, activity and posture classification, fall detection, tremor and bradykinesia quantification (Parkinson's), with the sensor placements (foot/insole, shank, thigh, trunk, wrist, forearm) and algorithms. Prior art for wearable movement-disorder and gait-monitoring claims reciting any of the placements/analytics surveyed; collected and published by 2012. General anchor for the gait / tremor / activity cross-cuts.

## AliveCor Heart Monitor / KardiaMobile (2012) — smartphone-coupled single-lead ECG (2012-12)

- **id**: `alivecor-kardiamobile-2012`
- **corpus**: private
- **form factor**: other
- **creator**: AliveCor, Inc. (David Albert)
- **disclosure**: AliveCor, Inc. 'AliveCor Heart Monitor' (later 'KardiaMobile'), FDA-cleared December 2012 — a card-sized two-electrode module that records a single-lead ECG via dry electrodes touched by the fingers (or pressed to the chest) and streams it to a smartphone app for AF detection. (The 'Kardia Band' wrist-strap ECG accessory for Apple Watch followed in 2017, FDA cleared.)
- **ip status**: patented
- **sensors**: sensor-ecg
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-hr
- **prior art notes**: Discloses a portable two-dry-electrode single-lead ECG recorder that the user contacts with the fingers (or chest) and that streams the trace to a smartphone for automated atrial-fibrillation detection — and, in the 2017 Kardia Band variant, the same dry-electrode single-lead ECG integrated into a wrist strap. Anticipates consumer single-lead-ECG and wrist-strap-ECG AF-detection claims from 2012/2017 — predating the Apple Watch Series 4 ECG (2018). Product-side anchor for the consumer-ECG cross-cut.

## Mukkamala et al. (2015) — 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice' (2015-08)

- **id**: `mukkamala-2015-ptt-cuffless-bp-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Ramakrishna Mukkamala et al.
- **disclosure**: Mukkamala R, Hahn J-O, Inan OT, Mestha LK, Kim C-S, Töreyin H, Kyal S. 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice.' IEEE Transactions on Biomedical Engineering 2015;62(8):1879-1901.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt, sensor-cuffless-bp-tonometry
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Canonical 2015 review of cuffless blood-pressure estimation by pulse transit time / pulse arrival time / pulse wave velocity: the physiological models, the practical sensor configurations (ECG+PPG, dual PPG, ballistocardiogram+PPG), the calibration strategies, and the accuracy limitations. Prior art for cuffless-BP wearable claims reciting any of the configurations or calibration approaches surveyed here — they were collected, modeled, and published by 2015. Combined with watch/ring/patch form-factor disclosures, makes wearable PTT-based BP an obvious combination under [[obviousness-template]].

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.
