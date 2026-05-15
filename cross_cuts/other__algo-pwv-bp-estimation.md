---
title: other ∩ algo-pwv-bp-estimation
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `algo-pwv-bp-estimation`

Axes: **form_factor × algorithms**

**5 corpus entries disclose both tags.**

Earliest disclosure: 1973

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Peñáz (1973) — the volume-clamp (vascular unloading) method of continuous finger blood pressure (1973)

- **id**: `penaz-1973-volume-clamp-finger-bp`
- **corpus**: academic
- **form factor**: other
- **creator**: Jan Peñáz
- **disclosure**: Peñáz J. 'Photoelectric measurement of blood pressure, volume and flow in the finger.' Digest of the 10th International Conference on Medical and Biological Engineering, Dresden, 1973, p. 104. (Basis of the Finapres / volume-clamp continuous BP monitors.)
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-cuffless-bp-volume-clamp, sensor-pressure-skin
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Discloses the volume-clamp / vascular-unloading method: a finger cuff servo-controlled by a photoplethysmographic feedback loop to hold the arterial volume constant, so the applied counter-pressure tracks the arterial pressure waveform continuously and non-invasively. Any cuffless/continuous-BP wearable claim reciting 'a photoplethysmographic feedback loop controlling an applied pressure to maintain constant vascular volume' reads on Peñáz 1973. Anchor for the volume-clamp cuffless-BP cross-cut (the finger/ring form-factor variants are obvious combinations under [[obviousness-template]]).

## Geddes et al. (1981) — pulse transit time as an indicator of arterial blood pressure (1981-01)

- **id**: `geddes-1981-pulse-transit-time-bp`
- **corpus**: academic
- **form factor**: other
- **creator**: Leslie A. Geddes et al. (Purdue)
- **disclosure**: Geddes LA, Voelz MH, Babbs CF, Bourland JD, Tacker WA. 'Pulse transit time as an indicator of arterial blood pressure.' Psychophysiology 1981;18(1):71-74.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Establishes that pulse transit time — the delay between a proximal timing reference (e.g. the ECG R-wave) and the arrival of the pulse at a distal site (e.g. a finger PPG) — varies inversely with arterial blood pressure, and can therefore be used to estimate BP without a cuff. Any cuffless-BP wearable claim reciting 'estimating blood pressure from a pulse transit time (or pulse arrival time / pulse wave velocity) derived from two physiological signals' reads on Geddes 1981. Earliest anchor for the PTT-cuffless-BP cross-cut; [[mukkamala-2015-ptt-cuffless-bp-review]] is the modern survey.

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

## Mukkamala et al. (2015) — 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice' (2015-08)

- **id**: `mukkamala-2015-ptt-cuffless-bp-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Ramakrishna Mukkamala et al.
- **disclosure**: Mukkamala R, Hahn J-O, Inan OT, Mestha LK, Kim C-S, Töreyin H, Kyal S. 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice.' IEEE Transactions on Biomedical Engineering 2015;62(8):1879-1901.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt, sensor-cuffless-bp-tonometry
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Canonical 2015 review of cuffless blood-pressure estimation by pulse transit time / pulse arrival time / pulse wave velocity: the physiological models, the practical sensor configurations (ECG+PPG, dual PPG, ballistocardiogram+PPG), the calibration strategies, and the accuracy limitations. Prior art for cuffless-BP wearable claims reciting any of the configurations or calibration approaches surveyed here — they were collected, modeled, and published by 2015. Combined with watch/ring/patch form-factor disclosures, makes wearable PTT-based BP an obvious combination under [[obviousness-template]].
