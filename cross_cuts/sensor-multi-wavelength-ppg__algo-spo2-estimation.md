---
title: sensor-multi-wavelength-ppg ∩ algo-spo2-estimation
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-multi-wavelength-ppg` ∩ `algo-spo2-estimation`

Axes: **sensors × algorithms**

**4 corpus entries disclose both tags.**

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
