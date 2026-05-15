#!/usr/bin/env python3
"""seed_2026q3_real_r8_breadth.py — breadth-expansion batch.

Targets the thinnest form factors on the real-product side: ingestible
(PillCam, Proteus/Abilify MyCite), contact-lens (Verily/Google glucose
lens, Mojo Vision AR lens), hearing-aid (Eargo OTC), armband (CTRL-labs
wrist EMG / neural interface), body-camera (Axon Body 2 / police body
cam). Plus the foundational ingestible-camera academic disclosure
(Iddan et al., Nature 2000).

Run from repo root:  python3 seeds/seed_2026q3_real_r8_breadth.py
Idempotent — skips ids already present.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


WORK = ("Draft: enumerate patent numbers and (where regulated) the exact FDA "
        "510(k)/De Novo/PMA identifiers, then promote to commons-grade.")


ENTRIES = [
    # ---------------- ACADEMIC: wireless capsule endoscopy ----------------
    E(
        id="iddan-2000-wireless-capsule-endoscopy",
        canonical_name="Iddan et al. (2000) — 'Wireless capsule endoscopy' (the foundational ingestible-camera disclosure)",
        aliases=["wireless capsule endoscopy", "PillCam concept paper", "Iddan capsule"],
        corpus="academic",
        first_disclosure_date="2000-05-25",
        disclosure_citation="Iddan G, Meron G, Glukhovsky A, Swain P. 'Wireless capsule endoscopy.' Nature 2000;405(6785):417.",
        creator="Gavriel Iddan / Gavriel Meron / Arkady Glukhovsky / Paul Swain (Given Imaging)",
        creator_country="IL",
        form_factor="ingestible",
        contact_surface="intra-abdominal",
        anatomical_target=["gastrointestinal-tract", "small-bowel"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["data-only"],
        ip_status="public-domain",
        prior_art_notes=(
            "Discloses a swallowable wireless capsule incorporating an imaging sensor, "
            "illumination, transmitter and battery that captures and transmits images of "
            "the gastrointestinal mucosa as it passes through the gut — i.e. the "
            "ingestible camera. Any claim reciting 'an ingestible capsule comprising an "
            "image sensor and a wireless transmitter for imaging the gastrointestinal "
            "tract' reads on Iddan et al. 2000. Anchor for the ingestible × camera "
            "cross-cut; product realization in [[pillcam-given-imaging-2001]]; cf. the "
            "fictional antecedents [[fantastic-voyage-intravascular-craft]] (1966) and "
            "[[the-matrix-navel-tracking-bug]] (1999)."
        ),
        sources=["Iddan G, Meron G, Glukhovsky A, Swain P. Nature 2000;405(6785):417."],
        cpc_classifications=["A61B 1/041", "A61B 1/00009", "A61B 5/0084", "A61B 5/073"],
    ),
    # ---------------- INGESTIBLE PRODUCTS ----------------
    E(
        id="pillcam-given-imaging-2001",
        canonical_name="PillCam SB (Given Imaging, 2001) — first FDA-cleared wireless capsule endoscope",
        aliases=["PillCam", "M2A capsule", "Given Imaging PillCam"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2001-08",
        disclosure_citation="Given Imaging Ltd. (later Medtronic). 'M2A' (subsequently 'PillCam SB') wireless capsule endoscope — FDA-cleared August 2001 — a swallowable capsule with a CMOS image sensor, LED illumination, battery and radio that images the small-bowel mucosa over 8 hours, transmitting frames to an external belt-worn receiver/recorder.",
        creator="Given Imaging Ltd. (founders Gavriel Iddan, Gavriel Meron)",
        creator_country="IL",
        form_factor="ingestible",
        contact_surface="intra-abdominal",
        anatomical_target=["gastrointestinal-tract", "small-bowel"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["data-only"],
        regulatory_pathway="fda-510k",
        lineage_ancestors=["iddan-2000-wireless-capsule-endoscopy"],
        notes="Draft. " + WORK + " Verify exact 510(k) (the M2A clearance, 2001).",
        prior_art_notes=(
            "Discloses the commercial ingestible imaging capsule: a swallowable CMOS-"
            "camera capsule with onboard illumination, battery and radio, imaging the GI "
            "mucosa during transit and streaming frames to a body-worn receiver/recorder. "
            "Product realization of [[iddan-2000-wireless-capsule-endoscopy]]; anticipates "
            "ingestible-camera claims from 2001. Anchor for the ingestible × camera "
            "cross-cut on the real side."
        ),
        sources=["Given Imaging Ltd., PillCam SB / M2A wireless capsule endoscope (product, 2001)."],
        cpc_classifications=["A61B 1/041", "A61B 1/00009", "A61B 1/00029", "A61B 5/073"],
    ),
    E(
        id="proteus-abilify-mycite-2017",
        canonical_name="Abilify MyCite (Otsuka / Proteus Digital Health, 2017) — first FDA-approved drug with an ingestible sensor (digital-pill / medication-adherence system)",
        aliases=["Abilify MyCite", "Proteus Digital Health", "ingestible event marker", "IEM"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2017-11-13",
        disclosure_citation="Otsuka Pharmaceutical Co., Ltd. and Proteus Digital Health, Inc. 'Abilify MyCite' (aripiprazole with embedded ingestible event marker), FDA-approved 13 November 2017 — the first drug-device combination approved by the FDA with an integrated ingestible sensor: a millimeter-scale sensor embedded in each tablet that activates on contact with stomach fluid and transmits to a skin-worn patch ('MyCite Patch'), which relays an ingestion event to a smartphone, confirming medication adherence.",
        creator="Otsuka Pharmaceutical Co. / Proteus Digital Health, Inc.",
        creator_country="US",
        form_factor="ingestible",
        form_factor_tags=["patch"],
        contact_surface="intra-abdominal",
        anatomical_target=["stomach", "torso"],
        sensors=["sensor-bioimpedance"],
        clinical_endpoints=["ingestion-event", "medication-adherence"],
        regulatory_pathway="fda-pma",
        notes="Draft. " + WORK + " The Proteus Discover platform's underlying ingestible-event-marker has its own FDA history (2012); verify the exact identifiers. Proteus filed for bankruptcy 2020 and its IP went to Otsuka.",
        prior_art_notes=(
            "Discloses a drug-device combination in which each medication tablet "
            "incorporates a tiny edible sensor that activates on contact with stomach "
            "fluid (powered by the electrochemical reaction with stomach acid), "
            "communicating an ingestion event to a skin-mounted receiver patch that "
            "relays it to a smartphone. The first FDA-approved digital-pill / "
            "medication-adherence-tracking system. Anticipates ingestible-sensor "
            "medication-adherence claims combining 'an ingestible sensor embedded in or "
            "co-delivered with a pharmaceutical', 'a skin-worn receiver/patch', and "
            "'transmission of an ingestion-event record' from 2017. Anchor for the "
            "ingestible × adherence cross-cut."
        ),
        sources=["Otsuka / Proteus, Abilify MyCite (product/regulatory, 2017)."],
        cpc_classifications=["A61B 5/073", "A61B 5/0008", "A61J 7/0481", "G16H 20/13"],
    ),
    # ---------------- CONTACT-LENS PRODUCTS ----------------
    E(
        id="verily-google-smart-contact-lens-2014",
        canonical_name="Google[X] / Verily smart contact lens (2014) — tear-glucose-sensing contact lens project",
        aliases=["Google smart contact lens", "Verily glucose contact lens", "Google[X] contact lens"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2014-01-16",
        disclosure_citation="Google[X] (Brian Otis, Babak Parviz). 'Smart contact lens' project, publicly disclosed 16 January 2014 — a soft contact lens with an embedded miniature glucose sensor, antenna, and wireless interface to a phone, intended to continuously measure tear glucose. Later transferred to Verily (Alphabet's life-sciences arm) and licensed to Novartis/Alcon; the program was reported wound down c. 2018 without a shipping product, but the underlying patent estate (Otis et al., Parviz et al.; e.g. US 8,608,310; US 9,184,698 and continuations) is extensive.",
        creator="Google[X] / Verily Life Sciences (Brian Otis, Babak Parviz, et al.)",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea", "tear-film"],
        sensors=["sensor-glucose-cgm", "sensor-optical-glucose"],
        algorithms=["algo-glucose-noninvasive"],
        clinical_endpoints=["tear-glucose"],
        lineage_ancestors=["yao-parviz-2011-contact-lens-glucose-sensor"],
        notes="Draft. " + WORK + " The product never shipped, but the disclosure (the 2014 announcement, the patents, the licensing agreements) is firmly in the public record and is heavily cited in subsequent smart-contact-lens patents.",
        prior_art_notes=(
            "Discloses a soft contact lens with an embedded miniature electrochemical "
            "glucose sensor, antenna, and wireless interface for continuous tear-glucose "
            "monitoring — a major industrial follow-on to [[yao-parviz-2011-contact-lens-"
            "glucose-sensor]]. Anticipates smart-contact-lens claims combining 'a soft "
            "ophthalmic lens', 'an embedded biosensor', and 'wireless transmission of "
            "the sensed analyte' from 2014; the extensive associated patent family is "
            "itself prior art on most subsequent contact-lens-biosensor and embedded-"
            "lens-electronics claims. Product-side anchor for the contact-lens × "
            "biosensor cross-cut."
        ),
        sources=["Google[X] / Verily, smart contact lens project (announcement, 2014)."],
        cpc_classifications=["G02C 7/04", "A61B 5/14532", "A61B 5/1455", "A61B 3/16"],
    ),
    E(
        id="mojo-vision-ar-contact-lens-2022",
        canonical_name="Mojo Vision Mojo Lens (2022) — wearable AR contact lens with embedded microLED display",
        aliases=["Mojo Lens", "Mojo Vision"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2022-06",
        disclosure_citation="Mojo Vision, Inc. 'Mojo Lens', publicly demonstrated June 2022 — a scleral contact lens with an embedded ~14k-PPI microLED display in the wearer's central field of view, an ARM Cortex processor, eye-tracking via motion sensors, a magnetometer for gaze direction, a microwave radio for offload, and a wirelessly charged battery; rendering an AR information overlay on the cornea. (The consumer AR-glucose pivot followed; production halted c. 2023.)",
        creator="Mojo Vision, Inc.",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea", "sclera"],
        sensors=["sensor-accelerometer", "sensor-gyroscope", "sensor-magnetometer"],
        algorithms=["algo-eye-gaze-tracking"],
        output_modalities=["visual-display"],
        lineage_ancestors=["rainbows-end-ar-contact-lens", "mi-ghost-protocol-contact-lens-camera"],
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a contact lens with an embedded microLED display in the central "
            "visual field, on-lens processing, gaze tracking via inertial/magnetic "
            "sensors, wireless RF link, and a wirelessly charged on-lens battery — i.e. "
            "an AR display contact lens worn on the cornea. Anticipates AR-contact-lens "
            "claims combining 'a contact lens', 'an embedded near-eye microdisplay', "
            "'on-lens processing and motion sensors for gaze', and 'a wireless link' "
            "from 2022. Product-side anchor for the contact-lens × visual-display "
            "cross-cut; cf. [[rainbows-end-ar-contact-lens]] (the 2006 fictional "
            "anticipation)."
        ),
        sources=["Mojo Vision, Inc., Mojo Lens (product/demo, 2022)."],
        cpc_classifications=["G02C 7/04", "G02B 27/01", "G06F 3/01", "A61B 3/113"],
    ),
    # ---------------- HEARING AID ----------------
    E(
        id="eargo-otc-hearing-aid-2017",
        canonical_name="Eargo (2017) — direct-to-consumer rechargeable in-canal hearing aid",
        aliases=["Eargo", "Eargo hearing aid"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2015-09",
        disclosure_citation="Eargo, Inc. 'Eargo Plus' (and successor models — Eargo Neo, Eargo 5, Eargo 7, Eargo 8), launched 2015–2017 in the US as a direct-to-consumer rechargeable invisible-in-canal hearing aid sold without an audiologist gatekeeper, with self-fit via a mobile app — predating the 2022 FDA OTC hearing-aid final rule (21 CFR 800.30) and the [[apple-airpods-pro-2-hearing-health-2024]] entry by years.",
        creator="Eargo, Inc.",
        creator_country="US",
        form_factor="hearing-aid",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        actuators=["audio"],
        output_modalities=["audio"],
        regulatory_pathway="fda-510k",
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a direct-to-consumer rechargeable invisible-in-canal hearing aid "
            "with self-fitting via a mobile app, sold and adjusted by the wearer without "
            "an audiologist — i.e. consumer-grade self-fit hearing aid years before the "
            "FDA's 2022 OTC hearing-aid rule. Anticipates self-fitting and "
            "direct-to-consumer hearing-aid claims from 2015–2017. Product-side anchor "
            "for the hearing-aid cross-cut on the real side (the only fictional entry is "
            "[[bionic-woman-bionic-ear]])."
        ),
        sources=["Eargo, Inc. (product, 2015 onward)."],
        cpc_classifications=["H04R 25/00", "H04R 25/70", "H04R 25/55"],
    ),
    # ---------------- ARMBAND / WRIST EMG ----------------
    E(
        id="ctrl-labs-meta-wrist-emg-2018",
        canonical_name="CTRL-labs (later Meta) wrist surface-EMG band (2018) — neural-interface wristband for finger/hand intent decoding",
        aliases=["CTRL-labs", "Meta wristband", "CTRL-kit", "Reardon EMG band"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2018-10",
        disclosure_citation="CTRL-Labs Corp. (Thomas Reardon, Patrick Kaifosh, Tim Machado) — surface-EMG wristband ('CTRL-kit') publicly demonstrated October 2018 at TechCrunch Disrupt and elsewhere: a wrist-worn band of dry EMG electrodes that decodes individual motor-unit firings on the wrist/forearm to infer finger/hand intent (including individuated finger movement and even imagined movement) as an input modality. CTRL-labs was acquired by Facebook (later Meta) in September 2019; the Meta production wristband for AR glasses is the descendant.",
        creator="CTRL-Labs Corp. (Thomas Reardon, Patrick Kaifosh, Tim Machado); later Meta Reality Labs",
        creator_country="US",
        form_factor="armband",
        form_factor_tags=["watch"],
        contact_surface="skin",
        anatomical_target=["wrist", "forearm"],
        sensors=["sensor-emg", "sensor-dry-eeg-electrode"],
        algorithms=["algo-hand-gesture-emg", "algo-keystroke-emg"],
        clinical_endpoints=["motor-intent", "individual-motor-unit-firing", "finger-gesture"],
        lineage_ancestors=["englehart-hudgins-2003-myoelectric-control", "myo-armband-2014"],
        notes="Draft. " + WORK + " The CTRL-labs / Meta patent estate (Reardon et al.) is large and central to neural-input-wristband claims.",
        prior_art_notes=(
            "Discloses a wrist-worn band of dry surface-EMG electrodes that decodes "
            "individual motor-unit firings to infer fine finger and hand intent — "
            "including individuated single-finger motions and 'imagined' movements with "
            "no overt muscle contraction — as a continuous neural-control input "
            "modality. Distinct from gross-gesture EMG decoders ([[myo-armband-2014]]) "
            "in its motor-unit-level resolution. Anticipates neural-interface-wristband "
            "claims combining 'a wrist band of surface-EMG electrodes', 'motor-unit-"
            "level decoding', and 'individual finger / imagined-movement output' from "
            "2018. Product-side anchor for the wrist × EMG × neural-input cross-cut; "
            "the Meta production wristband descends from it."
        ),
        sources=["CTRL-Labs Corp., CTRL-kit wristband (demonstrations, 2018); Meta Reality Labs (acquirer, 2019)."],
        cpc_classifications=["A61B 5/389", "G06F 3/015", "G06F 3/017", "A61B 5/24"],
    ),
    # ---------------- BODY-CAMERA ----------------
    E(
        id="axon-body-2-police-bodycam-2016",
        canonical_name="Axon Body 2 (2016) — networked law-enforcement body-worn camera with cloud digital-evidence chain of custody",
        aliases=["Axon Body 2", "TASER Axon body camera", "police body cam"],
        corpus="private",
        ip_status="patented",
        draft=True,
        first_disclosure_date="2016-06",
        disclosure_citation="Axon Enterprise, Inc. (formerly TASER International). 'Axon Body 2' body-worn camera, released 2016 — a chest-mounted body camera with HD video, infrared night vision, ambient audio, pre-event buffering (the prior 30-120 s of video kept and saved on trigger), wireless LTE upload, GPS, and integrated cloud chain-of-custody on the Evidence.com platform.",
        creator="Axon Enterprise, Inc. (formerly TASER International)",
        creator_country="US",
        form_factor="body-camera",
        form_factor_tags=["garment"],
        contact_surface="textile-mediated",
        anatomical_target=["chest"],
        sensors=["sensor-camera-rgb", "sensor-camera-ir", "sensor-microphone-air"],
        output_modalities=["data-only"],
        connectivity="lte-m",
        notes="Draft. " + WORK,
        prior_art_notes=(
            "Discloses a chest-worn networked law-enforcement body camera with HD video, "
            "IR night vision, audio, a pre-event circular buffer (capturing seconds "
            "before activation), GPS, wireless upload, and integrated cloud chain-of-"
            "custody. Anticipates body-worn-camera claims combining 'a chest-mounted "
            "camera', 'a continuous pre-event buffer with retrospective save on "
            "trigger', 'wireless upload to an evidence-management cloud service', and "
            "'cryptographic chain of custody' from 2016. Product-side anchor for the "
            "body-camera cross-cut on the real side; cf. [[aliens-marine-helmet-cam]] "
            "(the 1986 fictional networked-body-cam antecedent)."
        ),
        sources=["Axon Enterprise, Inc., Axon Body 2 (product, 2016)."],
        cpc_classifications=["H04N 5/77", "H04N 7/18", "G06F 21/64", "G07C 9/00"],
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
    print(f"  real breadth r8: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
