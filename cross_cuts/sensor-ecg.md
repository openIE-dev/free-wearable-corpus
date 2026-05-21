---
title: sensor-ecg
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-ecg`

Axis: **sensors**

**29 corpus entries disclose this tag.**

Earliest disclosure: 1903

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

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

## Holter (1961) — continuous ambulatory electrocardiography (the Holter monitor) (1961-04-21)

- **id**: `holter-1961-ambulatory-ecg`
- **corpus**: academic
- **form factor**: garment
- **creator**: Norman J. Holter
- **disclosure**: Holter NJ. 'New method for heart studies: continuous electrocardiography of active subjects over long periods is now practical.' Science 1961;134(3486):1214-1220.
- **ip status**: public-domain
- **sensors**: sensor-ecg
- **algorithms**: algo-arrhythmia-classification
- **prior art notes**: Establishes continuous, ambulatory, body-worn recording of the ECG over hours to days while the subject is active, for later analysis — the foundational 'wearable continuous ECG monitor'. Any claim reciting 'a body-worn device configured to continuously record an electrocardiographic signal of the wearer over an extended period for subsequent arrhythmia analysis' reads on Holter 1961. Anchor for the ambulatory-ECG / ECG-patch cross-cut; [[zio-patch-irhythm-2009]] and Apple Watch's ECG history both build on it.

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

## Polar Sport Tester PE2000 — first wireless wrist heart-rate monitor (1982)

- **id**: `polar-sport-tester-pe2000-1982`
- **corpus**: private
- **form factor**: watch
- **creator**: Polar Electro Oy (Seppo Säynäjäkangas)
- **disclosure**: Polar Electro Oy. 'Sport Tester PE2000' wrist heart-rate monitor, introduced 1982 — a chest electrode strap transmitting ECG-derived heart rate wirelessly to a wrist-worn receiver/display. Underlying invention: Seppo Säynäjäkangas, wireless heart-rate measurement, patents filed from c. 1977 (Polar Electro).
- **ip status**: patented
- **sensors**: sensor-ecg
- **algorithms**: algo-hr
- **prior art notes**: Discloses a body-worn heart-rate monitoring system: a chest strap with electrodes deriving heart rate from the ECG and transmitting it wirelessly to a wrist-worn receiver that displays it. Anticipates claims combining 'a chest-worn electrode assembly sensing heart rate' and 'wireless transmission to a wrist-worn display' (the chest-strap-plus-watch architecture), and the bare 'wristworn heart-rate display' concept, from 1982 (invention c. 1977). Anchor for the wristworn-HR cross-cut on the product side; [[bluetooth-sig-heart-rate-profile-2011]] later standardized the comms link.

## Neon Genesis Evangelion — 'plug suit' and 'A10 nerve clips' (bio-monitoring suit + head-worn neural sync interface) (1995-10-04)

- **id**: `nge-plug-suit-and-a10-clips`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Hideaki Anno / Gainax
- **disclosure**: Neon Genesis Evangelion (Gainax television series, premiered 4 October 1995); pilots wear a skin-tight pressurized 'plug suit' with continuous bio-monitoring and a measured 'synchronization ratio' with the mecha, plus 'A10 nerve clips' worn on the head that interface the pilot's nervous system to the machine.
- **ip status**: fictional
- **sensors**: sensor-ecg, sensor-dry-eeg-electrode, sensor-respiration-impedance
- **algorithms**: algo-hr, algo-respiratory-rate
- **prior art notes**: Discloses (a) a form-fitting body garment with continuous vital-sign monitoring and a derived operator-machine synchronization metric, and (b) head-worn clips coupling the wearer's nervous system to an external system. Relevant to instrumented-bodysuit claims combining 'a close-fitting garment with distributed physiological sensors' and 'a derived synchronization/engagement metric', and to head-worn neural-interface claims. § 103 motivation as of 1995. Cf. [[pacific-rim-drivesuit-and-conn-pod]] (a later dual-pilot variant).

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

## Garmin Forerunner 201 (2003) — wristworn GPS running watch with pace/distance and heart-rate (strap) integration (2003)

- **id**: `garmin-forerunner-201-2003`
- **corpus**: private
- **form factor**: watch
- **creator**: Garmin Ltd.
- **disclosure**: Garmin Ltd. 'Forerunner 101/201', introduced 2003 — a wrist-worn GPS receiver/watch logging pace, distance, route, and (with a paired chest strap) heart rate, with workout history and a web/PC sync. Later Garmin watches (Fenix/Forerunner with the 'Elevate' optical sensor, c. 2015) moved heart rate, and subsequently SpO2 (pulse ox) and respiration, onto the wrist.
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-ecg, sensor-ppg
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification
- **prior art notes**: Discloses a wrist-worn GPS sport watch deriving pace, distance, and route, integrating heart rate from a paired electrode chest strap, and syncing workout history to a host — and, in later Garmin models, on-wrist optical-PPG heart rate, SpO2, and respiration. Anticipates GPS-sport-watch claims from 2003 and (for the later models) wrist-optical-vitals claims. Product-side anchor for the watch × GPS-fitness cross-cut.

## Paradiso et al. (2005) — 'A wearable health care system based on knitted integrated sensors' (WEALTHY) (2005-09)

- **id**: `paradiso-2005-wealthy-knitted-smart-shirt`
- **corpus**: academic
- **form factor**: garment
- **creator**: Rita Paradiso / Giannicola Loriga / Nicola Taccini (Smartex / CNR, Italy; EU WEALTHY consortium)
- **disclosure**: Paradiso R, Loriga G, Taccini N. 'A wearable health care system based on knitted integrated sensors.' IEEE Transactions on Information Technology in Biomedicine 2005;9(3):337-344. (Output of the EU FP5 'WEALTHY' project, 2002-2005.)
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification
- **prior art notes**: Discloses a smart shirt with electrodes and sensors knitted directly into the textile (conductive yarns forming dry ECG electrodes; piezoresistive yarns forming respiration sensors via thoracic/abdominal expansion; accelerometer; temperature) plus an on-garment electronic interface and wireless link, deriving ECG, heart rate, respiration, posture/activity, and temperature — i.e. a fully integrated textile-electrode wearable. Any claim reciting 'an item of clothing with electrodes/sensors integrated into the fabric structure for physiological monitoring' reads on Paradiso 2005. Anchor for the garment × textile-electrode cross-cut; the foundational EU project for the smart-shirt patent space (Hexoskin, Cityzen, etc. all build on this lineage).

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

## Kim et al. (Rogers group) (2011) — 'Epidermal Electronics' (electronic-tattoo skin-mounted devices) (2011-08-12)

- **id**: `kim-rogers-2011-epidermal-electronics`
- **corpus**: academic
- **form factor**: tattoo-electronic
- **creator**: Dae-Hyeong Kim et al. / John A. Rogers group (Illinois)
- **disclosure**: Kim D-H, Lu N, Ma R, Kim Y-S, Kim R-H, Wang S, et al. (Rogers JA). 'Epidermal Electronics.' Science 2011;333(6044):838-843.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-emg, sensor-eeg, sensor-skin-temperature, sensor-strain-gauge
- **prior art notes**: Discloses ultrathin, skin-conformal ('epidermal') electronic devices laminated directly onto the skin like a temporary tattoo, integrating electrodes, sensors (ECG, EMG, EEG, temperature, strain), interconnects, and even wireless components, mechanically matched to the skin so they move with it. The foundational disclosure of the 'electronic skin / electronic tattoo' form factor. Any claim reciting 'an ultrathin stretchable electronic device conformally mounted on the skin' for physiological sensing reads on Kim/Rogers 2011. Anchor for the tattoo-electronic form-factor cross-cut on the real side.

## FDA 510(k) K113862 (~2011) — iRhythm Zio Patch, long-term single-lead adhesive ECG monitor (2011-12)

- **id**: `fda-k113862-irhythm-zio-patch-2011`
- **corpus**: regulatory
- **form factor**: patch
- **creator**: U.S. Food and Drug Administration (CDRH); submitter iRhythm Technologies, Inc.
- **disclosure**: U.S. FDA, 510(k) Premarket Notification K113862 (iRhythm Technologies, Inc., 'Zio Patch') — record at accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K113862; a single-use adhesive chest patch recording a single channel of ECG continuously for up to ~14 days for later analysis, cleared as substantially equivalent to predicate ambulatory-ECG (Holter-class) devices. (Followed by a chain of subsequent iRhythm 510(k)s — e.g. K143513, K163512, K181502 — refining the device, the algorithm/ZEUS software, and the Zio AT mobile-cardiac-telemetry variant.)
- **ip status**: regulatory-filing
- **sensors**: sensor-ecg
- **algorithms**: algo-arrhythmia-classification, algo-afib-detection
- **prior art notes**: A public, dated FDA record of a single-use adhesive chest patch that records one channel of ECG continuously for up to ~14 days for later arrhythmia analysis — the modern 'ECG patch' realization of ambulatory ECG ([[holter-1961-ambulatory-ecg]]). Establishes as of ~2011 the public availability of an adhesive long-wear single-lead ECG patch with downstream automated arrhythmia analysis; and, as a 510(k), it cites a predicate chain back to earlier ambulatory-ECG devices — that chain is itself prior art. Prior art for ECG-patch claims; product-side and regulatory anchor for the patch × ECG cross-cut. Cf. [[apple-watch-series4-ecg-2018]] (the wrist single-lead route).

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

## Hexoskin smart shirt (2014) — textile-integrated ECG, respiration and activity garment (2013)

- **id**: `hexoskin-smart-shirt-2014`
- **corpus**: private
- **form factor**: garment
- **creator**: Carre Technologies Inc.
- **disclosure**: Carre Technologies Inc. (Hexoskin). 'Hexoskin Smart Shirt', introduced 2013 (consumer); a compression shirt with knitted dry textile electrodes for single-lead ECG, two-channel respiratory inductive plethysmography (thoracic + abdominal expansion), a 3-axis accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate/volume, cadence, steps, and sleep. (Used in NASA/CSA 'Astroskin' studies.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a consumer/research compression shirt with textile-integrated dry ECG electrodes, two-channel respiratory inductive plethysmography (thoracic + abdominal), an accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate and volume, activity, and sleep. A commercial realization of [[paradiso-2005-wealthy-knitted-smart-shirt]]; anticipates smart-shirt claims combining 'textile-integrated ECG and respiration sensors' and 'a detachable electronics module' from 2013. Product-side anchor for the garment × textile-electrode cross-cut.

## Pacific Rim — Jaeger 'Drivesuit' and 'Conn-Pod' dual-pilot neural bridge (2013-07-12)

- **id**: `pacific-rim-drivesuit-and-conn-pod`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Guillermo del Toro / Legendary Pictures
- **disclosure**: Pacific Rim (Warner Bros. / Legendary), released 12 July 2013; pilots wear a 'Drivesuit' (a body suit capturing motion and monitoring vitals) and a 'relay-gel'/spinal-clamp helmet that creates a shared neural bridge ('the Drift') between two co-pilots and the mecha.
- **ip status**: fictional
- **sensors**: sensor-ecg, sensor-dry-eeg-electrode, sensor-accelerometer
- **algorithms**: algo-hr
- **prior art notes**: Discloses an instrumented pilot suit (motion capture + vital-sign monitoring) combined with head/spine-worn relays that establish a shared neural bridge between two operators and a controlled machine. Relevant to multi-operator neural-interface claims and to instrumented-bodysuit claims combining 'a motion-capturing garment', 'vital-sign monitoring', and 'a head/spine neural relay linking multiple operators'. § 103 motivation as of 2013. Cf. [[nge-plug-suit-and-a10-clips]] (single-pilot), [[surrogates-neural-teleoperation-rig]].

## OpenBCI Cyton — open-source 8-channel biosignal (EEG/EMG/ECG) acquisition board and 3D-printed headset (2014-01-22)

- **id**: `openbci-cyton-2014`
- **corpus**: open
- **form factor**: cap
- **creator**: Joel Murphy / Conor Russomanno (OpenBCI)
- **disclosure**: OpenBCI (Joel Murphy, Conor Russomanno). 'OpenBCI: An Open Source Brain-Computer Interface For Makers.' Kickstarter campaign launched 22 January 2014; hardware designs and firmware released open source at github.com/OpenBCI (Cyton board, Ganglion board, Ultracortex Mark IV 3D-printed headset).
- **ip status**: open-permissive
- **sensors**: sensor-saline-eeg-electrode, sensor-dry-eeg-electrode, sensor-emg, sensor-ecg
- **algorithms**: algo-bci-p300, algo-bci-ssvep, algo-bci-motor-imagery
- **prior art notes**: An openly-published, openly-licensed wearable biosignal acquisition system: a multi-channel ADS1299-based board, electrodes, and a 3D-printed head-worn frame for EEG/EMG/ECG, with reference firmware and BCI demonstrations. As open-hardware prior art it is unencumbered: any claim reciting a multi-channel head-worn biopotential acquisition device with the features published here (since 2014) reads on OpenBCI. Anchors the `open` bucket for biosignal wearables; relevant to headband/cap EEG and to EMG/ECG wearable claims.

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

## VitalConnect VitalPatch (2016) — adhesive chest patch with single-lead ECG and multi-parameter monitoring (2016)

- **id**: `vitalconnect-vitalpatch-2016`
- **corpus**: private
- **form factor**: patch
- **creator**: VitalConnect, Inc.
- **disclosure**: VitalConnect, Inc. 'VitalPatch' biosensor, FDA-cleared as a single-use adhesive chest patch with single-lead ECG, heart rate, heart-rate variability, respiratory rate, skin temperature, posture, activity, and fall detection, streamed wirelessly to a smartphone/relay; 7-day wear (later 14-day variants).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-arrhythmia-classification
- **prior art notes**: Discloses a single-use adhesive chest patch deriving single-lead ECG, HR, HRV, respiratory rate, skin temperature, posture, activity, and falls in one body-worn unit, streamed wirelessly — i.e. a packed multi-parameter vital-signs patch. Anticipates multi-parameter ECG-patch claims combining any subset of those measurements in one adhesive form factor from 2016. Product-side anchor for the patch × multi-parameter-vitals cross-cut alongside [[fda-k113862-irhythm-zio-patch-2011]] (the AFib-focused variant).

## Polar H10 (2017) — research-grade chest-strap ECG heart-rate sensor (2017-01)

- **id**: `polar-h10-chest-strap-2017`
- **corpus**: private
- **form factor**: garment
- **creator**: Polar Electro Oy
- **disclosure**: Polar Electro Oy. 'Polar H10' chest heart-rate sensor, released 2017 — a chest strap with two dry electrodes deriving a single-lead ECG, computing R-R intervals and heart rate, with onboard 1-session memory, dual-broadcast (BLE + ANT+ + 5 kHz GymLink), an accelerometer (relative orientation), and well-documented R-R-interval accuracy (often used as a gold-standard reference for consumer wearables).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-arrhythmia-classification
- **prior art notes**: Discloses a chest strap with two dry electrodes deriving single-lead ECG, with on-strap R-R-interval computation, multi-protocol broadcast (BLE + ANT+ + the 5 kHz GymLink legacy band), and accelerometer-assisted noise rejection. Anticipates chest-strap-ECG claims combining 'dry textile/elastic chest electrodes', 'on-strap derivation of R-R intervals and HR', and 'multi-protocol simultaneous wireless broadcast' from 2017. Product-side anchor for the garment/patch × ECG strap cross-cut; refines [[polar-sport-tester-pe2000-1982]].

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.

## FDA De Novo DEN180044 (2018) — over-the-counter electrocardiograph software for use in detecting atrial fibrillation (Apple Watch ECG app) (2018-09-11)

- **id**: `fda-den180044-apple-watch-ecg-app-2018`
- **corpus**: regulatory
- **form factor**: watch
- **creator**: U.S. Food and Drug Administration (CDRH); requester Apple Inc.
- **disclosure**: U.S. FDA, De Novo Classification Request DEN180044 (Apple Inc., 'ECG App'), granted 11 September 2018 — decision summary at accessdata.fda.gov/cdrh_docs/reviews/DEN180044.pdf; established a new FDA device classification for over-the-counter electrocardiograph software intended to acquire, store, transfer and display a single-lead (Lead I) ECG and to provide a rhythm classification (AFib vs. sinus rhythm) on a consumer wrist-worn platform, with general/special controls.
- **ip status**: regulatory-filing
- **sensors**: sensor-ecg
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification
- **prior art notes**: A public, dated FDA decision describing — and creating the device class for — over-the-counter single-lead ECG software on a consumer wrist-worn device with on-device AFib-vs-sinus classification. As a government disclosure it establishes, as of 11 September 2018, the public availability of the device described: a wristworn Lead-I ECG with consumer-facing rhythm classification. Useful prior art for later claims to that combination; the De Novo decision summary also enumerates the clinical validation and the bench/algorithm characteristics, which are themselves citable. Pairs with the product entry [[apple-watch-series4-ecg-2018]] and the standard [[ieee-11073-10406-basic-ecg-2011]].

## Apple Watch Series 4 (2018) — wrist single-lead ECG and PPG-based irregular-rhythm notification (2018-09-12)

- **id**: `apple-watch-series4-ecg-2018`
- **corpus**: private
- **form factor**: watch
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. 'Apple Watch Series 4', announced 12 September 2018 (ECG app and irregular rhythm notification feature enabled later in 2018) — a wristworn device taking a single-lead (Lead I) ECG between a back-crystal electrode and a Digital Crown electrode touched by the opposite hand, with on-device AF/sinus classification, plus a PPG-based irregular-rhythm (possible-AF) notification algorithm. FDA cleared via De Novo (ECG app: DEN180044; irregular rhythm notification: DEN180042).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-ppg
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-hr
- **prior art notes**: Discloses a wristworn device that records a single-lead ECG between a watch-back electrode and a crown electrode touched by the contralateral hand, classifies the rhythm (AF vs. sinus) on-device, and separately runs a PPG-based background algorithm flagging possible atrial fibrillation. Anticipates wristworn-ECG and watch-AF-detection claims postdating September 2018; the underlying single-lead ECG and PPG-rhythm-screening techniques are much older ([[einthoven-1903-string-galvanometer-ecg]], [[holter-1961-ambulatory-ecg]], [[allen-2007-ppg-review]], [[ieee-11073-10406-basic-ecg-2011]]). Product-side anchor for the watch × ECG and watch × PPG × AF-detection cross-cuts.

## BioIntelliSense BioSticker (2019) — long-wear adhesive chest patch with extensive multi-parameter monitoring (2019-12)

- **id**: `biointellisense-biosticker-2019`
- **corpus**: private
- **form factor**: patch
- **creator**: BioIntelliSense, Inc.
- **disclosure**: BioIntelliSense, Inc. 'BioSticker' single-use adhesive medical-grade biosensor, FDA-cleared 2019 — a chest patch with up to 30-day wear continuously measuring skin temperature, single-lead ECG-derived heart rate at rest, respiratory rate at rest, body position, activity (steps, cadence, gait), sleep, cough, vomiting events, and falls, with wireless upload.
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature, sensor-microphone-air
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-cough-detection, algo-gait-analysis, algo-sleep-staging
- **prior art notes**: Discloses a single-use 30-day adhesive chest patch combining skin temperature, resting HR-from-ECG, resting RR, posture/activity, sleep, cough and vomiting event detection, and falls — i.e. an unusually broad multi-parameter long-wear patch with explicit event-detection (cough, vomit) classifiers. Anticipates long-wear multi-parameter patch claims from 2019, including the event-detection (cough/vomit) elements that some later patents recite. Product-side anchor for the patch × long-wear multi-parameter cross-cut.

## Withings ScanWatch (2020) — hybrid analog watch with PPG, SpO2 pulse oximetry, single-lead ECG, and accelerometer (2020-01-05)

- **id**: `withings-scanwatch-2020`
- **corpus**: private
- **form factor**: watch
- **creator**: Withings SA
- **disclosure**: Withings (Nokia/Withings). 'ScanWatch', announced January 2020 (CE-marked 2020; FDA cleared 2022) — a hybrid analog wristwatch integrating a reflectance-PPG sensor (heart rate, irregular-rhythm screening), an SpO2 (pulse-oximetry) measurement, a single-lead ECG (back electrode plus a bezel electrode touched by the opposite hand, with AF detection), a 3-axis accelerometer, and an altimeter — with sleep and activity tracking.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-ecg, sensor-accelerometer, sensor-barometer
- **algorithms**: algo-hr, algo-spo2-estimation, algo-afib-detection, algo-arrhythmia-classification, algo-sleep-staging, algo-step-count, algo-respiratory-rate
- **prior art notes**: Discloses a wristwatch combining reflectance-PPG heart rate, pulse-oximetry SpO2, a single-lead ECG with AF detection, accelerometry, and an altimeter, with sleep-apnea screening (from the SpO2/respiration signals) — multiple regulated cardiorespiratory measurements in one consumer watch. Anticipates multi-modal medical-smartwatch claims reciting combinations of wrist PPG-HR + wrist SpO2 + single-lead ECG from 2020. Product-side anchor for the watch × {PPG, SpO2, ECG} multi-sensor cross-cut.

## Samsung Galaxy Watch3 / Samsung Health Monitor (2020) — wrist single-lead ECG and optical-PPG cuffless blood pressure (2020-08)

- **id**: `samsung-galaxy-watch-bp-ecg-2020`
- **corpus**: private
- **form factor**: watch
- **creator**: Samsung Electronics Co., Ltd.
- **disclosure**: Samsung Electronics. 'Samsung Health Monitor' app on Galaxy Watch3 / Watch Active2, 2020 — wrist single-lead ECG (between a back-crystal electrode and a side-button electrode touched by the opposite hand, with AF/sinus classification) and a cuffless blood-pressure feature using the optical (PPG) pulse-wave signal calibrated against a periodic conventional cuff reading. (Cleared in Korea 2020; subsequently in other markets.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-pwv-bp-estimation, algo-hr
- **prior art notes**: Discloses a wristworn device that takes a single-lead ECG with on-device AF classification and, separately, estimates blood pressure from the wrist optical-PPG pulse waveform after calibration against a periodic conventional cuff measurement (a calibrated-cuffless approach). Anticipates wrist-cuffless-BP claims reciting 'estimating blood pressure from a wrist photoplethysmography signal calibrated by a reference cuff reading' from 2020 — the underlying PTT/PWV-BP technique is much older ([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the watch × cuffless-BP cross-cut.

## HealthyPi Move (ProtoCentral, 2026) — open-source medical-grade smartwatch (2024)

- **id**: `healthypi-move-2026`
- **corpus**: open
- **form factor**: watch
- **creator**: ProtoCentral Electronics
- **disclosure**: ProtoCentral Electronics (Bengaluru, India). 'HealthyPi Move' fully open-source AMOLED smartwatch — Crowd Supply campaign launched 2024, units shipping 15 May 2026. Sensors: single-lead ECG, dual-site PPG (wrist + finger), SpO2, blood-pressure trending, EDA/GSR, heart rate, HRV, respiration rate (derived), body temperature, 6-axis IMU. Compute: Nordic nRF5340 (dual ARM Cortex-M33). Display: AMOLED, 300 mAh battery. Companion app: Flutter, runs on Android/iOS/macOS/Windows/Linux, all data stored locally. Hardware design, firmware (Zephyr RTOS on nRF Connect SDK), and companion app all open-source. https://www.crowdsupply.com/protocentral/healthypi-move
- **ip status**: open-permissive
- **sensors**: sensor-ecg, sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg, sensor-gsr, sensor-accelerometer, sensor-gyroscope, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-spo2-estimation, algo-respiratory-rate, algo-pwv-bp-estimation, algo-sleep-staging, algo-activity-classification, algo-step-count
- **prior art notes**: Discloses, as fully open-source hardware and firmware (CC and MIT-style licensing across components), a wrist-worn smartwatch with the full consumer-medical sensor stack: single-lead ECG between back-of-watch electrode and a finger-touch electrode; multi-wavelength reflectance PPG with SpO2 and BP-trending; EDA/GSR; skin temperature; 6-axis IMU; on-device Zephyr-RTOS application; AMOLED display; all-local data storage via cross-platform Flutter app. Anticipates wrist-multi-sensor-watch claims from 2024-2026 to the extent they recite combinations of these elements; as `open` prior art it is unencumbered and any patent claim reciting these combinations must distinguish over HealthyPi Move's specific implementation. The product-side anchor for the 'open watch with the full sensor stack' cross-cut.
