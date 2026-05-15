---
title: other ∩ algo-hrv
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `algo-hrv`

Axes: **form_factor × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 1996-03

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Task Force of the ESC and NASPE (1996) — heart rate variability: standards of measurement (1996-03)

- **id**: `esc-naspe-1996-hrv-standards`
- **corpus**: standards
- **form factor**: other
- **creator**: Task Force of the ESC and NASPE
- **disclosure**: Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. 'Heart rate variability: standards of measurement, physiological interpretation, and clinical use.' Circulation 1996;93(5):1043-1065 (also European Heart Journal 1996;17:354-381).
- **ip status**: standards
- **sensors**: sensor-ecg, sensor-ppg
- **algorithms**: algo-hrv, algo-stress-index
- **prior art notes**: Standardizes the time-domain (SDNN, RMSSD, pNN50, ...) and frequency-domain (VLF/LF/HF, LF/HF ratio) measures of heart rate variability, their computation from an interbeat-interval series, and their physiological interpretation. Any wearable claim reciting 'computing a heart-rate-variability metric (e.g. RMSSD, LF/HF) from a sequence of interbeat intervals' rests on metrics standardized here. Anchor for the HRV cross-cut; applicable whether the interbeat intervals come from ECG or PPG.

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
