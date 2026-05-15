---
title: sensor-spo2
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-spo2`

Axis: **sensors**

**8 corpus entries disclose this tag.**

Earliest disclosure: 1974

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Aoyagi (1974) — two-wavelength pulse oximetry principle (1974)

- **id**: `aoyagi-1974-two-wavelength-pulse-oximetry`
- **corpus**: private
- **form factor**: other
- **creator**: Takuo Aoyagi (Nihon Kohden)
- **disclosure**: Aoyagi T, et al. — the pulsatile two-wavelength (red/infrared) ratio method for non-invasive arterial oxygen saturation, presented at the 13th Annual Meeting of the Japan Society of Medical Electronics and Biological Engineering (1974); commercialized as the Nihon Kohden 'Ear Oximeter OLV-5100' (1975) and Minolta 'Oximet MET-1471' (1977). History documented in Severinghaus JW, Honda Y. 'History of blood gas analysis. VII. Pulse oximetry.' J Clin Monit 1987;3(2):135-138.
- **ip status**: patented
- **sensors**: sensor-spo2, sensor-ppg, sensor-multi-wavelength-ppg
- **algorithms**: algo-spo2-estimation
- **prior art notes**: Discloses the pulsatile two-wavelength ratiometric method that underlies every non-invasive SpO2 device: comparing the AC/DC ratios of light absorbance at (typically) red ~660 nm and infrared ~940 nm through pulsatile tissue to compute arterial oxygen saturation. Any wearable claim reciting 'a first and second light source at distinct wavelengths and a photodetector configured to compute oxygen saturation from a ratio of pulsatile components' reads on this. § 102 prior art for the SpO2 principle from 1974; the wrist/ring/earbud form-factor variants are obvious combinations under [[obviousness-template]].

## Mendelson & Ochs (1988) — reflectance-mode pulse oximetry / skin-reflectance PPG (1988-10)

- **id**: `mendelson-ochs-1988-reflectance-pulse-oximetry`
- **corpus**: academic
- **form factor**: other
- **creator**: Yitzhak Mendelson / Burt D. Ochs
- **disclosure**: Mendelson Y, Ochs BD. 'Noninvasive pulse oximetry utilizing skin reflectance photoplethysmography.' IEEE Transactions on Biomedical Engineering 1988;35(10):798-805.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg
- **algorithms**: algo-spo2-estimation, algo-hr
- **prior art notes**: Establishes pulse oximetry by reflectance (light source and detector on the same side of the tissue) rather than transmission — the geometry every wrist, forehead, ring, chest, and earbud PPG/SpO2 wearable uses, since those sites cannot be transilluminated. Any wearable-SpO2 claim reciting 'a reflectance photoplethysmography sensor' or 'a light source and photodetector arranged on a common surface against the skin' reads on Mendelson & Ochs 1988. Anchor for the reflectance-PPG/SpO2 cross-cut on non-fingertip sites.

## Webster (ed.) (1997) — 'Design of Pulse Oximeters' (1997)

- **id**: `webster-1997-design-of-pulse-oximeters`
- **corpus**: academic
- **form factor**: other
- **creator**: John G. Webster (ed.)
- **disclosure**: Webster JG (ed). 'Design of Pulse Oximeters.' Series in Medical Physics and Biomedical Engineering, IOP Publishing / Institute of Physics, 1997. ISBN 0-7503-0467-7.
- **ip status**: public-domain
- **sensors**: sensor-spo2, sensor-ppg
- **algorithms**: algo-spo2-estimation, algo-hr
- **prior art notes**: The standard engineering reference on pulse oximeter design as of 1997 — LED selection and drive, photodiode front-ends, the ratio-of-ratios calibration, motion-artifact handling, low-perfusion behavior, calibration-curve construction. Prior art for wearable-SpO2 claims to the extent they recite implementation details (wavelength choice, AC/DC ratio computation, calibration-curve mapping, artifact rejection) covered here; these were textbook-level public knowledge by 1997.

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

## ISO 80601-2-61 — particular requirements for basic safety and essential performance of pulse oximeter equipment (2011/2017) (2011-08-15)

- **id**: `iso-80601-2-61-pulse-oximeter-equipment-2011`
- **corpus**: standards
- **form factor**: other
- **creator**: ISO/IEC (TC 121/SC 3 and IEC SC 62D)
- **disclosure**: ISO 80601-2-61:2011 (revised 2017). 'Medical electrical equipment — Part 2-61: Particular requirements for basic safety and essential performance of pulse oximeter equipment.' ISO, 2011.
- **ip status**: standards
- **sensors**: sensor-spo2, sensor-ppg, sensor-multi-wavelength-ppg
- **algorithms**: algo-spo2-estimation
- **prior art notes**: Publicly-adopted standard defining pulse oximeter equipment (a device estimating SpO2 and pulse rate from light at two or more wavelengths through perfused tissue) and the accuracy/validation requirements for it. Prior art for wearable-SpO2 claims to the extent they recite the multi-wavelength pulsatile method or the SpO2-and-pulse-rate output described here; the equipment definition and method have been a published standard since 2011 (building on the [[aoyagi-1974-two-wavelength-pulse-oximetry]] principle).

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
