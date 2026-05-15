---
title: garment ∩ algo-arrhythmia-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `garment` ∩ `algo-arrhythmia-classification`

Axes: **form_factor × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 1961-04-21

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
