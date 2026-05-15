#!/usr/bin/env python3
"""seed_2026q3_fiction_r2.py — fictional seed batch round 2.

Rings, hearables, garments/footwear, plus deeper eyewear and
body-measurement. Run from repo root:

    python3 seeds/seed_2026q3_fiction_r2.py

Idempotent — skips ids already present.

Doctrinal note (same as round 1): fictional disclosures are generally
non-enabling; their prior-art value is § 103 motivation-to-combine, not
§ 102 anticipation. prior_art_notes say so where relevant.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("corpus", "fictional")
    kw.setdefault("ip_status", "fictional")
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    # ---------------- RINGS ----------------
    E(
        id="green-lantern-power-ring",
        canonical_name="Green Lantern power ring",
        aliases=["GL ring", "power ring"],
        first_disclosure_date="1940-07",
        disclosure_citation="All-American Comics #16 (cover date July 1940), DC Comics; the finger-worn 'power ring' that responds to the wearer's will and must be periodically recharged from a separate power source ('the lantern').",
        creator="Martin Nodell / Bill Finger / DC Comics",
        creator_country="US",
        form_factor="ring",
        tier=2,
        prior_art_notes=(
            "Reference-only. Documents a finger-worn device that (a) is controlled by the "
            "wearer's intent/will rather than by buttons, and (b) requires periodic "
            "recharging by contact with a dedicated charging fixture. Thin as prior art — "
            "no physiological sensing — but contributes the 'ring as a will-controlled, "
            "rechargeable, finger-worn appliance' concept circa 1940 to the smart-ring "
            "form-factor cross-cut. Promote to Tier 1 if a sensing/measurement reading "
            "is added."
        ),
        sources=[
            "Nodell, Martin; Finger, Bill. All-American Comics #16. DC Comics, 1940.",
        ],
        cpc_classifications=["G06F 1/163", "G06F 3/01"],
    ),
    E(
        id="kingsman-signet-ring",
        canonical_name="Kingsman signet ring (electroshock ring)",
        aliases=["Kingsman shock ring"],
        first_disclosure_date="2014-12-13",
        disclosure_citation="Kingsman: The Secret Service (20th Century Fox / Marv Films), 2014; the agency signet ring that delivers a high-voltage electric shock on hand contact.",
        creator="Matthew Vaughn / Marv Films",
        creator_country="GB",
        form_factor="ring",
        contact_surface="skin",
        anatomical_target=["finger"],
        actuators=["electrical-stim-tens"],
        output_modalities=["electrical-stim"],
        prior_art_notes=(
            "Discloses a finger-worn ring whose function is to deliver an electrical "
            "stimulus through the wearer's hand on contact — a ring-form electrical-output "
            "device. Relevant to ring-form-factor claims combining 'a ring body', "
            "'electrodes exposed at the ring surface', and 'circuitry configured to apply "
            "an electrical stimulus' (defensive personal-shock rings; ring-form "
            "neuromuscular-stimulation devices). § 103 motivation that the electrical-output "
            "ring was an articulated objective by 2014. Thin: no sensing element."
        ),
        sources=[
            "Kingsman: The Secret Service (film). 20th Century Fox / Marv Films, 2014.",
        ],
        cpc_classifications=["G06F 1/163", "A61N 1/04", "F41H 13/00"],
    ),
    # ---------------- BRACELET ----------------
    E(
        id="black-panther-kimoyo-beads",
        canonical_name="Black Panther 'Kimoyo beads'",
        aliases=["Kimoyo bracelet", "Wakandan beads"],
        first_disclosure_date="2018-02-16",
        disclosure_citation="Black Panther (Marvel Studios), released February 16, 2018; the wrist-worn 'Kimoyo beads' — bracelet beads providing voice/holographic communication, holographic information display, remote vehicle/device control, and on-body medical diagnostics and treatment.",
        creator="Marvel Studios",
        creator_country="US",
        form_factor="bracelet",
        form_factor_tags=["pendant"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        clinical_endpoints=["multi-parameter-vitals", "injury-assessment"],
        output_modalities=["visual-display", "audio", "data-only"],
        connectivity="ubiquitous wireless mesh (fictional)",
        prior_art_notes=(
            "Discloses a wrist-worn bracelet of modular beads functioning as (a) a "
            "voice/visual communicator, (b) a projected holographic display surface, (c) a "
            "remote controller for paired vehicles and devices, and (d) an on-body medical "
            "scanner reporting injury and physiological state. Relevant to bracelet/"
            "wristband claims combining 'a band of modular elements', 'a display', 'a "
            "wireless transceiver for device control', and 'sensors for physiological "
            "measurement'. § 103 motivation that the multifunction medical/communication "
            "wrist bracelet was an articulated objective by 2018."
        ),
        sources=[
            "Black Panther (film). Marvel Studios, 2018.",
        ],
        cpc_classifications=["G06F 1/163", "A61B 5/00", "G08C 17/02"],
    ),
    # ---------------- HEARABLES ----------------
    E(
        id="fahrenheit-451-seashell-radio",
        canonical_name="Fahrenheit 451 'Seashell' ear radios",
        aliases=["Seashell radio", "thimble radio"],
        first_disclosure_date="1953-10-19",
        disclosure_citation="Bradbury, Ray. Fahrenheit 451. Ballantine Books, 1953 — the 'Seashell' ear-thimble radios worn in the ear delivering a continuous stream of broadcast audio.",
        creator="Ray Bradbury",
        creator_country="US",
        form_factor="earbud",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        actuators=["audio"],
        output_modalities=["audio"],
        connectivity="broadcast receiver (fictional)",
        prior_art_notes=(
            "Earliest broadly-disseminated depiction of a small, in-ear, wireless audio "
            "device worn habitually for continuous audio streaming — the 'wireless earbud' "
            "concept. Discloses the in-ear form-factor element and the 'continuous wireless "
            "audio reception' element of modern hearable claims. § 103 motivation that a "
            "habitually-worn in-ear wireless audio device was an articulated objective by "
            "1953. Non-enabling on the transceiver/transducer; pair with enabling "
            "miniature-receiver art."
        ),
        sources=[
            "Bradbury, Ray. Fahrenheit 451. Ballantine Books, 1953.",
        ],
        cpc_classifications=["H04R 1/10", "H04R 25/00"],
    ),
    E(
        id="star-trek-tos-uhura-earpiece",
        canonical_name="Star Trek (TOS) bridge communications earpiece",
        aliases=["Uhura earpiece", "Starfleet comm earpiece"],
        first_disclosure_date="1966-09-08",
        disclosure_citation="Star Trek (The Original Series), premiered September 8, 1966; the in-ear wireless receiver worn at the communications station to monitor incoming transmissions.",
        creator="Gene Roddenberry / Desilu Productions",
        creator_country="US",
        form_factor="earbud",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        actuators=["audio"],
        output_modalities=["audio"],
        connectivity="ship comms (fictional)",
        lineage_ancestors=["fahrenheit-451-seashell-radio"],
        prior_art_notes=(
            "Discloses a single-ear wireless audio receiver worn during operation to "
            "monitor a communication channel hands-free — a working depiction of the "
            "in-ear wireless comms earpiece. § 103 motivation that the single-ear wireless "
            "monitoring earpiece was an articulated objective by 1966."
        ),
        sources=[
            "Star Trek (The Original Series). Desilu Productions / Paramount, 1966.",
        ],
        cpc_classifications=["H04R 1/10", "H04M 1/05"],
    ),
    E(
        id="hitchhikers-babel-fish",
        canonical_name="The Hitchhiker's Guide to the Galaxy 'Babel fish'",
        aliases=["Babel fish"],
        first_disclosure_date="1978-03-08",
        disclosure_citation="Adams, Douglas. The Hitchhiker's Guide to the Galaxy (BBC Radio 4 series), first episode broadcast March 8, 1978 (novelisation 1979) — a small organism placed in the ear that performs real-time, two-way translation of any spoken language for the wearer.",
        creator="Douglas Adams",
        creator_country="GB",
        form_factor="earbud",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        actuators=["audio"],
        output_modalities=["audio"],
        notes="No algorithm tag exists for speech translation; the disclosure is captured in prior_art_notes.",
        prior_art_notes=(
            "Discloses an in-ear device that performs continuous, real-time, two-way speech "
            "translation between languages, delivering the translated audio directly into "
            "the ear canal — i.e. the 'real-time translation earbud'. Relevant to hearable "
            "claims combining 'an in-ear housing', 'a microphone capturing speech in a "
            "source language', 'a translation engine', and 'a speaker rendering the target "
            "language'. § 103 motivation that the in-ear real-time translation device was "
            "an articulated objective by 1978 (well prior to commercial translate-earbud "
            "patents). Non-enabling on the translation engine; pair with enabling "
            "machine-translation art."
        ),
        sources=[
            "Adams, Douglas. The Hitchhiker's Guide to the Galaxy (radio series). BBC Radio 4, 1978.",
            "Adams, Douglas. The Hitchhiker's Guide to the Galaxy (novel). Pan Books, 1979. ISBN 0-330-25864-8.",
        ],
        cpc_classifications=["H04R 1/10", "G06F 40/58", "G10L 15/00"],
    ),
    E(
        id="her-samantha-earpiece",
        canonical_name="Her — 'Samantha' in-ear conversational AI",
        aliases=["Samantha OS1 earpiece"],
        first_disclosure_date="2013-10-12",
        disclosure_citation="Her (Annapurna Pictures / Warner Bros.), 2013; the in-ear earpiece through which the wearer continuously converses with an adaptive AI assistant ('Samantha') that infers the wearer's emotional state from voice and context.",
        creator="Spike Jonze / Annapurna Pictures",
        creator_country="US",
        form_factor="earbud",
        contact_surface="ear",
        anatomical_target=["ear-canal"],
        sensors=["sensor-microphone-air"],
        algorithms=["algo-emotion-recognition"],
        actuators=["audio"],
        output_modalities=["audio"],
        connectivity="mobile network (fictional)",
        lineage_ancestors=["star-trek-tos-uhura-earpiece"],
        prior_art_notes=(
            "Discloses an habitually-worn in-ear device that is the user's continuous "
            "interface to a conversational AI assistant, including the assistant inferring "
            "the user's emotional/affective state from voice prosody and conversational "
            "context. Relevant to hearable claims combining 'an in-ear device', 'a "
            "microphone', 'a wireless link to a conversational agent', and 'affect "
            "estimation from captured speech'. § 103 motivation that the always-worn "
            "AI-assistant earbud with affect sensing was an articulated objective by 2013."
        ),
        sources=[
            "Her (film). Annapurna Pictures / Warner Bros., 2013.",
        ],
        cpc_classifications=["H04R 1/10", "G06F 3/16", "G10L 25/63"],
    ),
    # ---------------- GARMENTS / FOOTWEAR ----------------
    E(
        id="dune-stillsuit",
        canonical_name="Dune 'stillsuit' (body-moisture reclamation garment)",
        aliases=["stillsuit"],
        first_disclosure_date="1965-08-01",
        disclosure_citation="Herbert, Frank. Dune. Chilton Books, 1965 — a full-body garment with layered reclamation membranes that capture perspiration, respiration moisture, and other body fluids, filter and recycle the water, and monitor fit and function so the wearer can survive desert exposure.",
        creator="Frank Herbert",
        creator_country="US",
        form_factor="garment",
        contact_surface="skin",
        sensors=["sensor-microfluidic-sweat-collection", "sensor-sweat-rate"],
        algorithms=["algo-hydration-status"],
        clinical_endpoints=["hydration-status", "fluid-balance"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a body-conforming garment with integrated microfluidic channels "
            "that collect and process perspiration (and other body fluids) from the skin "
            "surface, with monitoring of collection rate, fit, and the wearer's hydration "
            "state. Directly relevant to sweat-collecting / sweat-analysis wearable claims "
            "combining 'a skin-contacting garment or patch', 'microfluidic channels to "
            "collect perspiration', and 'a determination of hydration or fluid balance'. "
            "§ 103 motivation that the sweat-collecting body garment with hydration "
            "monitoring was an articulated objective by 1965 — decades before the "
            "epidermal-microfluidics patent wave. Non-enabling on the membrane chemistry; "
            "pair with enabling microfluidic-sweat-sensor art."
        ),
        sources=[
            "Herbert, Frank. Dune. Chilton Books, 1965.",
        ],
        cpc_classifications=["A61B 5/145", "A61B 10/0064", "A41D 13/00"],
    ),
    E(
        id="bttf2-self-drying-jacket",
        canonical_name="Back to the Future Part II self-drying / auto-sizing jacket",
        aliases=["Marty McFly jacket", "self-drying jacket"],
        first_disclosure_date="1989-11-22",
        disclosure_citation="Back to the Future Part II (Universal Pictures), released November 22, 1989; the jacket that automatically adjusts to fit the wearer ('size adjusting') and, on detecting that it is wet, runs a powered drying cycle and announces 'Jacket drying'.",
        creator="Robert Zemeckis / Universal Pictures",
        creator_country="US",
        form_factor="garment",
        contact_surface="skin",
        actuators=["thermal"],
        output_modalities=["thermal", "audio", "data-only"],
        notes="No moisture-sensor tag exists; the wetness-detection element is captured in prior_art_notes.",
        prior_art_notes=(
            "Discloses a garment that (a) senses its own state (wet vs. dry; fit vs. "
            "loose), (b) actuates in response — a powered drying cycle, a size-adjustment "
            "mechanism — and (c) reports status to the wearer. Relevant to smart-garment "
            "claims combining 'a wearable garment', 'a sensor detecting a garment "
            "condition', 'an actuator (heating element / fit adjuster) responsive to the "
            "sensor', and 'a status output'. § 103 motivation that the sensing-and-"
            "actuating smart garment was an articulated objective by 1989."
        ),
        sources=[
            "Back to the Future Part II (film). Universal Pictures, 1989.",
        ],
        cpc_classifications=["A41D 13/005", "D06F 58/00", "G06F 1/163"],
    ),
    E(
        id="bttf2-power-laces-shoes",
        canonical_name="Back to the Future Part II self-lacing 'power laces' shoes",
        aliases=["Nike Mag power laces (fictional)", "self-lacing sneakers"],
        first_disclosure_date="1989-11-22",
        disclosure_citation="Back to the Future Part II (Universal Pictures), released November 22, 1989; the powered footwear that automatically tightens its laces around the wearer's foot on being put on ('power laces').",
        creator="Robert Zemeckis / Universal Pictures",
        creator_country="US",
        form_factor="shoe",
        contact_surface="skin",
        anatomical_target=["foot"],
        actuators=["motorized-lacing"],
        output_modalities=["data-only"],
        notes="Subsequently cited by Nike's own self-lacing-shoe development (HyperAdapt / Adapt BB).",
        prior_art_notes=(
            "Discloses powered footwear with a motor-driven fastening system that detects "
            "foot insertion and automatically adjusts lace tension to fit. Relevant to "
            "footwear claims combining 'a shoe', 'a powered tensioning mechanism', 'a "
            "sensor detecting the wearer's foot', and 'a controller adjusting fit'. § 103 "
            "motivation that the self-adjusting powered shoe was an articulated objective "
            "by 1989, well prior to the modern powered-footwear patent estate."
        ),
        sources=[
            "Back to the Future Part II (film). Universal Pictures, 1989.",
        ],
        cpc_classifications=["A43C 11/00", "A43B 3/34", "A43B 3/00"],
    ),
    E(
        id="ready-player-one-haptic-suit",
        canonical_name="Ready Player One full-body haptic suit and visor",
        aliases=["OASIS haptic suit", "X1 Boots and gloves"],
        first_disclosure_date="2011-08-16",
        disclosure_citation="Cline, Ernest. Ready Player One. Crown Publishers, 2011 — a head-mounted VR visor plus a full-body haptic-feedback suit (with haptic gloves and boots) that renders touch sensations across the wearer's body and tracks body motion for immersive virtual presence.",
        creator="Ernest Cline",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["goggles"],
        contact_surface="skin",
        sensors=["sensor-accelerometer", "sensor-gyroscope"],
        actuators=["haptic-eccentric", "haptic-piezo"],
        output_modalities=["haptic", "visual-display", "audio"],
        prior_art_notes=(
            "Discloses an integrated VR rig: a near-eye display visor plus a full-body "
            "garment with distributed haptic actuators and distributed motion sensors, "
            "providing whole-body force/tactile feedback registered to a virtual "
            "environment and capturing the wearer's posture and gestures. Relevant to "
            "haptic-garment claims combining 'a body-worn garment', 'an array of haptic "
            "actuators at multiple body sites', 'motion sensors capturing body pose', and "
            "'coupling to a head-mounted display'. § 103 motivation that the full-body "
            "haptic VR suit was an articulated objective by 2011."
        ),
        sources=[
            "Cline, Ernest. Ready Player One. Crown Publishers, 2011. ISBN 0-307-88743-6.",
        ],
        cpc_classifications=["G06F 3/01", "A41D 1/00", "G02B 27/01"],
    ),
    E(
        id="stark-iron-spider-suit",
        canonical_name="Stark 'Iron Spider' suit with mask HUD and AI ('Karen')",
        aliases=["Iron Spider suit", "Stark Spider-Man suit", "Karen suit"],
        first_disclosure_date="2017-07-07",
        disclosure_citation="Spider-Man: Homecoming (Marvel Studios / Sony), released July 7, 2017; the Stark-built suit with an in-mask heads-up display, an integrated conversational AI ('Karen'), distributed suit sensors, environmental analysis, biometric monitoring of the wearer, a deployable drone, and configurable web-shooter telemetry.",
        creator="Marvel Studios / Sony Pictures",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["goggles"],
        contact_surface="skin",
        sensors=["sensor-camera-rgb", "sensor-accelerometer", "sensor-microphone-air"],
        clinical_endpoints=["heart-rate", "respiratory-rate"],
        algorithms=["algo-emotion-recognition"],
        output_modalities=["visual-display", "audio", "data-only"],
        connectivity="cellular/satellite (fictional)",
        prior_art_notes=(
            "Discloses a smart full-body garment integrating: an in-mask near-eye HUD; a "
            "conversational AI assistant resident in the suit; distributed suit sensors and "
            "environmental analysis (object/person identification, threat assessment); "
            "biometric monitoring of the wearer (HR, respiration, stress); and reconfigurable "
            "actuator/output settings. Relevant to smart-garment and helmet-HUD claims "
            "combining 'a body-worn garment with distributed sensors', 'a head-mounted "
            "display presenting environmental and physiological data', 'a voice AI', and "
            "'wearer biometric monitoring'. § 103 motivation that the integrated "
            "sensing/HUD/AI body suit was an articulated objective by 2017."
        ),
        sources=[
            "Spider-Man: Homecoming (film). Marvel Studios / Sony Pictures, 2017.",
        ],
        cpc_classifications=["G02B 27/01", "A61B 5/00", "G06F 3/16", "A41D 1/00"],
    ),
    E(
        id="get-smart-shoe-phone",
        canonical_name="Get Smart shoe phone",
        aliases=["Maxwell Smart shoe phone"],
        first_disclosure_date="1965-09-18",
        disclosure_citation="Get Smart (NBC television series), premiered September 18, 1965; a telephone concealed in and integrated with the heel of a shoe.",
        creator="Mel Brooks / Buck Henry / Talent Associates",
        creator_country="US",
        form_factor="shoe",
        tier=2,
        actuators=["audio"],
        output_modalities=["audio"],
        prior_art_notes=(
            "Reference-only. Documents electronics — a working telephone — integrated into "
            "the structure of footwear, contributing the 'shoe as an electronics host "
            "platform' concept circa 1965 to the smart-shoe form-factor cross-cut. Thin: "
            "no sensing or measurement. Promote to Tier 1 if a footwear-integrated "
            "sensing/measurement reading is added (e.g. as antecedent to gait/pressure "
            "smart-shoe claims)."
        ),
        sources=[
            "Get Smart. Talent Associates / NBC, 1965-1970.",
        ],
        cpc_classifications=["A43B 3/00", "H04M 1/05"],
    ),
    # ---------------- DEEPER EYEWEAR / HELMET HUD ----------------
    E(
        id="aliens-marine-helmet-cam",
        canonical_name="Aliens — Colonial Marine helmet camera with live command feed",
        aliases=["M3 helmet cam", "Colonial Marine helmet camera"],
        first_disclosure_date="1986-07-18",
        disclosure_citation="Aliens (20th Century Fox), released July 18, 1986; each Colonial Marine's helmet carries a camera and light that streams live video to a remote tactical console where a commander monitors all squad feeds simultaneously and issues instructions.",
        creator="James Cameron / 20th Century Fox",
        creator_country="US",
        form_factor="helmet",
        form_factor_tags=["body-camera"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["data-only"],
        connectivity="wireless video uplink (fictional)",
        prior_art_notes=(
            "Discloses head-worn cameras on multiple wearers each streaming live first-"
            "person video over a wireless link to a single remote monitoring station that "
            "displays all feeds and supports two-way command communication — i.e. the "
            "body-worn-camera-to-remote-command-center system. Relevant to claims combining "
            "'a head- or body-worn camera', 'wireless transmission of the video to a remote "
            "device', and 'a console displaying multiple wearers' feeds for supervision'. "
            "§ 103 motivation that networked body-worn camera supervision was an articulated "
            "objective by 1986, prior to the modern body-camera and tele-supervision "
            "patent space."
        ),
        sources=[
            "Aliens (film). 20th Century Fox, 1986.",
        ],
        cpc_classifications=["H04N 7/18", "G02B 27/01", "A42B 3/04"],
    ),
    E(
        id="robocop-targeting-hud",
        canonical_name="RoboCop helmet HUD with recording and database lookup",
        aliases=["RoboCop visor display", "RoboCop targeting display"],
        first_disclosure_date="1987-07-17",
        disclosure_citation="RoboCop (Orion Pictures), released July 17, 1987; the cyborg officer's helmet-integrated heads-up display providing targeting reticles, continuous video recording of the wearer's view, and real-time identification of persons against a records database.",
        creator="Paul Verhoeven / Orion Pictures",
        creator_country="US",
        form_factor="helmet",
        form_factor_tags=["body-camera"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["visual-display", "data-only"],
        notes="No facial-recognition algorithm tag exists; the database-lookup element is captured in prior_art_notes.",
        prior_art_notes=(
            "Discloses a helmet-integrated near-eye HUD that (a) overlays targeting/aiming "
            "graphics on the wearer's view, (b) continuously records that view, and (c) "
            "performs real-time identification of people in view by querying a records "
            "database and displaying the match. Relevant to helmet/eyewear claims combining "
            "'a head-mounted display', 'an outward camera', 'video recording', and 'on-view "
            "person identification against a database'. § 103 motivation that the "
            "recording, identifying helmet HUD was an articulated objective by 1987."
        ),
        sources=[
            "RoboCop (film). Orion Pictures, 1987.",
        ],
        cpc_classifications=["G02B 27/01", "G06V 40/16", "A42B 3/04", "H04N 5/77"],
    ),
    # ---------------- BODY MEASUREMENT (own cross-cut) ----------------
    E(
        id="star-trek-borg-implants",
        canonical_name="Star Trek Borg cybernetic implant suite",
        aliases=["Borg implants", "Borg ocular implant", "Borg cortical node"],
        first_disclosure_date="1989-05-08",
        disclosure_citation="Star Trek: The Next Generation, 'Q Who' (first aired May 8, 1989); the Borg — humanoids fitted with an integrated suite of cybernetic implants: an ocular sensor implant, a cortical processing node, continuous physiological regulation, and a permanent network link to a collective.",
        creator="Maurice Hurley / Paramount Television",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["eye", "skull", "spine", "limb"],
        sensors=["sensor-camera-ir"],
        clinical_endpoints=["multi-parameter-vitals", "metabolic-state"],
        output_modalities=["visual-display", "data-only"],
        connectivity="collective network link (fictional)",
        prior_art_notes=(
            "Discloses a coordinated suite of implanted devices: a vision-replacement "
            "ocular sensor implant; an implanted processing/computation node interfaced to "
            "the nervous system; implanted systems that continuously monitor and regulate "
            "the host's physiology; and a persistent wireless link joining the implants to "
            "an external network. Relevant to implantable-sensor-network and "
            "implantable-physiological-regulation claims combining 'a plurality of implanted "
            "sensors/effectors', 'an implanted processor', 'closed-loop physiological "
            "control', and 'a wireless link to an external system'. § 103 motivation that "
            "the networked implantable sensor/regulator suite was an articulated objective "
            "by 1989."
        ),
        sources=[
            "Star Trek: The Next Generation, 'Q Who'. Paramount Television, 1989.",
        ],
        cpc_classifications=["A61B 5/00", "A61N 1/372", "A61F 9/08", "A61B 5/0031"],
    ),
    E(
        id="gattaca-biometric-checkpoints",
        canonical_name="Gattaca continuous multi-modal biometric identity verification",
        aliases=["Gattaca DNA checkpoints", "valid-invalid screening"],
        first_disclosure_date="1997-09-07",
        disclosure_citation="Gattaca (Columbia Pictures), released 1997; pervasive checkpoints performing rapid identification of individuals by multiple biometric modalities — blood draw, urine sample, hair, and skin/contact residue — gating access on a genetic-identity match.",
        creator="Andrew Niccol / Columbia Pictures",
        creator_country="US",
        form_factor="other",
        contact_surface="skin",
        notes="Form factor 'other' — identification is performed by fixed checkpoint instruments reading samples from the body. In scope as body measurement (multi-modal biometric identification).",
        prior_art_notes=(
            "Discloses continuous, pervasive identification of individuals by combining "
            "multiple biometric sample modalities (blood, urine, hair, skin residue) into "
            "a single identity decision used to gate physical access in real time. Relevant "
            "to multi-modal biometric-fusion identity claims combining 'acquisition of two "
            "or more distinct biometric samples', 'matching against an enrolled identity "
            "record', and 'an access decision'. § 103 motivation that pervasive multi-modal "
            "biometric identity gating was an articulated objective by 1997. Non-enabling "
            "on assay speed; pair with enabling rapid-assay art."
        ),
        sources=[
            "Gattaca (film). Columbia Pictures, 1997.",
        ],
        cpc_classifications=["G06V 40/70", "A61B 5/00", "G07C 9/00"],
    ),
]


def main():
    existing = set()
    if CORPUS.exists() and CORPUS.stat().st_size:
        for line in CORPUS.read_text().splitlines():
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])

    added = 0
    skipped = 0
    with CORPUS.open("a") as f:
        for e in ENTRIES:
            if e["id"] in existing:
                skipped += 1
                continue
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
            added += 1

    print(f"  fiction round 2: added {added}, skipped {skipped} (already present)")
    print("  next:")
    print("    python3 tools/validate.py corpus.jsonl --strict")
    print("    python3 tools/index.py .")
    print("    python3 tools/cross_cuts.py")


if __name__ == "__main__":
    main()
