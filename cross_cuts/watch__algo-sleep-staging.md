---
title: watch ∩ algo-sleep-staging
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `watch` ∩ `algo-sleep-staging`

Axes: **form_factor × algorithms**

**8 corpus entries disclose both tags.**

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
