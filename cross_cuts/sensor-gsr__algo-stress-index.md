---
title: sensor-gsr ∩ algo-stress-index
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-gsr` ∩ `algo-stress-index`

Axes: **sensors × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 2014-10-30

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
