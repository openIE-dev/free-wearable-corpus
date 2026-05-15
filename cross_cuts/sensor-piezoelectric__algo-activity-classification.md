---
title: sensor-piezoelectric ∩ algo-activity-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-piezoelectric` ∩ `algo-activity-classification`

Axes: **sensors × algorithms**

**4 corpus entries disclose both tags.**

Earliest disclosure: 1998-10

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Williams et al. (1998) — accelerometer-based automatic fall and activity monitor for telecare (1998-10)

- **id**: `williams-1998-automatic-fall-detector`
- **corpus**: academic
- **form factor**: belt
- **creator**: G. Williams / K. Doughty / K. Cameron / D.A. Bradley
- **disclosure**: Williams G, Doughty K, Cameron K, Bradley DA. 'A smart fall and activity monitor for telecare applications.' Proceedings of the 20th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBS), Hong Kong, 1998, pp. 1151-1154.
- **ip status**: unknown
- **sensors**: sensor-accelerometer, sensor-piezoelectric
- **algorithms**: algo-fall-detection, algo-activity-classification
- **prior art notes**: Discloses a body-worn (waist/trunk) device that automatically detects a fall from accelerometer/impact signals — distinguishing falls from normal activity — and raises a telecare alarm, without requiring the wearer to press a button. Anticipates automatic-fall-detection wearable claims combining 'a body-worn inertial sensor', 'a classifier distinguishing a fall from activities of daily living', and 'an automatic alert on detection'. Anchor for the fall-detection cross-cut; combined with watch/pendant form-factor disclosures, makes wristworn/pendant automatic fall detection obvious under [[obviousness-template]].

## Paradiso et al. (2005) — 'A wearable health care system based on knitted integrated sensors' (WEALTHY) (2005-09)

- **id**: `paradiso-2005-wealthy-knitted-smart-shirt`
- **corpus**: academic
- **form factor**: garment
- **creator**: Rita Paradiso / Giannicola Loriga / Nicola Taccini (Smartex / CNR, Italy; EU WEALTHY consortium)
- **disclosure**: Paradiso R, Loriga G, Taccini N. 'A wearable health care system based on knitted integrated sensors.' IEEE Transactions on Information Technology in Biomedicine 2005;9(3):337-344. (Output of the EU FP5 'WEALTHY' project, 2002-2005.)
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification
- **prior art notes**: Discloses a smart shirt with electrodes and sensors knitted directly into the textile (conductive yarns forming dry ECG electrodes; piezoresistive yarns forming respiration sensors via thoracic/abdominal expansion; accelerometer; temperature) plus an on-garment electronic interface and wireless link, deriving ECG, heart rate, respiration, posture/activity, and temperature — i.e. a fully integrated textile-electrode wearable. Any claim reciting 'an item of clothing with electrodes/sensors integrated into the fabric structure for physiological monitoring' reads on Paradiso 2005. Anchor for the garment × textile-electrode cross-cut; the foundational EU project for the smart-shirt patent space (Hexoskin, Cityzen, etc. all build on this lineage).

## Hexoskin smart shirt (2014) — textile-integrated ECG, respiration and activity garment (2013)

- **id**: `hexoskin-smart-shirt-2014`
- **corpus**: private
- **form factor**: garment
- **creator**: Carre Technologies Inc.
- **disclosure**: Carre Technologies Inc. (Hexoskin). 'Hexoskin Smart Shirt', introduced 2013 (consumer); a compression shirt with knitted dry textile electrodes for single-lead ECG, two-channel respiratory inductive plethysmography (thoracic + abdominal expansion), a 3-axis accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate/volume, cadence, steps, and sleep. (Used in NASA/CSA 'Astroskin' studies.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a consumer/research compression shirt with textile-integrated dry ECG electrodes, two-channel respiratory inductive plethysmography (thoracic + abdominal), an accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate and volume, activity, and sleep. A commercial realization of [[paradiso-2005-wealthy-knitted-smart-shirt]]; anticipates smart-shirt claims combining 'textile-integrated ECG and respiration sensors' and 'a detachable electronics module' from 2013. Product-side anchor for the garment × textile-electrode cross-cut.

## Sensoria Smart Socks (2014) — pressure-sensing sock + electronic anklet for gait/running analysis (2014-01)

- **id**: `sensoria-smart-socks-2014`
- **corpus**: private
- **form factor**: sock
- **creator**: Sensoria Inc. (formerly Heapsylon)
- **disclosure**: Sensoria Inc. 'Sensoria Fitness Smart Socks', announced January 2014 — running socks with three pressure-sensitive textile sensors woven into the sole (under the heel, ball of foot, and toes) and a magnetically-attached 'Sensoria Core' anklet (accelerometer + Bluetooth) that derives cadence, foot strike pattern (heel/mid/forefoot), foot landing zone, pace, distance, and provides real-time audio coaching.
- **ip status**: patented
- **sensors**: sensor-pressure-skin, sensor-piezoelectric, sensor-accelerometer
- **algorithms**: algo-step-count, algo-gait-analysis, algo-activity-classification
- **prior art notes**: Discloses a sock with multiple pressure-sensitive textile sensors woven into the sole, paired with a removable ankle-worn electronics module that derives cadence, foot-strike pattern, pressure distribution, and pace. Anticipates smart-sock/sole-pressure-sensing claims combining 'a sock with one or more textile pressure sensors at multiple positions of the foot sole' and 'a paired electronics module deriving gait metrics' from 2014. Product-side anchor for the sock form-factor cross-cut (the only `sock` entry); cf. [[nike-plus-ipod-sport-kit-2006]] (the earlier shoe/insole route).
