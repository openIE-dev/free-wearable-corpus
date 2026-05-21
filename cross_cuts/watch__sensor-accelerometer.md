---
title: watch ∩ sensor-accelerometer
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `watch` ∩ `sensor-accelerometer`

Axes: **form_factor × sensors**

**23 corpus entries disclose both tags.**

Earliest disclosure: 1992

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Cole & Kripke et al. (1992) — automatic sleep/wake identification from wrist activity (the Cole-Kripke algorithm) (1992)

- **id**: `cole-kripke-1992-wrist-actigraphy-sleep`
- **corpus**: academic
- **form factor**: watch
- **creator**: Roger J. Cole / Daniel F. Kripke et al.
- **disclosure**: Cole RJ, Kripke DF, Gruen W, Mullaney DJ, Gillin JC. 'Automatic sleep/wake identification from wrist activity.' Sleep 1992;15(5):461-469.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer
- **algorithms**: algo-sleep-staging, algo-activity-classification
- **prior art notes**: Discloses an algorithm that classifies each epoch as sleep or wake from a wrist-worn activity (accelerometer) recording, validated against polysomnography — i.e. wrist actigraphy as a wearable sleep monitor. Any consumer-wearable claim reciting 'estimating sleep/wake state from a wrist-worn accelerometer signal' (the method underlying Fitbit/Jawbone-class sleep tracking) reads on Cole-Kripke 1992. Anchor for the accelerometry sleep-staging cross-cut; combined with the wrist form factor it makes wristworn sleep tracking obvious under [[obviousness-template]].

## Sadeh et al. (1994) — activity-based sleep-wake identification (the Sadeh algorithm) (1994)

- **id**: `sadeh-1994-actigraphy-sleep-wake-algorithm`
- **corpus**: academic
- **form factor**: watch
- **creator**: Avi Sadeh / Katherine M. Sharkey / Mary A. Carskadon
- **disclosure**: Sadeh A, Sharkey KM, Carskadon MA. 'Activity-based sleep-wake identification: an empirical test of methodological issues.' Sleep 1994;17(3):201-207.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer
- **algorithms**: algo-sleep-staging, algo-activity-classification
- **prior art notes**: A second widely-used wrist-actigraphy sleep/wake scoring algorithm, with explicit treatment of the methodological choices (epoch length, scoring window, scaling). Prior art alongside [[cole-kripke-1992-wrist-actigraphy-sleep]] for any wearable claim reciting an actigraphy-based sleep-detection method or its parameters; both were published and validated by 1994.

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

## Ancoli-Israel et al. (2003) — 'The role of actigraphy in the study of sleep and circadian rhythms' (2003-05)

- **id**: `ancoli-israel-2003-actigraphy-review`
- **corpus**: academic
- **form factor**: watch
- **creator**: Sonia Ancoli-Israel et al. (American Academy of Sleep Medicine review)
- **disclosure**: Ancoli-Israel S, Cole R, Alessi C, Chambers M, Moorcroft W, Pollak CP. 'The role of actigraphy in the study of sleep and circadian rhythms.' Sleep 2003;26(3):342-392.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer
- **algorithms**: algo-sleep-staging
- **prior art notes**: Authoritative review establishing wrist actigraphy — a wrist-worn accelerometer/activity recorder analyzed by validated algorithms — as an accepted method for estimating sleep parameters and circadian rhythm. Prior art for the proposition that a wrist-worn motion sensor with appropriate scoring yields clinically meaningful sleep metrics; the field, methods, and validation were settled and reviewed by 2003.

- **Pokémon — 'Pokétch' wrist device with an app ecosystem** (2006-09-28) — `pokemon-poketch` [fictional] — Pokémon Diamond and Pearl (Nintendo / Game Freak, 2006); the 'Pokétch' — a wrist-worn touchscreen device hosting an extensible set of small applications (clock, calculator, step counter, map, friendsh…
## Fitbit Tracker (2009) — clip-on accelerometer activity and sleep monitor (2009-10)

- **id**: `fitbit-tracker-2009`
- **corpus**: private
- **form factor**: pendant
- **creator**: Fitbit, Inc. (James Park, Eric Friedman)
- **disclosure**: Fitbit, Inc. 'Fitbit Tracker', launched October 2009 — a clip-worn device with a 3-axis accelerometer estimating steps, distance, calories burned, active minutes, and sleep quality, syncing wirelessly to a web dashboard. (The wrist PPG heart-rate variant, Fitbit Charge HR, followed in January 2015.)
- **ip status**: patented
- **sensors**: sensor-accelerometer
- **algorithms**: algo-step-count, algo-calorie-estimation, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a small body-worn (clip) device with a 3-axis accelerometer that estimates step count, distance, calories, active minutes, and sleep quality on-device and syncs wirelessly to a cloud dashboard. Anticipates consumer-activity-tracker claims combining 'a body-worn accelerometer', 'on-device estimation of steps/calories/activity/sleep', and 'wireless sync to a remote service' from 2009. Anchor for the step-count and consumer-sleep-tracking cross-cuts on the product side.

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

## FDA 510(k) K181861 (2018) — Empatica Embrace physiological-signal-based seizure monitoring system (2018)

- **id**: `fda-k181861-empatica-embrace-seizure-system-2018`
- **corpus**: regulatory
- **form factor**: watch
- **creator**: U.S. Food and Drug Administration (CDRH); submitter Empatica Inc.
- **disclosure**: U.S. FDA, 510(k) Premarket Notification K181861 (Empatica Inc., 'Embrace' physiological-signal-based seizure monitoring system) — a wrist-worn device using accelerometry plus electrodermal activity to detect probable generalized tonic-clonic seizures and alert caregivers; reported as the first FDA-cleared smartwatch indicated for use in neurology (clearance announced February 2018). (Verify which Embrace generation K181861 maps to; the original clearance may carry a different K-number.)
- **ip status**: regulatory-filing
- **sensors**: sensor-accelerometer, sensor-gsr
- **algorithms**: algo-seizure-detection
- **prior art notes**: A public, dated FDA record of a wrist-worn device detecting probable generalized tonic-clonic seizures from combined accelerometry and electrodermal activity, with caregiver alerting — the non-EEG route to wearable seizure detection. Establishes the public availability of that device as of 2018; the 510(k) cites a predicate chain that is itself prior art. Prior art for wrist-based seizure-detection claims using motion + EDA; regulatory anchor pairing with [[empatica-embrace2-seizure-watch-2018]] (the EEG route is anchored separately by [[zanetti-aminifar-atienza-eglass-2025]] and [[chb-mit-scalp-eeg-database-2009]]).

## Empatica Embrace2 (2018) — first FDA-cleared seizure-monitoring smartwatch (accelerometer + electrodermal activity) (2018-01-31)

- **id**: `empatica-embrace2-seizure-watch-2018`
- **corpus**: private
- **form factor**: watch
- **creator**: Empatica Inc. (Rosalind Picard, Matteo Lai, et al.)
- **disclosure**: Empatica Inc. 'Embrace2' smartwatch, FDA-cleared January 2018 — a wrist-worn device with a 3-axis accelerometer/gyroscope, an electrodermal-activity (EDA) sensor, and a peripheral skin-temperature sensor, running an on-device classifier that detects probable generalized tonic-clonic seizures from the combined motion + EDA signature and alerts caregivers; the first FDA-cleared smartwatch for seizure monitoring. (Descends from the MIT Media Lab 'iCalm'/'Q sensor' EDA wristband research, Picard et al.)
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-gsr, sensor-skin-temperature
- **algorithms**: algo-seizure-detection, algo-stress-index, algo-activity-classification
- **prior art notes**: Discloses a wristworn device that detects probable generalized tonic-clonic seizures by combining a motion (accelerometer/gyroscope) signature with an electrodermal-activity (sympathetic-surge) signature in an on-device classifier, and alerts caregivers — i.e. multimodal wrist-based seizure detection, distinct from the EEG-based approach. Anticipates wrist-seizure-detection claims combining 'a wrist-worn accelerometer and an electrodermal-activity sensor' and 'a classifier flagging a seizure from their combined signal' from 2018. Product-side anchor for the wrist × seizure-detection cross-cut; complementary to the EEG route in [[zanetti-aminifar-atienza-eglass-2025]] and [[chb-mit-scalp-eeg-database-2009]].

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
