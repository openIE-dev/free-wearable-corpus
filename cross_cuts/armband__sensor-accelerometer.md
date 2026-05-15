---
title: armband ∩ sensor-accelerometer
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `armband` ∩ `sensor-accelerometer`

Axes: **form_factor × sensors**

**3 corpus entries disclose both tags.**

Earliest disclosure: 2012-04-20

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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

## Thalmic Labs Myo armband (2014) — consumer surface-EMG gesture-control armband (2013-02-25)

- **id**: `myo-armband-2014`
- **corpus**: private
- **form factor**: armband
- **creator**: Thalmic Labs Inc. (later North)
- **disclosure**: Thalmic Labs Inc. 'Myo gesture control armband', announced February 2013, shipped 2014 — a forearm-worn band of eight medical-grade stainless-steel surface-EMG electrode segments plus a 9-axis IMU, recognizing hand and finger gestures from the forearm-muscle electrical activity and arm orientation/motion, and transmitting them over Bluetooth as input to computers/devices.
- **ip status**: patented
- **sensors**: sensor-emg, sensor-accelerometer, sensor-gyroscope, sensor-magnetometer
- **algorithms**: algo-hand-gesture-emg, algo-keystroke-emg
- **prior art notes**: Discloses a forearm-worn band with an array of eight surface-EMG electrodes plus a 9-axis IMU that recognizes hand/finger gestures from forearm-muscle EMG combined with arm motion/orientation and transmits them wirelessly as a control input. A consumer realization of the myoelectric pattern-recognition approach ([[englehart-hudgins-2003-myoelectric-control]]); anticipates EMG-gesture-armband claims combining 'a band of surface-EMG electrodes worn around the forearm', 'an inertial sensor', and 'a classifier mapping the combined signal to a hand gesture / control command' from 2014. Product-side anchor for the armband × EMG cross-cut (the only `armband` form-factor entry besides [[mass-effect-omni-tool]] and [[fallout-pip-boy]]).

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
