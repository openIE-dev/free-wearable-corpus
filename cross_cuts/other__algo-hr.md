---
title: other ∩ algo-hr
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `algo-hr`

Axes: **form_factor × algorithms**

**10 corpus entries disclose both tags.**

Earliest disclosure: 1968

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Blade Runner — the Voight-Kampff machine (contactless multi-physiological liveness/identity test) (1968)

- **id**: `blade-runner-voight-kampff`
- **corpus**: fictional
- **form factor**: other
- **creator**: Philip K. Dick
- **disclosure**: Dick, Philip K. Do Androids Dream of Electric Sheep? Doubleday, 1968 (film: Blade Runner, Warner Bros., 1982); a portable instrument that measures involuntary physiological responses — pupil dilation, 'capillary dilation of the so-called blush response', heart rate, micro-expression — under questioning, to classify a subject as human or replicant.
- **ip status**: fictional
- **sensors**: sensor-camera-ir, sensor-camera-eye
- **algorithms**: algo-pupillometry, algo-hr, algo-emotion-recognition
- **prior art notes**: Discloses a device that contactlessly measures multiple involuntary physiological signals from a person's face (pupil dilation, blush/capillary response, heart rate, micro-expression) and fuses them into a binary classification of the subject. Relevant to remote-photoplethysmography / pupillometry / 'deception or liveness detection' claims combining 'contactless facial imaging', 'extraction of two or more involuntary physiological signals', and 'a classification of the subject'. § 103 motivation as of 1968. Cf. [[psycho-pass-cymatic-scan]], [[gattaca-biometric-checkpoints]].

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

## Continua Health Alliance — Design Guidelines (first edition, 2007) (2007)

- **id**: `continua-design-guidelines-2007`
- **corpus**: standards
- **form factor**: other
- **creator**: Continua Health Alliance
- **disclosure**: Continua Health Alliance (later Personal Connected Health Alliance). 'Continua Design Guidelines' (first edition published 2007; subsequently maintained, ITU-T H.810 series). Specifies end-to-end interoperability for personal connected health devices, profiling IEEE 11073, Bluetooth, USB, ZigBee, HL7/IHE.
- **ip status**: standards
- **sensors**: sensor-ppg, sensor-ecg, sensor-glucose-cgm, sensor-accelerometer
- **algorithms**: algo-hr, algo-step-count, algo-glucose-cgm-readout
- **prior art notes**: Publicly-published end-to-end interoperability framework for personal connected health devices — defining how a body-worn sensor (weight scale, blood-pressure cuff, glucose meter, pulse oximeter, activity monitor, ECG, etc.) connects to an application hub and onward to health-record systems, profiling the underlying transport and data standards. Prior art for connected-wearable-system claims reciting the architecture, the device-to-hub-to-record data flow, or the standard profiles assembled here, public from 2007.

## Allen (2007) — 'Photoplethysmography and its application in clinical physiological measurement' (2007-02-20)

- **id**: `allen-2007-ppg-review`
- **corpus**: academic
- **form factor**: other
- **creator**: John Allen (Freeman Hospital / Newcastle)
- **disclosure**: Allen J. 'Photoplethysmography and its application in clinical physiological measurement.' Physiological Measurement 2007;28(3):R1-R39. doi:10.1088/0967-3334/28/3/R01.
- **ip status**: public-domain
- **sensors**: sensor-ppg
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-spo2-estimation, algo-pwv-bp-estimation
- **prior art notes**: Canonical review collecting the state of PPG measurement and the physiological parameters derivable from a PPG signal as of 2007 — heart rate, HRV, respiratory rate, SpO2, blood-pressure surrogates, arterial-stiffness/aging indices, vasomotor assessment. Relevant to wearable claims that recite 'deriving [parameter X] from a photoplethysmography signal' for any X covered here: the derivation was a published, enabled technique by 2007, defeating novelty of the bare derivation and supplying § 103 motivation for the form-factor+PPG+algorithm combinations. The single most-cited anchor for PPG-derived-metric wearable patents.

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

## Bluetooth SIG — Heart Rate Profile / Heart Rate Service (2011) (2011-07-12)

- **id**: `bluetooth-sig-heart-rate-profile-2011`
- **corpus**: standards
- **form factor**: other
- **creator**: Bluetooth Special Interest Group
- **disclosure**: Bluetooth SIG. 'Heart Rate Profile' specification v1.0 and 'Heart Rate Service' (GATT service UUID 0x180D, characteristics: Heart Rate Measurement 0x2A37, Body Sensor Location 0x2A38, Heart Rate Control Point 0x2A39), adopted 12 July 2011; available at bluetooth.com/specifications.
- **ip status**: standards
- **sensors**: sensor-ppg, sensor-ecg
- **algorithms**: algo-hr
- **prior art notes**: A publicly-adopted standard defining how a body-worn heart-rate sensor advertises, structures, and transmits heart-rate measurements (including energy expended and RR-interval data) over Bluetooth Low Energy to a collector, with a defined sensor-location enumeration including wrist, finger, ear, chest, foot, hand. Prior art for wearable-HR claims reciting 'a BLE-advertised heart-rate measurement characteristic', 'transmission of RR intervals from a body-worn sensor', or a 'body sensor location' field — these were standardized and public from 2011. Relevant to PPG and ECG HR wearables alike.

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
