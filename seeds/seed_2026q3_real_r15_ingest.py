#!/usr/bin/env python3
"""seed_2026q3_real_r15_ingest.py — ingest batch from the 2026-05-16 wearables convo.

Eleven entries that fill real gaps in the corpus:

Open watches (the corpus's `open` bucket was only 1 entry — OpenBCI):
  - HealthyPi Move (ProtoCentral, 2026) — full-stack open-source medical-grade smartwatch
  - PineTime (Pine64, 2018-2020) — the precedent low-cost open smartwatch
  - Bangle.js 2 (Espruino, 2021) — open JS-app smartwatch validated in academic research
  - Open-Watch (SMotlaq BSc thesis, 2021) — fully documented open STM32 smartwatch

Contact lens prior art the corpus was missing:
  - Sensimed Triggerfish — the *only* commercially shipping smart contact lens
    (glaucoma 24-h IOP monitoring; CE-marked Class IIa 2009, FDA De Novo 2016).
    A major omission to fix.
  - XPANCEO (2024) — Dubai-based AR smart contact lens, $40M+, CES demos
  - Pandey et al. 2010 — the canonical 'fully integrated RF-powered contact lens'
    academic disclosure (the disclosure root for ambient-RF-powered wearables)
  - Pourshaban et al. 2024 — dual-mode (solar + RF) sub-mW contact-lens harvester

Ring/hand gesture input:
  - Tap Strap (Tap Systems, 2018) — finger-mounted gesture/keyboard input

Open-hardware academic smartwatches:
  - H-Watch (Magno et al., arXiv 2407.21501, 2024) — open Cortex-M4F + ML + NB-IoT
    + energy-harvesting research smartwatch
  - CogWatch (HardwareX 2024) — open-source cognitive-load smartwatch

Run from repo root:  python3 seeds/seed_2026q3_real_r15_ingest.py
Idempotent.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-16"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    # ---------------- OPEN WATCHES ----------------
    E(
        id="healthypi-move-2026",
        canonical_name="HealthyPi Move (ProtoCentral, 2026) — open-source medical-grade smartwatch",
        aliases=["HealthyPi Move", "ProtoCentral HealthyPi Move"],
        corpus="open",
        first_disclosure_date="2024",
        disclosure_citation="ProtoCentral Electronics (Bengaluru, India). 'HealthyPi Move' fully open-source AMOLED smartwatch — Crowd Supply campaign launched 2024, units shipping 15 May 2026. Sensors: single-lead ECG, dual-site PPG (wrist + finger), SpO2, blood-pressure trending, EDA/GSR, heart rate, HRV, respiration rate (derived), body temperature, 6-axis IMU. Compute: Nordic nRF5340 (dual ARM Cortex-M33). Display: AMOLED, 300 mAh battery. Companion app: Flutter, runs on Android/iOS/macOS/Windows/Linux, all data stored locally. Hardware design, firmware (Zephyr RTOS on nRF Connect SDK), and companion app all open-source. https://www.crowdsupply.com/protocentral/healthypi-move",
        creator="ProtoCentral Electronics",
        creator_country="IN",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist", "fingertip"],
        sensors=["sensor-ecg", "sensor-ppg", "sensor-spo2", "sensor-multi-wavelength-ppg", "sensor-gsr", "sensor-accelerometer", "sensor-gyroscope", "sensor-skin-temperature"],
        algorithms=["algo-hr", "algo-hrv", "algo-spo2-estimation", "algo-respiratory-rate", "algo-pwv-bp-estimation", "algo-sleep-staging", "algo-activity-classification", "algo-step-count"],
        clinical_endpoints=["electrocardiogram", "blood-oxygen", "heart-rate", "heart-rate-variability", "respiratory-rate", "blood-pressure", "electrodermal-activity", "skin-temperature"],
        ip_status="open-permissive",
        connectivity="ble",
        notes="The corpus's anchor for 'the entire wearable sensor stack is implementable as open-source hardware.' Falsifies any claim that the integrated multi-sensor consumer smartwatch is necessarily proprietary.",
        prior_art_notes=(
            "Discloses, as fully open-source hardware and firmware (CC and MIT-style "
            "licensing across components), a wrist-worn smartwatch with the full "
            "consumer-medical sensor stack: single-lead ECG between back-of-watch "
            "electrode and a finger-touch electrode; multi-wavelength reflectance PPG "
            "with SpO2 and BP-trending; EDA/GSR; skin temperature; 6-axis IMU; on-device "
            "Zephyr-RTOS application; AMOLED display; all-local data storage via "
            "cross-platform Flutter app. Anticipates wrist-multi-sensor-watch claims "
            "from 2024-2026 to the extent they recite combinations of these elements; "
            "as `open` prior art it is unencumbered and any patent claim reciting these "
            "combinations must distinguish over HealthyPi Move's specific implementation. "
            "The product-side anchor for the 'open watch with the full sensor stack' "
            "cross-cut."
        ),
        sources=[
            "ProtoCentral, HealthyPi Move (Crowd Supply campaign, 2024).",
            "github.com/Protocentral (hardware + firmware + app repositories).",
        ],
        cpc_classifications=["A61B 5/0006", "A61B 5/02416", "A61B 5/318", "A61B 5/14552", "G04G 21/04"],
    ),
    E(
        id="pine64-pinetime-2020",
        canonical_name="Pine64 PineTime (2018-2020) — low-cost open-source smartwatch",
        aliases=["PineTime", "Pine64 PineTime"],
        corpus="open",
        first_disclosure_date="2018-09",
        disclosure_citation="Pine64. 'PineTime' open-source smartwatch — first announced September 2018, dev-kit shipping early 2020, sealed units (~US$30) shipping from late 2020. Hardware: Nordic nRF52832 (ARM Cortex-M4), heart-rate monitor, 3-axis accelerometer, touchscreen, BLE. Open firmware: 'InfiniTime' (C++/FreeRTOS) at github.com/InfiniTimeOrg/InfiniTime; 'Wasp-OS' (Python/MicroPython) at github.com/daniel-thompson/wasp-os. Hardware schematics at wiki.pine64.org/wiki/PineTime. https://pine64.com/product/pinetime-smartwatch-sealed/",
        creator="Pine Store Ltd. (Pine64)",
        creator_country="HK",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-step-count"],
        clinical_endpoints=["heart-rate"],
        ip_status="open-permissive",
        connectivity="ble",
        prior_art_notes=(
            "Discloses a low-cost (US$30) wrist-worn smartwatch with PPG-HR sensor, "
            "accelerometer, touchscreen, BLE, and fully open-source firmware (InfiniTime "
            "in C++/FreeRTOS, or Wasp-OS in Python/MicroPython on the same hardware) and "
            "published hardware schematics. Establishes (since 2018-2020) that the "
            "basic smartwatch architecture — MCU + PPG + accel + display + BLE + open "
            "firmware — is unencumbered open-hardware prior art. Distinct from "
            "[[healthypi-move-2026]] in being earlier and simpler; together they "
            "establish open-watch prior art across a >5-year span."
        ),
        sources=[
            "Pine Store Ltd., PineTime (product, 2018-2020).",
            "github.com/InfiniTimeOrg/InfiniTime (firmware).",
            "wiki.pine64.org/wiki/PineTime (schematics).",
        ],
        cpc_classifications=["A61B 5/02416", "A61B 5/681", "G04G 21/04"],
    ),
    E(
        id="bangle-js-2-2021",
        canonical_name="Bangle.js 2 (Espruino, 2021) — open JavaScript-app smartwatch validated in academic research",
        aliases=["Bangle.js 2", "Espruino smartwatch"],
        corpus="open",
        first_disclosure_date="2021",
        disclosure_citation="Espruino / Pur3 Ltd. 'Bangle.js 2', released 2021 — Nordic nRF52840 (ARM Cortex-M4), GPS, heart rate, 3-axis accelerometer, magnetometer, pressure sensor; 4-week battery life; JavaScript app development with web-based app loader. https://banglejs.com . Validated for step counting and heart-rate measurement in academic research (multi-subject MDPI study).",
        creator="Pur3 Ltd. (Gordon Williams, Espruino)",
        creator_country="GB",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-accelerometer", "sensor-magnetometer", "sensor-barometer"],
        algorithms=["algo-hr", "algo-step-count", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "location", "altitude"],
        ip_status="open-permissive",
        connectivity="ble",
        prior_art_notes=(
            "Discloses an open-hardware smartwatch with PPG + IMU + magnetometer + "
            "barometer + GPS, web-loaded JavaScript apps, and 4-week battery life — "
            "validated against reference devices in peer-reviewed studies for step "
            "counting and HR. As open-source hardware released in 2021 it is "
            "unencumbered prior art against patents reciting the open-firmware-platform "
            "smartwatch with this sensor set."
        ),
        sources=[
            "Pur3 Ltd. / Espruino, Bangle.js 2 (product, 2021).",
            "banglejs.com (documentation + schematics).",
        ],
        cpc_classifications=["A61B 5/02438", "A61B 5/1118", "G01S 19/19", "G04G 21/04"],
    ),
    E(
        id="smotlaq-open-watch-2021",
        canonical_name="Open-Watch (Salar Motlaqolahi, 2021) — fully documented open STM32 smartwatch (BSc thesis)",
        aliases=["Open-Watch", "SMotlaq Open-Watch"],
        corpus="open",
        first_disclosure_date="2021",
        disclosure_citation="Motlaqolahi S. 'Open-Watch' — fully open-source smartwatch released as BSc thesis output (MIT license). Hardware: STM32 ARM Cortex-M MCU, MPU6050 6-axis IMU, MAX30102 reflectance PPG + SpO2, 4-layer PCB sponsored by PCBWay, full schematics + Gerbers + firmware published. https://github.com/SMotlaq/open-watch",
        creator="Salar Motlaqolahi",
        creator_country="IR",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-spo2", "sensor-accelerometer", "sensor-gyroscope"],
        algorithms=["algo-hr", "algo-spo2-estimation", "algo-step-count"],
        clinical_endpoints=["heart-rate", "blood-oxygen"],
        ip_status="open-permissive",
        connectivity="ble",
        prior_art_notes=(
            "Discloses, as an MIT-licensed open-hardware smartwatch with full PCB "
            "design files (4-layer, PCBWay-sponsored fabrication) and firmware "
            "published, a wrist-worn device with reflectance PPG + SpO2 + 6-axis IMU "
            "+ MCU + display. Demonstrates that the entire smartwatch design — "
            "schematic, layout, firmware — can be reproduced from undergraduate-thesis-"
            "level public work, defeating any claim that the integrated smartwatch is "
            "novel as a combination."
        ),
        sources=[
            "Motlaqolahi S., 'Open-Watch' github.com/SMotlaq/open-watch (2021).",
        ],
        cpc_classifications=["A61B 5/02416", "A61B 5/14552", "A61B 5/1118", "G04G 21/04"],
    ),
    # ---------------- CONTACT LENS GAPS ----------------
    E(
        id="sensimed-triggerfish-iop-contact-lens-2009",
        canonical_name="Sensimed Triggerfish (2009) — the only commercially shipping smart contact lens (24-h intraocular pressure monitoring for glaucoma)",
        aliases=["Triggerfish", "Sensimed Triggerfish", "CLS-2"],
        corpus="private",
        first_disclosure_date="2009",
        disclosure_citation="Sensimed SA (Lausanne, Switzerland). 'Triggerfish' continuous 24-h intraocular pressure (IOP) monitoring contact lens system, CE-marked Class IIa 2009, FDA De Novo (DEN150040) granted March 2016. A soft hydrogel contact lens with embedded strain-gauge antenna whose resonance frequency shifts with circumferential deformation of the cornea (a proxy for IOP), wirelessly read by a periorbital adhesive antenna patch. The only smart contact lens to reach the commercial market for any indication. https://www.sensimed.ch",
        creator="Sensimed SA (founders: Bertrand Mercier, Matteo Leonardi)",
        creator_country="CH",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea", "limbus"],
        sensors=["sensor-strain-gauge"],
        clinical_endpoints=["intraocular-pressure", "iop-fluctuation"],
        ip_status="patented",
        regulatory_pathway="fda-de-novo",
        ip_citations=["DEN150040"],
        connectivity="nfc",
        draft=True,
        notes="Draft: DEN150040 cited from contact-lens regulatory history; verify against FDA accessdata. CE Class IIa 2009 widely reported. Patent enumeration TODO (Sensimed has a substantial patent portfolio).",
        prior_art_notes=(
            "Discloses a commercially-shipped smart contact lens for continuous, "
            "wirelessly-read measurement of a physiological parameter (intraocular "
            "pressure proxy via cornea circumferential strain) — the first and so far "
            "only smart contact lens cleared for commercial use anywhere in the world. "
            "Anticipates smart-contact-lens claims combining 'a soft ophthalmic contact "
            "lens', 'an embedded strain or other sensor measuring a physiological "
            "parameter', 'wireless readout to a body-mounted patch', and 'continuous "
            "monitoring over a clinically-meaningful interval (24 hours)' from 2009. "
            "Anchor for the contact-lens × shipped-medical-device cross-cut; "
            "complement to [[yao-parviz-2011-contact-lens-glucose-sensor]] (academic), "
            "[[verily-google-smart-contact-lens-2014]] (private, never shipped), and "
            "[[mojo-vision-ar-contact-lens-2022]] (AR, never shipped)."
        ),
        sources=[
            "Sensimed SA, Triggerfish (product, 2009 CE; 2016 FDA).",
        ],
        cpc_classifications=["G02C 7/04", "A61B 3/16", "A61B 5/0031"],
    ),
    E(
        id="xpanceo-ar-contact-lens-2024",
        canonical_name="XPANCEO smart contact lens (2024) — Dubai-based AR/biosensor contact lens project",
        aliases=["XPANCEO", "XPANCEO smart contact lens"],
        corpus="private",
        first_disclosure_date="2022",
        disclosure_citation="XPANCEO (Dubai, UAE). Smart contact lens project — founded 2021, public demonstrations at CES 2024 / 2025; raised >US$40M to date across multiple rounds; demonstrated working prototypes integrating tunable optics, image projection, eye-tracking, and biochemical sensing within a soft contact lens. The most active contact-lens player as of 2026 in the wake of Mojo Vision's pivot. https://xpanceo.com",
        creator="XPANCEO (founders: Roman Axelrod, Dr. Valentyn Volkov)",
        creator_country="AE",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea"],
        sensors=["sensor-camera-eye"],
        output_modalities=["visual-display"],
        ip_status="patented",
        draft=True,
        notes="Draft: patent enumeration TODO; XPANCEO holds patents but specific numbers need enumeration. Product not yet commercial; multiple working prototypes demonstrated.",
        prior_art_notes=(
            "Discloses ongoing development of a smart contact lens integrating an "
            "embedded display, eye/gaze tracking, and biochemical sensing on a soft "
            "ophthalmic contact lens, with substantial venture funding and CES demos. "
            "Even without a shipped product, the public demos and disclosures "
            "constitute prior art as of 2024 against subsequent contact-lens claims. "
            "Complements [[mojo-vision-ar-contact-lens-2022]] (the previous AR-lens "
            "project that paused) and [[sensimed-triggerfish-iop-contact-lens-2009]] "
            "(the only commercially-shipped smart contact lens)."
        ),
        sources=[
            "XPANCEO (company; CES 2024/2025 demonstrations; press coverage 2022-2026).",
        ],
        cpc_classifications=["G02C 7/04", "G02B 27/01", "A61B 3/113"],
    ),
    # ---------------- ACADEMIC: RF-POWERED CONTACT LENS / HARVESTING ----------------
    E(
        id="pandey-2010-rf-powered-contact-lens",
        canonical_name="Pandey et al. (2010) — 'A fully integrated RF-powered contact lens' (the disclosure root of ambient-RF-powered wearables)",
        aliases=["Pandey RF-powered contact lens", "fully integrated RF contact lens"],
        corpus="academic",
        first_disclosure_date="2010",
        disclosure_citation="Pandey J, Liao Y-T, Lingley A, Mirjalili R, Parviz B, Otis BP. 'A fully integrated RF-powered contact lens with a single element display.' IEEE Transactions on Biomedical Circuits and Systems 2010;4(6):454-461. (Inductive RF power harvesting at sub-microwatt budget on a custom CMOS IC integrated onto a contact lens, driving a single-pixel display, with bidirectional wireless data.)",
        creator="Jagdish Pandey / Yu-Te Liao / Andrew Lingley / Ramin Mirjalili / Babak Parviz / Brian Otis (University of Washington)",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea"],
        sensors=["sensor-camera-eye"],
        output_modalities=["visual-display", "data-only"],
        ip_status="public-domain",
        prior_art_notes=(
            "The canonical academic disclosure of a complete RF-powered wearable "
            "system on a contact lens: ambient-RF energy harvesting + custom "
            "sub-microwatt CMOS + integrated single-pixel display + bidirectional "
            "wireless data, all on a soft contact-lens substrate. Foundational prior "
            "art for any wearable claim reciting 'an ambient-RF-powered sub-microwatt "
            "CMOS system on a body-worn substrate' — covers not just contact-lens "
            "claims but the broader ambient-RF-powered wearable system architecture "
            "(applies to smart rings, hearables, patches, implants). Pair with later "
            "follow-ons by the same group and Pourshaban et al. for the dual-mode "
            "harvesting variant ([[pourshaban-2024-dual-mode-contact-lens-harvester]])."
        ),
        sources=[
            "Pandey J, et al. IEEE Trans Biomed Circuits Syst 2010;4(6):454-461.",
        ],
        cpc_classifications=["A61B 5/0031", "G02C 7/04", "H02J 50/12"],
    ),
    E(
        id="pourshaban-2024-dual-mode-contact-lens-harvester",
        canonical_name="Pourshaban et al. (2024) — dual-mode (solar + RF) energy-harvesting contact lens delivering 150 μW at 3.3 V",
        aliases=["Pourshaban dual-mode harvester", "contact lens solar+RF harvesting"],
        corpus="academic",
        first_disclosure_date="2024",
        disclosure_citation="Pourshaban E, et al. Dual-mode photovoltaic + RF harvesting contact lens delivering up to ~150 μW continuous power at 3.3 V into an 11 mF supercapacitor — combining solar harvesting (eyes open) with RF harvesting (eyes closed), on a 0.13 μm CMOS IC with ~0.2 mm² die area, ~47% RF-to-DC conversion efficiency. Work conducted at the University of Washington / now at Texas Instruments.",
        creator="Ehsan Pourshaban et al.",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea"],
        ip_status="public-domain",
        notes="Specific journal / DOI to be verified.",
        prior_art_notes=(
            "Discloses a dual-mode ambient energy-harvesting front-end for an on-eye "
            "contact lens combining photovoltaic harvesting (eye open) with "
            "inductively-coupled RF harvesting (eye closed) into a single supercapacitor-"
            "buffered power rail at ~150 μW continuous — the architectural template for "
            "any battery-free wearable that must operate continuously across changing "
            "ambient conditions. Prior art for ring/patch/implant claims reciting "
            "'a wearable with two or more energy-harvesting modalities operating "
            "complementarily with a shared energy buffer' from 2024."
        ),
        sources=[
            "Pourshaban E, et al. (2024). [Specific journal/DOI to be verified.]",
        ],
        cpc_classifications=["H02J 50/12", "H02S 40/38", "A61B 5/0031"],
    ),
    # ---------------- HAND / FINGER GESTURE INPUT ----------------
    E(
        id="tap-systems-tap-strap-2018",
        canonical_name="Tap Strap (Tap Systems, 2018) — finger-mounted gesture and keyboard input device",
        aliases=["Tap Strap", "Tap", "Tap Systems"],
        corpus="private",
        first_disclosure_date="2018",
        disclosure_citation="Tap Systems Inc. (founded 2014, Sherman Oaks, CA). 'Tap Strap' wearable input device, shipped 2018 — five finger-loops connected by a flexible band across the back of the hand, with accelerometers on each finger detecting tapping and gesture; mapped onto a virtual keyboard, mouse, and gesture commands via BLE. Successor 'Tap Strap 2' (2019) and 'TapXR' (a wrist version, 2023). https://www.tapwithus.com",
        creator="Tap Systems Inc. (founder: Dovid Schick)",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["ring", "armband"],
        contact_surface="skin",
        anatomical_target=["fingers", "hand"],
        sensors=["sensor-accelerometer"],
        algorithms=["algo-hand-gesture-emg"],
        clinical_endpoints=["finger-tap", "hand-gesture"],
        ip_status="patented",
        connectivity="ble",
        draft=True,
        notes="Draft: patent enumeration TODO. Form factor 'other' — multi-finger band, no exact match in current taxonomy (added form_factor_tags ring + armband as approximations).",
        prior_art_notes=(
            "Discloses a hand-worn device of multiple finger-loops linked by a back-of-"
            "hand band, with motion sensors on each finger detecting per-finger tap and "
            "swipe events and mapping them via BLE to a virtual keyboard / mouse / "
            "gesture protocol — wearable per-finger gesture input by motion sensing "
            "alone (no EMG). Directly relevant prior art for any finger/hand "
            "gesture-input wearable, including [[ctrl-labs-meta-wrist-emg-2018]] (EMG "
            "route), [[myo-armband-2014]] (forearm-EMG route), and ring-form gesture "
            "input devices. Anticipates per-finger-motion-sensor gesture-recognition "
            "wearable claims from 2018."
        ),
        sources=[
            "Tap Systems Inc., Tap Strap / Tap Strap 2 / TapXR (products, 2018-2023).",
        ],
        cpc_classifications=["G06F 3/014", "G06F 3/017", "A61B 5/1118"],
    ),
    # ---------------- OPEN ACADEMIC SMARTWATCH RESEARCH ----------------
    E(
        id="h-watch-magno-2024",
        canonical_name="H-Watch (Magno et al., 2024) — open-source ARM Cortex-M4F + ML + NB-IoT + energy-harvesting research smartwatch",
        aliases=["H-Watch", "Magno H-Watch"],
        corpus="academic",
        first_disclosure_date="2024",
        disclosure_citation="Magno M, et al. 'H-Watch: A Multi-Sensor Smart Wearable for COVID-19 Symptom Monitoring with ML and Energy Harvesting.' arXiv:2407.21501 (2024). Fully open-source smartwatch hardware + firmware for symptom monitoring: ARM Cortex-M4F MCU, on-device ML inference, NB-IoT cellular connectivity, integrated energy harvesting + battery. https://arxiv.org/abs/2407.21501",
        creator="Michele Magno et al. (ETH Zürich and collaborators)",
        creator_country="CH",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-spo2", "sensor-skin-temperature", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-spo2-estimation", "algo-respiratory-rate", "algo-activity-classification"],
        clinical_endpoints=["heart-rate", "blood-oxygen", "respiratory-rate", "skin-temperature"],
        ip_status="public-domain",
        connectivity="lte-m",
        prior_art_notes=(
            "Discloses a fully open-source research smartwatch combining multi-sensor "
            "vitals (PPG/SpO2/temperature/IMU), on-device ML inference, NB-IoT direct "
            "cellular connectivity (no phone required), and integrated energy harvesting "
            "to extend battery life — published with full hardware design and firmware. "
            "Prior art for symptom-monitoring smartwatch claims reciting any of those "
            "elements from 2024. Establishes that the cellular-connected open-hardware "
            "ML-enabled smartwatch is a published research design."
        ),
        sources=[
            "Magno M, et al. arXiv:2407.21501 (2024).",
        ],
        cpc_classifications=["A61B 5/0006", "A61B 5/02416", "G16H 50/20", "H04W 4/80"],
    ),
    E(
        id="cogwatch-2024-hardwarex",
        canonical_name="CogWatch (HardwareX, 2024) — open-source smartwatch for cognitive-load monitoring",
        aliases=["CogWatch"],
        corpus="academic",
        first_disclosure_date="2024",
        disclosure_citation="'CogWatch: An open-source smartwatch platform for cognitive-load monitoring.' HardwareX 19 (2024). Open-source smartwatch design — full hardware, firmware, and assembly documentation published in the open-hardware-focused journal HardwareX (Elsevier). https://www.hardware-x.com/article/S2468-0672(24)00032-4/fulltext",
        creator="(See HardwareX publication for full author list.)",
        creator_country="EU",
        form_factor="watch",
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-gsr", "sensor-accelerometer"],
        algorithms=["algo-hr", "algo-hrv", "algo-stress-index", "algo-cognitive-workload"],
        clinical_endpoints=["heart-rate", "heart-rate-variability", "electrodermal-activity", "cognitive-load"],
        ip_status="public-domain",
        notes="Full author list / volume number to be filled in from HardwareX article when verifying citation.",
        prior_art_notes=(
            "Discloses, as open-hardware (HardwareX is the canonical venue for full "
            "publication of open-hardware designs), a wrist-worn smartwatch instrumented "
            "for cognitive-load monitoring from PPG-derived HRV and EDA/GSR. Prior art "
            "for smartwatch-cognitive-load claims combining 'a wrist-worn device', "
            "'PPG and EDA sensors', and 'a derived cognitive-load metric' from 2024."
        ),
        sources=[
            "CogWatch. HardwareX 19 (2024) S2468-0672(24)00032-4.",
        ],
        cpc_classifications=["A61B 5/0531", "A61B 5/16", "A61B 5/02438"],
    ),
]


def main():
    existing = set()
    if CORPUS.exists() and CORPUS.stat().st_size:
        for line in CORPUS.read_text().splitlines():
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])
    added = skipped = 0
    with CORPUS.open("a") as f:
        for e in ENTRIES:
            if e["id"] in existing:
                skipped += 1
                continue
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
            added += 1
    print(f"  ingest r15: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
