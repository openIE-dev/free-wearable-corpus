---
title: sensor-ecg ∩ algo-arrhythmia-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ecg` ∩ `algo-arrhythmia-classification`

Axes: **sensors × algorithms**

**11 corpus entries disclose both tags.**

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

## FDA 510(k) K113862 (~2011) — iRhythm Zio Patch, long-term single-lead adhesive ECG monitor (2011-12)

- **id**: `fda-k113862-irhythm-zio-patch-2011`
- **corpus**: regulatory
- **form factor**: patch
- **creator**: U.S. Food and Drug Administration (CDRH); submitter iRhythm Technologies, Inc.
- **disclosure**: U.S. FDA, 510(k) Premarket Notification K113862 (iRhythm Technologies, Inc., 'Zio Patch') — record at accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K113862; a single-use adhesive chest patch recording a single channel of ECG continuously for up to ~14 days for later analysis, cleared as substantially equivalent to predicate ambulatory-ECG (Holter-class) devices. (Followed by a chain of subsequent iRhythm 510(k)s — e.g. K143513, K163512, K181502 — refining the device, the algorithm/ZEUS software, and the Zio AT mobile-cardiac-telemetry variant.)
- **ip status**: regulatory-filing
- **sensors**: sensor-ecg
- **algorithms**: algo-arrhythmia-classification, algo-afib-detection
- **prior art notes**: A public, dated FDA record of a single-use adhesive chest patch that records one channel of ECG continuously for up to ~14 days for later arrhythmia analysis — the modern 'ECG patch' realization of ambulatory ECG ([[holter-1961-ambulatory-ecg]]). Establishes as of ~2011 the public availability of an adhesive long-wear single-lead ECG patch with downstream automated arrhythmia analysis; and, as a 510(k), it cites a predicate chain back to earlier ambulatory-ECG devices — that chain is itself prior art. Prior art for ECG-patch claims; product-side and regulatory anchor for the patch × ECG cross-cut. Cf. [[apple-watch-series4-ecg-2018]] (the wrist single-lead route).

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

## FDA De Novo DEN180044 (2018) — over-the-counter electrocardiograph software for use in detecting atrial fibrillation (Apple Watch ECG app) (2018-09-11)

- **id**: `fda-den180044-apple-watch-ecg-app-2018`
- **corpus**: regulatory
- **form factor**: watch
- **creator**: U.S. Food and Drug Administration (CDRH); requester Apple Inc.
- **disclosure**: U.S. FDA, De Novo Classification Request DEN180044 (Apple Inc., 'ECG App'), granted 11 September 2018 — decision summary at accessdata.fda.gov/cdrh_docs/reviews/DEN180044.pdf; established a new FDA device classification for over-the-counter electrocardiograph software intended to acquire, store, transfer and display a single-lead (Lead I) ECG and to provide a rhythm classification (AFib vs. sinus rhythm) on a consumer wrist-worn platform, with general/special controls.
- **ip status**: regulatory-filing
- **sensors**: sensor-ecg
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification
- **prior art notes**: A public, dated FDA decision describing — and creating the device class for — over-the-counter single-lead ECG software on a consumer wrist-worn device with on-device AFib-vs-sinus classification. As a government disclosure it establishes, as of 11 September 2018, the public availability of the device described: a wristworn Lead-I ECG with consumer-facing rhythm classification. Useful prior art for later claims to that combination; the De Novo decision summary also enumerates the clinical validation and the bench/algorithm characteristics, which are themselves citable. Pairs with the product entry [[apple-watch-series4-ecg-2018]] and the standard [[ieee-11073-10406-basic-ecg-2011]].

## Apple Watch Series 4 (2018) — wrist single-lead ECG and PPG-based irregular-rhythm notification (2018-09-12)

- **id**: `apple-watch-series4-ecg-2018`
- **corpus**: private
- **form factor**: watch
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. 'Apple Watch Series 4', announced 12 September 2018 (ECG app and irregular rhythm notification feature enabled later in 2018) — a wristworn device taking a single-lead (Lead I) ECG between a back-crystal electrode and a Digital Crown electrode touched by the opposite hand, with on-device AF/sinus classification, plus a PPG-based irregular-rhythm (possible-AF) notification algorithm. FDA cleared via De Novo (ECG app: DEN180044; irregular rhythm notification: DEN180042).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-ppg
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-hr
- **prior art notes**: Discloses a wristworn device that records a single-lead ECG between a watch-back electrode and a crown electrode touched by the contralateral hand, classifies the rhythm (AF vs. sinus) on-device, and separately runs a PPG-based background algorithm flagging possible atrial fibrillation. Anticipates wristworn-ECG and watch-AF-detection claims postdating September 2018; the underlying single-lead ECG and PPG-rhythm-screening techniques are much older ([[einthoven-1903-string-galvanometer-ecg]], [[holter-1961-ambulatory-ecg]], [[allen-2007-ppg-review]], [[ieee-11073-10406-basic-ecg-2011]]). Product-side anchor for the watch × ECG and watch × PPG × AF-detection cross-cuts.

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

## Samsung Galaxy Watch3 / Samsung Health Monitor (2020) — wrist single-lead ECG and optical-PPG cuffless blood pressure (2020-08)

- **id**: `samsung-galaxy-watch-bp-ecg-2020`
- **corpus**: private
- **form factor**: watch
- **creator**: Samsung Electronics Co., Ltd.
- **disclosure**: Samsung Electronics. 'Samsung Health Monitor' app on Galaxy Watch3 / Watch Active2, 2020 — wrist single-lead ECG (between a back-crystal electrode and a side-button electrode touched by the opposite hand, with AF/sinus classification) and a cuffless blood-pressure feature using the optical (PPG) pulse-wave signal calibrated against a periodic conventional cuff reading. (Cleared in Korea 2020; subsequently in other markets.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-pwv-bp-estimation, algo-hr
- **prior art notes**: Discloses a wristworn device that takes a single-lead ECG with on-device AF classification and, separately, estimates blood pressure from the wrist optical-PPG pulse waveform after calibration against a periodic conventional cuff measurement (a calibrated-cuffless approach). Anticipates wrist-cuffless-BP claims reciting 'estimating blood pressure from a wrist photoplethysmography signal calibrated by a reference cuff reading' from 2020 — the underlying PTT/PWV-BP technique is much older ([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the watch × cuffless-BP cross-cut.
