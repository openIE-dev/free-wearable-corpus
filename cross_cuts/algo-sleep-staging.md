---
title: algo-sleep-staging
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-sleep-staging`

Axis: **algorithms**

**21 corpus entries disclose this tag.**

Earliest disclosure: 1953-09-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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
