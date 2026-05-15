---
title: other ∩ sensor-spo2
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `sensor-spo2`

Axes: **form_factor × sensors**

**5 corpus entries disclose both tags.**

Earliest disclosure: 1974

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

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
