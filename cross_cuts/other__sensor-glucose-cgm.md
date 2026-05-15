---
title: other ∩ sensor-glucose-cgm
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `sensor-glucose-cgm`

Axes: **form_factor × sensors**

**5 corpus entries disclose both tags.**

Earliest disclosure: 1962

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Clark & Lyons (1962) — the enzyme electrode (basis of the amperometric glucose biosensor) (1962)

- **id**: `clark-lyons-1962-enzyme-electrode`
- **corpus**: academic
- **form factor**: other
- **creator**: Leland C. Clark Jr. / Champ Lyons
- **disclosure**: Clark LC Jr, Lyons C. 'Electrode systems for continuous monitoring in cardiovascular surgery.' Annals of the New York Academy of Sciences 1962;102(1):29-45.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm
- **prior art notes**: Proposes coupling an enzyme (glucose oxidase) to an oxygen electrode so that the electrode current reports glucose concentration — the founding concept of the amperometric enzyme biosensor and hence of every electrochemical continuous glucose monitor. Any CGM claim reciting 'an enzyme electrode configured to generate a current dependent on glucose concentration' rests on a concept public since 1962. § 102 prior art for the electrochemical-glucose-sensing principle.

## Updike & Hicks (1967) — the practical glucose enzyme electrode (1967-06-03)

- **id**: `updike-hicks-1967-enzyme-electrode`
- **corpus**: academic
- **form factor**: other
- **creator**: Stuart J. Updike / George P. Hicks
- **disclosure**: Updike SJ, Hicks GP. 'The enzyme electrode.' Nature 1967;214(5092):986-988.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm
- **prior art notes**: Reduces Clark & Lyons's concept to a working device — an immobilized-enzyme membrane on an electrode giving a glucose-dependent signal — the practical ancestor of the implantable/subcutaneous glucose sensor. Prior art for CGM claims reciting 'a membrane-immobilized glucose oxidase layer on an electrode'. Combined with [[shichiri-1982-wearable-needle-glucose-sensor]] it establishes both the chemistry and the wearable form.

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

## Bandodkar & Wang (2014) — 'Non-invasive wearable electrochemical sensors: a review' (2014-07)

- **id**: `bandodkar-wang-2014-wearable-electrochemical-sensors-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Amay J. Bandodkar / Joseph Wang (UC San Diego)
- **disclosure**: Bandodkar AJ, Wang J. 'Non-invasive wearable electrochemical sensors: a review.' Trends in Biotechnology 2014;32(7):363-371.
- **ip status**: public-domain
- **sensors**: sensor-lactate, sensor-electrolyte, sensor-ph, sensor-glucose-cgm, sensor-alcohol-transdermal, sensor-uric-acid, sensor-cortisol
- **algorithms**: algo-electrolyte-trend, algo-hydration-status
- **prior art notes**: Surveys, as of 2014, wearable non-invasive electrochemical biosensors across body fluids and form factors — temporary-tattoo electrodes on the skin (sweat lactate, Na+, ammonium, pH), textile-integrated sensors, mouthguard (saliva) sensors, contact-lens (tear glucose) sensors, and the transdermal/interstitial route — including the sampling, transduction, and on-body electronics issues. Prior art for wearable-electrochemical-sensing claims reciting any of the analyte/form-factor combinations collected here; the approaches were published by 2014. General anchor for the electrochemical wearable cross-cuts.

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.
