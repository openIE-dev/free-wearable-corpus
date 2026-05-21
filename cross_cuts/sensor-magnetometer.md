---
title: sensor-magnetometer
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-magnetometer`

Axis: **sensors**

**3 corpus entries disclose this tag.**

Earliest disclosure: 2013-02-25

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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

## Mojo Vision Mojo Lens (2022) — wearable AR contact lens with embedded microLED display (2022-06)

- **id**: `mojo-vision-ar-contact-lens-2022`
- **corpus**: private
- **form factor**: contact-lens
- **creator**: Mojo Vision, Inc.
- **disclosure**: Mojo Vision, Inc. 'Mojo Lens', publicly demonstrated June 2022 — a scleral contact lens with an embedded ~14k-PPI microLED display in the wearer's central field of view, an ARM Cortex processor, eye-tracking via motion sensors, a magnetometer for gaze direction, a microwave radio for offload, and a wirelessly charged battery; rendering an AR information overlay on the cornea. (The consumer AR-glucose pivot followed; production halted c. 2023.)
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-magnetometer
- **algorithms**: algo-eye-gaze-tracking
- **prior art notes**: Discloses a contact lens with an embedded microLED display in the central visual field, on-lens processing, gaze tracking via inertial/magnetic sensors, wireless RF link, and a wirelessly charged on-lens battery — i.e. an AR display contact lens worn on the cornea. Anticipates AR-contact-lens claims combining 'a contact lens', 'an embedded near-eye microdisplay', 'on-lens processing and motion sensors for gaze', and 'a wireless link' from 2022. Product-side anchor for the contact-lens × visual-display cross-cut; cf. [[rainbows-end-ar-contact-lens]] (the 2006 fictional anticipation).
