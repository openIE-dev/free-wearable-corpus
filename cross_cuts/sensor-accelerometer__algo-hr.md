---
title: sensor-accelerometer ∩ algo-hr
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-accelerometer` ∩ `algo-hr`

Axes: **sensors × algorithms**

**31 corpus entries disclose both tags.**

Earliest disclosure: 2001-07

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## MIT wearable ring sensor (Rhee, Yang, Asada) — finger-ring PPG for ambulatory monitoring (2001-07)

- **id**: `asada-mit-wearable-ring-sensor-2003`
- **corpus**: academic
- **form factor**: ring
- **creator**: Sokwoo Rhee / Boo-Ho Yang / Haruhiko Harry Asada (MIT d'Arbeloff Lab)
- **disclosure**: Rhee S, Yang B-H, Asada HH. 'Artifact-resistant power-efficient design of finger-ring plethysmographic sensors.' IEEE Transactions on Biomedical Engineering 2001;48(7):795-805 (and Asada HH, Shaltis P, Reisner A, Rhee S, Hutchinson RC. 'Mobile monitoring with wearable photoplethysmographic biosensors.' IEEE Engineering in Medicine and Biology Magazine 2003;22(3):28-40).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer
- **algorithms**: algo-hr, algo-spo2-estimation
- **prior art notes**: Discloses a finger-ring-form-factor wearable PPG sensor with motion-artifact-resistant optical/mechanical design, low-power operation, on-body processing, and wireless telemetry of heart rate and SpO2 for ambulatory monitoring — i.e. the smart-ring physiological monitor, ~14 years before the commercial smart-ring wave. Directly anticipates ring-form claims combining 'a ring body', 'a PPG emitter/detector at the inner ring surface', 'motion-artifact compensation', and 'wireless transmission of derived vitals'. Anchor for the ring × PPG cross-cut; [[oura-ring-gen1-2015]] and similar products descend from it.

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

## Iron Man helmet HUD with biometric monitoring (2008-05-02)

- **id**: `iron-man-helmet-hud`
- **corpus**: fictional
- **form factor**: helmet
- **creator**: Marvel Studios
- **disclosure**: Iron Man (Marvel Studios / Paramount), released May 2, 2008; the suit helmet's interior HUD presenting wearer vitals, environmental/tactical data, and a conversational voice AI (JARVIS). (Armor concept originates Tales of Suspense #39, Marvel Comics, March 1963.)
- **ip status**: fictional
- **sensors**: sensor-accelerometer
- **algorithms**: algo-hr, algo-respiratory-rate
- **prior art notes**: Discloses a helmet whose interior near-eye display continuously presents the wearer's physiological state (HR, respiration, O2, fatigue) alongside environmental/tactical overlays, mediated by a hands-free conversational voice assistant. Relevant to helmet- and headgear-integrated biometric-monitoring claims combining 'sensors disposed to contact the wearer', 'a head-mounted display presenting physiological metrics', and 'a voice interface'. § 103 motivation that the vitals-in-the-helmet-HUD concept was an articulated objective by 2008 (and the broader powered-helmet-display lineage by 1963).

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

## The Circle — 'SeeChange' wearable cameras and employee health wristbands (2013-10-08)

- **id**: `the-circle-seechange-and-health-wristbands`
- **corpus**: fictional
- **form factor**: bracelet
- **creator**: Dave Eggers
- **disclosure**: Eggers, Dave. The Circle. Alfred A. Knopf, 2013 (film adaptation 2017); 'SeeChange' miniature wearable/mountable cameras streaming continuously, and employee wristbands (worn in pairs on each wrist) that continuously monitor heart rate, activity, sleep, and other physiological data and upload it to the company.
- **ip status**: fictional
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-camera-rgb
- **algorithms**: algo-hr, algo-step-count, algo-sleep-staging
- **prior art notes**: Discloses (a) continuously-worn wristbands with PPG and motion sensing that stream heart rate, activity, and sleep data to an employer, and (b) tiny body-wearable always-streaming cameras. Relevant to workplace-wellness wearable claims combining 'a wrist-worn PPG/motion sensor', 'continuous physiological streaming to a remote/employer system', and to body-worn-camera streaming claims. § 103 motivation that the employer-monitored wrist wearable and the always-streaming wearable camera were articulated objectives by 2013.

## Bragi Dash (2014) — the first true 'hearable': in-ear PPG heart rate, accelerometer, storage and touch control inside wireless earbuds (2014-02-25)

- **id**: `bragi-dash-2014`
- **corpus**: private
- **form factor**: earbud
- **creator**: Bragi GmbH
- **disclosure**: Bragi GmbH. 'The Dash' wireless smart earphones, crowdfunded February 2014 (shipped 2016) — fully wireless in-ear earbuds with a reflectance-PPG heart-rate sensor and oxygen-saturation estimation against the ear-canal wall, a 3-axis accelerometer (head-gesture and step/activity tracking), 4 GB onboard music storage, bone-conduction microphone, and capacitive touch control.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-microphone-bone
- **algorithms**: algo-hr, algo-spo2-estimation, algo-step-count, algo-activity-classification
- **prior art notes**: Discloses fully-wireless in-ear earbuds with a reflectance-PPG heart-rate and SpO2 sensor against the ear-canal wall, an accelerometer for head-gesture and step/activity tracking, onboard music storage, a bone-conduction microphone, and capacitive touch control — i.e. physiological sensing integrated into wireless earbuds. Anticipates hearable claims combining 'a wireless earbud housing', 'an in-ear PPG/SpO2 sensor', 'an accelerometer for activity or head gesture', and 'on-device media and controls' from 2014. Product-side anchor for the earbud × PPG cross-cut.

## Inan et al. (2015) — ballistocardiography and seismocardiography review (2014-10-07)

- **id**: `inan-2015-bcg-scg-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Omer T. Inan et al.
- **disclosure**: Inan OT, Migeotte P-F, Park K-S, Etemadi M, Tavakolian K, Casanella R, Zanetti J, Tank J, Funtova I, Prisk GK, Di Rienzo M. 'Ballistocardiography and seismocardiography: a review of recent advances.' IEEE Journal of Biomedical and Health Informatics 2015;19(4):1414-1427.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer, sensor-piezoelectric
- **algorithms**: algo-hr, algo-hrv, algo-pwv-bp-estimation
- **prior art notes**: Reviews ballistocardiography (whole-body reaction force from cardiac ejection, measured at the seat/scale/bed) and seismocardiography (local chest vibration from cardiac motion, measured by accelerometers on the sternum) and their integration into bathroom scales, weighing chairs, beds, and chest patches — i.e. the mechanical-cardiac-signal route to heart rate, HRV, and cardiac-timing-interval / stroke-volume estimation. Prior art for claims reciting 'measuring cardiac activity from a body-worn or support-mounted accelerometer/force sensor', as both the BCG and SCG approaches and their wearable instantiations were collected and reviewed by 2015. Anchor for the BCG/SCG cross-cut.

## Microsoft Band (2014) — ten-sensor wristband (optical HR, GPS, GSR, UV, skin temp, barometer, ambient light, capacitive, microphone, IMU) (2014-10-30)

- **id**: `microsoft-band-2014`
- **corpus**: private
- **form factor**: watch
- **creator**: Microsoft Corp.
- **disclosure**: Microsoft Corp. 'Microsoft Band', released 30 October 2014 — a wristband integrating ten sensors: an optical (PPG) heart-rate sensor, a 3-axis accelerometer/gyroscope, GPS, an ambient-light sensor, a skin-temperature sensor, a UV sensor, a capacitive (wear-detection) sensor, a galvanic-skin-response sensor, a microphone, and a barometer (added in Band 2).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-gyroscope, sensor-skin-temperature, sensor-uv, sensor-gsr, sensor-barometer, sensor-photodiode-ambient, sensor-microphone-air
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-sleep-staging, algo-stress-index, algo-uv-dose-tracking
- **prior art notes**: Discloses a single wristband integrating an unusually broad sensor suite — reflectance-PPG HR, IMU, GPS, skin temperature, UV exposure, galvanic skin response (electrodermal activity), barometer, ambient light, capacitive wear-detection, and a microphone — feeding HR, activity, sleep, UV dose, and stress-index estimations. Prior art for multi-sensor-wristband claims reciting combinations of these sensors (notably wrist GSR/EDA + PPG + skin temperature for stress) from October 2014. Product-side anchor for the multi-sensor wristband cross-cut.

## WHOOP Strap (2015) — display-less wrist/bicep PPG band for continuous HR/HRV, sleep and recovery (2015)

- **id**: `whoop-strap-2015`
- **corpus**: private
- **form factor**: bracelet
- **creator**: WHOOP, Inc. (Will Ahmed)
- **disclosure**: WHOOP, Inc. 'WHOOP Strap', launched 2015 — a screenless band worn on the wrist or upper arm with photoplethysmography, a 3-axis accelerometer, and skin-temperature sensing, providing continuous heart rate, heart-rate variability, respiratory rate, sleep staging, and a derived 'recovery' score, with no on-device display.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging, algo-activity-classification
- **prior art notes**: Discloses a display-less band worn on the wrist or upper arm with PPG, accelerometry, and skin-temperature sensing that continuously derives HR, HRV, respiratory rate, and sleep stages and combines them into a daily 'recovery' index, with no screen (companion-app readout). Anticipates screenless-band claims and PPG-derived-HRV/recovery-score claims from 2015. Product-side anchor for the bracelet × PPG cross-cut and the HRV cross-cut.

## Fitbit Charge HR (2015) — wristband with continuous wrist-PPG heart rate ('PurePulse') (2015-01-06)

- **id**: `fitbit-charge-hr-2015`
- **corpus**: private
- **form factor**: watch
- **creator**: Fitbit, Inc.
- **disclosure**: Fitbit, Inc. 'Fitbit Charge HR', announced January 2015 — a wristband with 'PurePulse' continuous optical (green-LED PPG) heart rate, a 3-axis accelerometer, steps/distance/floors/calories/active-minutes, automatic sleep tracking, and call/text notifications.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-barometer
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a wristband with continuous green-LED reflectance-PPG heart rate plus accelerometry and an altimeter, deriving HR, steps, floors, calories, and sleep, with phone notifications. A mainstream realization of [[mendelson-ochs-1988-reflectance-pulse-oximetry]]-geometry wrist PPG; anticipates wrist-PPG-HR-band claims from January 2015. Product-side anchor for the watch × PPG cross-cut alongside [[apple-watch-original-2015]].

## Apple Watch (1st generation, 2015) — wrist green-PPG heart rate and activity (2015-04-24)

- **id**: `apple-watch-original-2015`
- **corpus**: private
- **form factor**: watch
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. 'Apple Watch', announced September 2014, available 24 April 2015 — a wrist-worn device with a green/infrared photoplethysmography heart-rate sensor against the dorsal wrist, accelerometer and gyroscope, and activity/exercise tracking.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-multi-wavelength-ppg, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification
- **prior art notes**: Discloses a wristworn device with a dorsal-wrist green-LED photoplethysmography heart-rate sensor (with IR for low-perfusion conditions), inertial sensors, and continuous HR/activity tracking. Anticipates wristworn-PPG-HR claims to the extent they postdate April 2015; combined with the much earlier PPG principle ([[hertzman-1937-photoplethysmography]]) and wrist form factor, the combination is in any case obvious under [[obviousness-template]]. Product-side anchor for the watch × PPG cross-cut.

## Oura Ring (Gen 1, 2015) — finger-ring PPG, skin-temperature and accelerometer for HRV, sleep and body temperature (2015-08)

- **id**: `oura-ring-gen1-2015`
- **corpus**: private
- **form factor**: ring
- **creator**: Oura Health Oy
- **disclosure**: Oura Health Oy. 'Oura Ring' (1st generation), crowdfunded 2015, shipped 2016 — a titanium finger ring with infrared photoplethysmography, an NTC skin-temperature sensor, and a 3-axis accelerometer, deriving resting heart rate, heart-rate variability, respiratory rate, sleep staging, and body-temperature trend.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging
- **prior art notes**: Discloses a finger-ring wearable with infrared PPG, a skin-temperature sensor, and an accelerometer, deriving resting HR, HRV, respiratory rate, sleep stages, and a body-temperature trend, with companion-app readout. A commercial realization, ~12-16 years later, of the MIT ring-sensor concept ([[asada-mit-wearable-ring-sensor-2003]]); to the extent later claims recite ring-form PPG + skin-temperature + HRV/sleep, both Asada 2003 and Oura 2015 are prior art. Product-side anchor for the ring × PPG × HRV and ring × skin-temperature cross-cuts.

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

## Pine64 PineTime (2018-2020) — low-cost open-source smartwatch (2018-09)

- **id**: `pine64-pinetime-2020`
- **corpus**: open
- **form factor**: watch
- **creator**: Pine Store Ltd. (Pine64)
- **disclosure**: Pine64. 'PineTime' open-source smartwatch — first announced September 2018, dev-kit shipping early 2020, sealed units (~US$30) shipping from late 2020. Hardware: Nordic nRF52832 (ARM Cortex-M4), heart-rate monitor, 3-axis accelerometer, touchscreen, BLE. Open firmware: 'InfiniTime' (C++/FreeRTOS) at github.com/InfiniTimeOrg/InfiniTime; 'Wasp-OS' (Python/MicroPython) at github.com/daniel-thompson/wasp-os. Hardware schematics at wiki.pine64.org/wiki/PineTime. https://pine64.com/product/pinetime-smartwatch-sealed/
- **ip status**: open-permissive
- **sensors**: sensor-ppg, sensor-accelerometer
- **algorithms**: algo-hr, algo-step-count
- **prior art notes**: Discloses a low-cost (US$30) wrist-worn smartwatch with PPG-HR sensor, accelerometer, touchscreen, BLE, and fully open-source firmware (InfiniTime in C++/FreeRTOS, or Wasp-OS in Python/MicroPython on the same hardware) and published hardware schematics. Establishes (since 2018-2020) that the basic smartwatch architecture — MCU + PPG + accel + display + BLE + open firmware — is unencumbered open-hardware prior art. Distinct from [[healthypi-move-2026]] in being earlier and simpler; together they establish open-watch prior art across a >5-year span.

## Omron HeartGuide (2019) — wristwatch with an inflatable oscillometric blood-pressure cuff in the band (2019-01-08)

- **id**: `omron-heartguide-2019`
- **corpus**: private
- **form factor**: watch
- **creator**: Omron Healthcare Co., Ltd.
- **disclosure**: Omron Healthcare. 'HeartGuide' (model BP8000-M), announced January 2019, FDA-cleared — a wristwatch whose band contains an inflatable cuff and an oscillometric pressure transducer, taking a clinically-validated brachial-style blood-pressure measurement at the wrist on demand, alongside heart rate, steps, and sleep.
- **ip status**: patented
- **sensors**: sensor-pressure-skin, sensor-accelerometer, sensor-ppg
- **algorithms**: algo-hr, algo-step-count, algo-sleep-staging
- **prior art notes**: Discloses a wristwatch whose strap incorporates an inflatable cuff and pressure transducer, performing an oscillometric blood-pressure measurement at the wrist (occlude-and-release, automatically positioned at heart level by the wearer) in a watch form factor, plus activity and sleep tracking. Distinct from cuffless-PPG approaches: it is a true oscillometric cuff miniaturized into a watch band. Anticipates watch-with-integrated-inflatable-cuff BP claims from 2019. Product-side anchor for the watch × oscillometric-BP cross-cut (vs. the cuffless-PPG variant in [[samsung-galaxy-watch-bp-ecg-2020]] and [[aktiia-bracelet-cuffless-bp-2021]]).

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

## Bangle.js 2 (Espruino, 2021) — open JavaScript-app smartwatch validated in academic research (2021)

- **id**: `bangle-js-2-2021`
- **corpus**: open
- **form factor**: watch
- **creator**: Pur3 Ltd. (Gordon Williams, Espruino)
- **disclosure**: Espruino / Pur3 Ltd. 'Bangle.js 2', released 2021 — Nordic nRF52840 (ARM Cortex-M4), GPS, heart rate, 3-axis accelerometer, magnetometer, pressure sensor; 4-week battery life; JavaScript app development with web-based app loader. https://banglejs.com . Validated for step counting and heart-rate measurement in academic research (multi-subject MDPI study).
- **ip status**: open-permissive
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-magnetometer, sensor-barometer
- **algorithms**: algo-hr, algo-step-count, algo-activity-classification
- **prior art notes**: Discloses an open-hardware smartwatch with PPG + IMU + magnetometer + barometer + GPS, web-loaded JavaScript apps, and 4-week battery life — validated against reference devices in peer-reviewed studies for step counting and HR. As open-source hardware released in 2021 it is unencumbered prior art against patents reciting the open-firmware-platform smartwatch with this sensor set.

## Open-Watch (Salar Motlaqolahi, 2021) — fully documented open STM32 smartwatch (BSc thesis) (2021)

- **id**: `smotlaq-open-watch-2021`
- **corpus**: open
- **form factor**: watch
- **creator**: Salar Motlaqolahi
- **disclosure**: Motlaqolahi S. 'Open-Watch' — fully open-source smartwatch released as BSc thesis output (MIT license). Hardware: STM32 ARM Cortex-M MCU, MPU6050 6-axis IMU, MAX30102 reflectance PPG + SpO2, 4-layer PCB sponsored by PCBWay, full schematics + Gerbers + firmware published. https://github.com/SMotlaq/open-watch
- **ip status**: open-permissive
- **sensors**: sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-spo2-estimation, algo-step-count
- **prior art notes**: Discloses, as an MIT-licensed open-hardware smartwatch with full PCB design files (4-layer, PCBWay-sponsored fabrication) and firmware published, a wrist-worn device with reflectance PPG + SpO2 + 6-axis IMU + MCU + display. Demonstrates that the entire smartwatch design — schematic, layout, firmware — can be reproduced from undergraduate-thesis-level public work, defeating any claim that the integrated smartwatch is novel as a combination.

## Aktiia bracelet (2021) — optical-PPG-based continuous cuffless blood-pressure monitoring bracelet (2021-01)

- **id**: `aktiia-bracelet-cuffless-bp-2021`
- **corpus**: private
- **form factor**: bracelet
- **creator**: Aktiia SA
- **disclosure**: Aktiia SA. 'Aktiia bracelet' (later 'Hilo'), CE-marked and launched in Europe January 2021 — a slim wristband with optical photoplethysmography that, after a one-time initialization against a conventional cuff (and periodic re-calibration), estimates systolic and diastolic blood pressure several times a day automatically, day and night, from the wrist PPG pulse waveform.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-cuffless-bp-ptt, sensor-accelerometer
- **algorithms**: algo-pwv-bp-estimation, algo-hr
- **prior art notes**: Discloses a slim wristband that, after a one-time cuff initialization (and periodic re-calibration), automatically estimates systolic and diastolic blood pressure multiple times per day and night purely from the wrist optical-PPG pulse waveform — i.e. continuous, fully cuffless, calibration-initialized wrist BP monitoring. Anticipates continuous-cuffless-wrist-BP claims from 2021; the PPG-pulse-feature-to-BP mapping rests on the much older PTT/PWV-BP and pulse-contour literature ([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the bracelet × cuffless-BP cross-cut.

## Masimo W1 (2022) — first FDA-cleared continuous wrist medical-grade pulse oximetry watch (2022-05)

- **id**: `masimo-w1-2022`
- **corpus**: private
- **form factor**: watch
- **creator**: Masimo Corp.
- **disclosure**: Masimo Corp. 'Masimo W1' health-tracking watch, announced May 2022 — a wrist-worn device performing continuous medical-grade pulse oximetry (SpO2), pulse rate, perfusion index (PI), pleth variability index (PVi), respiratory rate from the PPG, and HRV, using Masimo's SET/rainbow signal-extraction algorithms. (FDA cleared as a continuous-monitoring medical device.)
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg, sensor-accelerometer
- **algorithms**: algo-spo2-estimation, algo-hr, algo-hrv, algo-respiratory-rate
- **prior art notes**: Discloses a wrist-worn device performing continuous medical-grade pulse oximetry — SpO2, PR, perfusion index, PVi, RR-from-PPG, HRV — using established signal-extraction methods, distinguished from consumer spot-check SpO2 by continuous operation and clearance for medical use. Anticipates wrist-continuous-medical-SpO2 claims from 2022; the underlying two-wavelength SpO2 method is much older ([[aoyagi-1974-two-wavelength-pulse-oximetry]], [[mendelson-ochs-1988-reflectance-pulse-oximetry]], [[iso-80601-2-61-pulse-oximeter-equipment-2011]]). Product-side anchor for the watch × continuous-SpO2 cross-cut.

## Ultrahuman Ring AIR (2023) — smart ring with metabolic-focus tracking (PPG, skin temperature, IMU) (2023)

- **id**: `ultrahuman-ring-air-2023`
- **corpus**: private
- **form factor**: ring
- **creator**: Ultrahuman Healthcare Pvt. Ltd.
- **disclosure**: Ultrahuman Healthcare Pvt. Ltd. 'Ultrahuman Ring AIR', launched 2023 — a titanium smart ring with infrared photoplethysmography, IR skin-temperature, and a 6-axis IMU, deriving HR, HRV, skin temperature, sleep staging, activity, and metabolic-health framing (paired with the company's CGM-based metabolism platform).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-hrv, algo-sleep-staging, algo-respiratory-rate
- **prior art notes**: Discloses a smart ring with IR PPG, skin-temperature, and a 6-axis IMU, deriving HR/HRV, sleep, and activity, packaged with a metabolic-health platform (CGM-linked). Product-side reference in the ring × PPG cross-cut alongside [[oura-ring-gen1-2015]] and [[samsung-galaxy-ring-2024]].

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

## H-Watch (Magno et al., 2024) — open-source ARM Cortex-M4F + ML + NB-IoT + energy-harvesting research smartwatch (2024)

- **id**: `h-watch-magno-2024`
- **corpus**: academic
- **form factor**: watch
- **creator**: Michele Magno et al. (ETH Zürich and collaborators)
- **disclosure**: Magno M, et al. 'H-Watch: A Multi-Sensor Smart Wearable for COVID-19 Symptom Monitoring with ML and Energy Harvesting.' arXiv:2407.21501 (2024). Fully open-source smartwatch hardware + firmware for symptom monitoring: ARM Cortex-M4F MCU, on-device ML inference, NB-IoT cellular connectivity, integrated energy harvesting + battery. https://arxiv.org/abs/2407.21501
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-spo2, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-spo2-estimation, algo-respiratory-rate, algo-activity-classification
- **prior art notes**: Discloses a fully open-source research smartwatch combining multi-sensor vitals (PPG/SpO2/temperature/IMU), on-device ML inference, NB-IoT direct cellular connectivity (no phone required), and integrated energy harvesting to extend battery life — published with full hardware design and firmware. Prior art for symptom-monitoring smartwatch claims reciting any of those elements from 2024. Establishes that the cellular-connected open-hardware ML-enabled smartwatch is a published research design.

## CogWatch (HardwareX, 2024) — open-source smartwatch for cognitive-load monitoring (2024)

- **id**: `cogwatch-2024-hardwarex`
- **corpus**: academic
- **form factor**: watch
- **creator**: (See HardwareX publication for full author list.)
- **disclosure**: 'CogWatch: An open-source smartwatch platform for cognitive-load monitoring.' HardwareX 19 (2024). Open-source smartwatch design — full hardware, firmware, and assembly documentation published in the open-hardware-focused journal HardwareX (Elsevier). https://www.hardware-x.com/article/S2468-0672(24)00032-4/fulltext
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-gsr, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-stress-index, algo-cognitive-workload
- **prior art notes**: Discloses, as open-hardware (HardwareX is the canonical venue for full publication of open-hardware designs), a wrist-worn smartwatch instrumented for cognitive-load monitoring from PPG-derived HRV and EDA/GSR. Prior art for smartwatch-cognitive-load claims combining 'a wrist-worn device', 'PPG and EDA sensors', and 'a derived cognitive-load metric' from 2024.

## Samsung Galaxy Ring (2024) — smart ring with PPG, skin temperature and accelerometer for HR/HRV, sleep and cycle tracking (2024-07-10)

- **id**: `samsung-galaxy-ring-2024`
- **corpus**: private
- **form factor**: ring
- **creator**: Samsung Electronics Co., Ltd.
- **disclosure**: Samsung Electronics. 'Samsung Galaxy Ring', announced July 2024 — a finger ring with infrared photoplethysmography, an IR skin-temperature sensor, and a 3-axis accelerometer, deriving heart rate, heart-rate variability, skin temperature, sleep staging, activity, snore detection, and (with cycle-tracking) menstrual-cycle predictions.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging, algo-snore-detection, algo-step-count
- **prior art notes**: Discloses a smart ring with infrared PPG, IR skin-temperature, and accelerometer, deriving HR/HRV, sleep, snore detection, activity, and menstrual-cycle prediction — a Samsung entry directly in the wake of [[oura-ring-gen1-2015]] and the [[asada-mit-wearable-ring-sensor-2003]] academic root. Product-side reference in the ring × PPG × HRV cross-cut alongside Oura.
