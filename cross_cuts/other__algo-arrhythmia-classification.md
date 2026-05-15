---
title: other ∩ algo-arrhythmia-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `algo-arrhythmia-classification`

Axes: **form_factor × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 2010-01

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
