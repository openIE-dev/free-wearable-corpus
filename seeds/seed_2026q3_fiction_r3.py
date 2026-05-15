#!/usr/bin/env python3
"""seed_2026q3_fiction_r3.py — fictional seed batch round 3.

Body-measurement / surveillance fiction (1984, THX 1138, Total Recall,
Demolition Man, The Island, Psycho-Pass, Elysium, Idiocracy), ingestible
/ intravascular fiction (Fantastic Voyage, The Matrix navel bug), and a
few more neural/eyewear wearables (BTTF2 video glasses, Strange Days SQUID,
Ghost in the Shell cyberbrain, Surrogates rig, Elysium exoskeleton).

Run from repo root:

    python3 seeds/seed_2026q3_fiction_r3.py

Idempotent — skips ids already present.

Dental fiction is genuinely sparse — the recurring "transmitter in a
molar" trope rarely traces to a citable primary source, so it is omitted
here rather than sourced loosely. Revisit if a well-attested dental
example surfaces.

Doctrinal note (same as rounds 1-2): fictional disclosures are generally
non-enabling; their prior-art value is § 103 motivation-to-combine.
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
    # ---------------- SURVEILLANCE / REMOTE BODY MONITORING ----------------
    E(
        id="1984-telescreen-body-monitoring",
        canonical_name="Nineteen Eighty-Four telescreen (remote body and behaviour monitoring)",
        aliases=["1984 telescreen", "telescreen Physical Jerks"],
        first_disclosure_date="1949-06-08",
        disclosure_citation="Orwell, George. Nineteen Eighty-Four. Secker & Warburg, 1949 — the two-way 'telescreen' that continuously observes occupants and, in the 'Physical Jerks' scene, monitors a citizen's exercise performance and exertion closely enough to single him out by name for inadequate effort.",
        creator="George Orwell",
        creator_country="GB",
        form_factor="other",
        contact_surface="non-contact",
        tier=2,
        notes="Form factor 'other' — monitoring is by a fixed wall device, not worn. In scope as remote, contactless monitoring of a person's physical activity and exertion.",
        prior_art_notes=(
            "Reference-only. Documents continuous, remote, contactless observation of a "
            "person's physical activity, posture, and exertion level by a fixed display/"
            "sensor device, with individualized feedback. Thin as prior art (no quantified "
            "sensing disclosed) but contributes the 'remote screen that watches and "
            "coaches your workout' concept circa 1949 to the activity/exertion-monitoring "
            "cross-cut. Promote to Tier 1 if read as antecedent to camera-based "
            "exercise-form-feedback claims."
        ),
        sources=[
            "Orwell, George. Nineteen Eighty-Four. Secker & Warburg, 1949.",
        ],
        cpc_classifications=["A61B 5/00", "G06V 40/20"],
    ),
    E(
        id="thx-1138-state-monitoring",
        canonical_name="THX 1138 — pervasive body-state monitoring with regulated medication",
        aliases=["THX 1138 monitoring", "THX physical condition readout"],
        first_disclosure_date="1971-03-11",
        disclosure_citation="THX 1138 (Warner Bros. / American Zoetrope), released March 11, 1971; a society in which citizens' physiological and emotional state is continuously monitored, displayed ('What's wrong?'), and managed through state-administered, dosage-adjusted medication. (Expands George Lucas's 1967 student short 'Electronic Labyrinth THX 1138 4EB'.)",
        creator="George Lucas / American Zoetrope",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        clinical_endpoints=["physiological-state", "affective-state", "medication-level"],
        notes="Form factor 'other' — monitoring is environmental, not worn. In scope as continuous body-state monitoring with closed-loop pharmacological response.",
        prior_art_notes=(
            "Discloses continuous monitoring of a person's physiological and emotional "
            "state coupled in closed loop to automatic adjustment of medication dosing — "
            "i.e. sense-the-body, titrate-the-drug. Relevant to closed-loop drug-delivery "
            "claims combining 'a sensor measuring a physiological or affective parameter', "
            "'a controller computing a dose from the measurement', and 'an actuator "
            "delivering the adjusted dose'. § 103 motivation that the sensor-driven "
            "closed-loop medication regime was an articulated objective by 1971."
        ),
        sources=[
            "THX 1138 (film). Warner Bros. / American Zoetrope, 1971.",
        ],
        cpc_classifications=["A61B 5/00", "A61M 5/172", "G16H 20/17"],
    ),
    E(
        id="total-recall-walkthrough-body-scanner",
        canonical_name="Total Recall walk-through whole-body imaging scanner",
        aliases=["Total Recall X-ray archway", "spaceport skeleton scanner"],
        first_disclosure_date="1990-06-01",
        disclosure_citation="Total Recall (TriStar Pictures), released June 1, 1990; the spaceport security archway that produces a real-time full-body anatomical/skeletal image of each person walking through it, highlighting concealed objects.",
        creator="Paul Verhoeven / Carolco Pictures",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        sensors=["sensor-camera-ir"],
        notes="Form factor 'other' — a fixed walk-through portal, not worn. In scope as contactless whole-body imaging of a person.",
        prior_art_notes=(
            "Discloses a walk-through portal that images the full body of a person passing "
            "through in real time, rendering internal anatomy and detecting concealed "
            "items on the body. Relevant to walk-through whole-body scanner claims "
            "combining 'a portal a person passes through', 'imaging hardware producing a "
            "body image', and 'detection of objects carried on the body' — i.e. the "
            "millimeter-wave / backscatter advanced-imaging-technology patent space. "
            "§ 103 motivation that the walk-through whole-body imager was an articulated "
            "objective by 1990. Non-enabling on the imaging physics."
        ),
        sources=[
            "Total Recall (film). TriStar Pictures / Carolco, 1990.",
        ],
        cpc_classifications=["G01V 5/00", "A61B 6/00", "G01N 23/00"],
    ),
    E(
        id="demolition-man-tracking-implant",
        canonical_name="Demolition Man subcutaneous tracking implant and ambient sensing 'fine machine'",
        aliases=["Demolition Man microchip", "verbal morality statute sensor"],
        first_disclosure_date="1993-10-08",
        disclosure_citation="Demolition Man (Warner Bros. / Silver Pictures), released October 8, 1993; every citizen carries a subcutaneous microchip used for identification and location tracking, and ambient acoustic sensors detect statutory violations (e.g. profanity) and automatically dispense a fine.",
        creator="Marco Brambilla / Silver Pictures",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["hand", "forearm"],
        output_modalities=["data-only"],
        notes="The ambient acoustic 'fine machine' is environmental sensing paired with the on-body implant; both are captured in prior_art_notes.",
        prior_art_notes=(
            "Discloses (a) a subcutaneous implanted identification-and-location chip carried "
            "by every individual, queryable wirelessly, and (b) ambient sensors that detect "
            "a defined event from a person and automatically trigger a consequence. Relevant "
            "to subcutaneous RFID/identification-implant claims combining 'a sub-dermal "
            "implant storing an identifier', 'a wireless reader', and 'a location/access "
            "function', and to ambient-sensing-triggered-action claims. § 103 motivation "
            "that the implanted ID/location chip on every person was an articulated "
            "objective by 1993."
        ),
        sources=[
            "Demolition Man (film). Warner Bros. / Silver Pictures, 1993.",
        ],
        cpc_classifications=["A61B 5/00", "G06K 19/07", "H04W 4/029", "A61B 5/0031"],
    ),
    E(
        id="the-island-continuous-health-monitoring",
        canonical_name="The Island — 24-hour ambient health monitoring with biochemical smart toilet",
        aliases=["The Island health monitoring", "The Island urine-analyzing toilet"],
        first_disclosure_date="2005-07-22",
        disclosure_citation="The Island (DreamWorks / Warner Bros.), released July 22, 2005; residents are told their health is monitored 24 hours a day, with proximity/contact sensors throughout the facility and a lavatory that analyses urine in real time and reports dietary findings ('there's too much sodium in your diet').",
        creator="Michael Bay / DreamWorks",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        sensors=["sensor-electrolyte"],
        clinical_endpoints=["urinary-sodium", "dietary-intake", "physiological-state"],
        notes="Form factor 'other' — sensing is in the environment (corridors, lavatory), not worn. In scope as continuous body measurement, including biochemical urinalysis.",
        prior_art_notes=(
            "Discloses (a) pervasive, continuous, ambient monitoring of residents' "
            "physiological state and (b) a lavatory that performs real-time urinalysis "
            "(electrolytes / sodium) and returns dietary feedback. Relevant to "
            "smart-toilet / in-fixture urinalysis claims combining 'a toilet fixture', "
            "'a sensor analysing excreted fluid', and 'a determination of a "
            "dietary/physiological parameter' (the modern smart-toilet patent space), and "
            "to pervasive ambient-health-monitoring claims. § 103 motivation that the "
            "biochemical smart toilet was an articulated objective by 2005."
        ),
        sources=[
            "The Island (film). DreamWorks / Warner Bros., 2005.",
        ],
        cpc_classifications=["A61B 10/0064", "A61B 5/20", "E03D 9/00", "G16H 50/30"],
    ),
    E(
        id="psycho-pass-cymatic-scan",
        canonical_name="Psycho-Pass — ambient continuous psychological-state scanning ('cymatic scan')",
        aliases=["Psycho-Pass scanner", "crime coefficient reader", "Sibyl cymatic scan"],
        first_disclosure_date="2012-10-12",
        disclosure_citation="Psycho-Pass (Production I.G television series), 2012; ubiquitous scanners continuously read each citizen's mental/emotional state and 'crime coefficient', and a handheld device ('Dominator') reads the targeted person's current psychological metrics in real time before acting.",
        creator="Production I.G",
        creator_country="JP",
        form_factor="other",
        contact_surface="non-contact",
        clinical_endpoints=["affective-state", "stress-index", "psychological-state"],
        notes="Form factor 'other' — scanning is environmental and handheld, not worn. In scope as contactless continuous psychological/affective-state measurement.",
        prior_art_notes=(
            "Discloses pervasive, contactless, continuous measurement of a person's "
            "psychological and emotional state, aggregated into a scalar index used to "
            "drive automated decisions, plus a portable scanner that reads a specific "
            "person's current affective metrics on demand. Relevant to affective-computing "
            "claims combining 'contactless sensing of a person', 'inference of an "
            "emotional/psychological state', and 'an action conditioned on the inferred "
            "state'. § 103 motivation that pervasive ambient affective-state scanning was "
            "an articulated objective by 2012."
        ),
        sources=[
            "Psycho-Pass (television series). Production I.G, 2012.",
        ],
        cpc_classifications=["A61B 5/16", "G06V 40/20", "G16H 50/30"],
    ),
    E(
        id="elysium-medbay-scanner",
        canonical_name="Elysium 'Med-Bay' — contactless full-body diagnostic and treatment scanner",
        aliases=["Elysium Med-Bay", "Med-Pod"],
        first_disclosure_date="2013-08-09",
        disclosure_citation="Elysium (TriStar Pictures / Media Rights Capital), released August 9, 2013; a home medical bed that performs a full-body scan of an occupant, diagnoses disease and injury, and administers treatment, presenting findings on an integrated display.",
        creator="Neill Blomkamp / Media Rights Capital",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        clinical_endpoints=["whole-body-diagnostics", "lesion-detection", "physiological-state"],
        output_modalities=["visual-display", "drug-delivery"],
        notes="Form factor 'other' — a fixed diagnostic bed, not worn. In scope as contactless whole-body measurement and closed-loop treatment.",
        prior_art_notes=(
            "Discloses a bed-form instrument that scans an occupant's whole body, derives "
            "a multi-system diagnosis (disease and injury), and delivers treatment in the "
            "same session, with a graphical report. Relevant to whole-body diagnostic-bed "
            "and closed-loop diagnose-and-treat claims combining 'a support an occupant "
            "lies on', 'imaging/sensing hardware', 'an automated diagnostic determination', "
            "and 'a coupled treatment delivery'. § 103 motivation that the integrated "
            "diagnose-and-treat body scanner was an articulated objective by 2013 — a "
            "later, more capable instance of the Star Trek biobed concept. Non-enabling."
        ),
        lineage_ancestors=["star-trek-biobed"],
        sources=[
            "Elysium (film). TriStar Pictures / Media Rights Capital, 2013.",
        ],
        cpc_classifications=["A61B 5/00", "A61B 5/0205", "G16H 50/20", "A61G 7/05"],
    ),
    E(
        id="idiocracy-barcode-identity-tattoo",
        canonical_name="Idiocracy machine-readable barcode identity tattoo",
        aliases=["Idiocracy barcode tattoo"],
        first_disclosure_date="2006-09-01",
        disclosure_citation="Idiocracy (20th Century Fox), released September 1, 2006; citizens bear a barcode tattoo on the body that is scanned at points of sale, hospitals, and checkpoints to retrieve identity and records.",
        creator="Mike Judge / 20th Century Fox",
        creator_country="US",
        form_factor="tattoo-electronic",
        contact_surface="skin",
        tier=2,
        output_modalities=["data-only"],
        notes="The tattoo shown is an optical barcode rather than an electronic device; included as a thin antecedent to on-body machine-readable identity markings.",
        prior_art_notes=(
            "Reference-only. Documents a machine-readable identity marking applied directly "
            "to the skin and scanned to retrieve a person's identity and records at "
            "transaction and access points. Thin as prior art (optical, passive) but "
            "contributes the 'permanent on-body machine-readable identity token' concept "
            "circa 2006 to the epidermal/tattoo-electronic identity cross-cut. Promote to "
            "Tier 1 if read as antecedent to electronic-skin / sub-dermal-identity claims."
        ),
        sources=[
            "Idiocracy (film). 20th Century Fox, 2006.",
        ],
        cpc_classifications=["G06K 19/06", "A61B 5/00", "G07C 9/00"],
    ),
    # ---------------- INGESTIBLE / INTRAVASCULAR ----------------
    E(
        id="fantastic-voyage-intravascular-craft",
        canonical_name="Fantastic Voyage — miniaturized intravascular craft navigating the body",
        aliases=["Fantastic Voyage submarine", "Proteus craft"],
        first_disclosure_date="1966-08-24",
        disclosure_citation="Fantastic Voyage (20th Century Fox), released August 24, 1966 (Isaac Asimov novelization, 1966); a miniaturized crewed craft is introduced into a patient's bloodstream and navigates the vasculature to reach and treat an internal target, in two-way communication with an external control station.",
        creator="Richard Fleischer / 20th Century Fox; novelization Isaac Asimov",
        creator_country="US",
        form_factor="ingestible",
        form_factor_tags=["implantable"],
        contact_surface="vascular",
        anatomical_target=["bloodstream", "brain"],
        output_modalities=["data-only"],
        notes="Form factor 'ingestible'/'implantable' by analogy — a device introduced into the body that traverses internal cavities/vessels. In scope as an in-body sensing/intervention capsule.",
        prior_art_notes=(
            "Discloses a small device introduced into the bloodstream that locomotes "
            "through the vasculature under guidance, reaches an internal target, performs "
            "an intervention there, and maintains a telemetry link to an external operator "
            "station. Relevant to intravascular microrobot / in-body capsule claims "
            "combining 'a device sized to traverse a blood vessel', 'a propulsion or "
            "navigation means', 'a therapeutic or sensing payload', and 'a wireless link "
            "to an external controller' — the modern microrobotics / capsule-endoscopy / "
            "intravascular-robotics patent space. § 103 motivation that the navigable "
            "in-bloodstream device was an articulated objective by 1966. Non-enabling on "
            "miniaturization."
        ),
        sources=[
            "Fantastic Voyage (film). 20th Century Fox, 1966.",
            "Asimov, Isaac. Fantastic Voyage. Houghton Mifflin, 1966.",
        ],
        cpc_classifications=["A61B 1/00", "A61B 5/0031", "A61B 34/00", "A61M 25/00"],
    ),
    E(
        id="the-matrix-navel-tracking-bug",
        canonical_name="The Matrix — migrating intra-abdominal surveillance 'bug'",
        aliases=["Matrix tracking bug", "Neo's bug"],
        first_disclosure_date="1999-03-31",
        disclosure_citation="The Matrix (Warner Bros. / Village Roadshow), released March 31, 1999; a small robotic device is introduced into a person through the navel, burrows into and lodges in the abdomen, and serves as a covert tracking/surveillance implant until later located and extracted.",
        creator="The Wachowskis / Village Roadshow",
        creator_country="US",
        form_factor="ingestible",
        form_factor_tags=["implantable"],
        contact_surface="intra-abdominal",
        anatomical_target=["abdomen", "navel"],
        output_modalities=["data-only"],
        notes="Form factor 'ingestible'/'implantable' — a device introduced into the body via a natural opening that then migrates and lodges internally.",
        prior_art_notes=(
            "Discloses a small device introduced into the body through a natural opening "
            "that actively migrates to and anchors at an internal site and then functions "
            "as a covert tracking/sensing implant, locatable and retrievable afterward. "
            "Relevant to ingestible/implantable migrating-capsule claims combining 'a "
            "device introduced via a body orifice', 'self-locomotion to an internal site', "
            "'an anchoring mechanism', and 'a tracking or sensing function' — adjacent to "
            "capsule-endoscopy, ingestible-sensor, and locatable-implant patents. § 103 "
            "motivation that the migrating, self-anchoring in-body capsule was an "
            "articulated objective by 1999."
        ),
        lineage_ancestors=["fantastic-voyage-intravascular-craft"],
        sources=[
            "The Matrix (film). Warner Bros. / Village Roadshow, 1999.",
        ],
        cpc_classifications=["A61B 1/00", "A61B 5/0031", "G06K 19/07", "A61B 5/07"],
    ),
    # ---------------- EYEWEAR / NEURAL WEARABLES ----------------
    E(
        id="bttf2-video-glasses",
        canonical_name="Back to the Future Part II personal video/phone glasses",
        aliases=["BTTF2 TV glasses", "future kids' glasses"],
        first_disclosure_date="1989-11-22",
        disclosure_citation="Back to the Future Part II (Universal Pictures), released November 22, 1989; wraparound glasses worn casually at home that display television, answer telephone calls, and present caller and channel information — each family member wearing their own.",
        creator="Robert Zemeckis / Universal Pictures",
        creator_country="US",
        form_factor="glasses",
        output_modalities=["visual-display", "audio"],
        connectivity="broadcast TV + telephony (fictional)",
        prior_art_notes=(
            "Discloses lightweight glasses functioning as a personal head-worn display for "
            "video media and as a telephony terminal (presenting caller ID, accepting "
            "calls), used by multiple co-located people each with their own pair. Relevant "
            "to display-glasses claims combining 'an eyewear frame', 'a near-eye display "
            "presenting video', 'a wireless link receiving media and calls', and 'a "
            "personal/individual viewing context'. § 103 motivation that the personal "
            "media-and-phone display glasses were an articulated objective by 1989 — "
            "predating Snow Crash's 1992 gargoyle rig."
        ),
        lineage_descendants=["snow-crash-gargoyle-rig"],
        sources=[
            "Back to the Future Part II (film). Universal Pictures, 1989.",
        ],
        cpc_classifications=["G02B 27/01", "H04N 21/41", "G02C 11/00"],
    ),
    E(
        id="strange-days-squid-recorder",
        canonical_name="Strange Days — SQUID head-worn neural experience recorder",
        aliases=["SQUID", "Superconducting Quantum Interference Device (Strange Days)", "wire trip recorder"],
        first_disclosure_date="1995-10-13",
        disclosure_citation="Strange Days (Lightstorm Entertainment / 20th Century Fox), released October 13, 1995; the 'SQUID' — a fine wire-mesh cap worn under a hat that records the wearer's full multisensory and emotional experience directly from the cerebral cortex for later playback into another person's cortex.",
        creator="Kathryn Bigelow / James Cameron (writer) / Lightstorm",
        creator_country="US",
        form_factor="cap",
        contact_surface="scalp",
        anatomical_target=["scalp", "cerebral-cortex"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        clinical_endpoints=["sensory-experience", "affective-state"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a head-worn mesh of scalp electrodes that records a rich, "
            "multi-channel signal of the wearer's perceptual and affective experience for "
            "storage and later replay. Relevant to wearable neural-recording claims "
            "combining 'a head-worn array of scalp electrodes', 'acquisition of a "
            "multi-channel cortical signal', 'encoding of perceptual/affective content', "
            "and 'storage for later playback'. § 103 motivation that the wearable "
            "experience-recording headset was an articulated objective by 1995. "
            "Non-enabling on the encoding/playback; pair with enabling EEG/BCI art."
        ),
        sources=[
            "Strange Days (film). Lightstorm Entertainment / 20th Century Fox, 1995.",
        ],
        cpc_classifications=["A61B 5/24", "A61B 5/372", "G06F 3/01", "A61B 5/16"],
    ),
    E(
        id="ghost-in-the-shell-cyberbrain",
        canonical_name="Ghost in the Shell — cyberbrain neural-interface implant and cyberbody monitoring",
        aliases=["cyberbrain", "GitS cyberbrain", "nape data port"],
        first_disclosure_date="1989-04",
        disclosure_citation="Shirow, Masamune. The Ghost in the Shell (Kōkaku Kidōtai), serialized in Young Magazine from April 1989, Kodansha; cybernetically augmented people carry a 'cyberbrain' — a neural-interface implant with wired data ports at the nape of the neck, networked connectivity, external memory, AR overlays, and continuous monitoring of the prosthetic body's status.",
        creator="Masamune Shirow",
        creator_country="JP",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["brain", "nape-of-neck", "spine"],
        clinical_endpoints=["prosthetic-body-status", "neural-activity"],
        output_modalities=["visual-display", "data-only"],
        connectivity="networked neural link (fictional)",
        prior_art_notes=(
            "Discloses an implanted neural interface providing (a) high-bandwidth data I/O "
            "to the brain via dedicated ports, (b) wireless and wired networking of the "
            "implant, (c) externalized/augmented memory, (d) AR information overlays on "
            "perception, and (e) continuous status monitoring of an attached prosthetic "
            "body. Relevant to implantable-BCI claims combining 'an implanted neural "
            "interface', 'a wired/wireless data link', and 'continuous monitoring of body "
            "or prosthesis state'. § 103 motivation that the networked implantable neural "
            "interface with body monitoring was an articulated objective by 1989. "
            "Non-enabling; pair with enabling neural-implant art."
        ),
        lineage_descendants=["star-trek-borg-implants"],
        sources=[
            "Shirow, Masamune. The Ghost in the Shell. Kodansha (Young Magazine), 1989-1990.",
        ],
        cpc_classifications=["A61B 5/372", "A61B 5/0031", "A61F 2/72", "G06F 3/01"],
    ),
    E(
        id="surrogates-neural-teleoperation-rig",
        canonical_name="Surrogates — head-worn neural interface rig for robot-body telepresence",
        aliases=["Surrogates stim chair rig", "operator headset (Surrogates)"],
        first_disclosure_date="2005-08-17",
        disclosure_citation="Venditti, Robert; Weldele, Brett. The Surrogates #1. Top Shelf Productions, 2005 (film adaptation: Touchstone Pictures, 2009); operators recline in a chair wearing a head-mounted neural interface that captures their volition and sensory channels to remotely embody and control a humanoid robot 'surrogate', receiving its sensory feedback in return.",
        creator="Robert Venditti and Brett Weldele",
        creator_country="US",
        form_factor="headband",
        form_factor_tags=["cap"],
        contact_surface="scalp",
        anatomical_target=["scalp", "head"],
        sensors=["sensor-dry-eeg-electrode", "sensor-eeg"],
        clinical_endpoints=["neural-activity", "motor-intent"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a head-worn neural-interface rig that reads the wearer's motor "
            "intent and routes sensory feedback, used to teleoperate a humanoid robot with "
            "the operator perceiving through the robot's sensors. Relevant to wearable-BCI "
            "teleoperation claims combining 'a head-worn neural sensor array', 'decoding "
            "of motor intent', 'transmission of commands to a remote robot', and 'return "
            "of the robot's sensory data to the wearer'. § 103 motivation that the "
            "wearable neural-interface telepresence rig was an articulated objective by "
            "2005. Non-enabling; pair with enabling BCI/teleop art."
        ),
        sources=[
            "Venditti, Robert; Weldele, Brett. The Surrogates. Top Shelf Productions, 2005-2006.",
            "Surrogates (film). Touchstone Pictures, 2009.",
        ],
        cpc_classifications=["A61B 5/372", "G06F 3/01", "B25J 13/00", "A61B 5/24"],
    ),
    E(
        id="elysium-bolt-on-exoskeleton",
        canonical_name="Elysium — surgically-integrated powered exoskeleton with neural control",
        aliases=["Elysium exosuit", "Max's exoskeleton"],
        first_disclosure_date="2013-08-09",
        disclosure_citation="Elysium (TriStar Pictures / Media Rights Capital), released August 9, 2013; a powered exoskeleton bolted to the wearer's skeleton and interfaced to the nervous system (with a head-mounted data port), augmenting strength and serving as a host platform for software/data.",
        creator="Neill Blomkamp / Media Rights Capital",
        creator_country="US",
        form_factor="exoskeleton",
        contact_surface="sub-dermal",
        anatomical_target=["spine", "limbs", "skull"],
        sensors=["sensor-emg"],
        clinical_endpoints=["motor-intent"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a powered exoskeleton rigidly coupled to the wearer's skeleton and "
            "interfaced to the nervous system to read movement intent and augment force, "
            "while also functioning as an embedded compute/data platform. Relevant to "
            "powered-exoskeleton claims combining 'a wearable frame coupled to the body', "
            "'actuators augmenting limb force', 'a neural or EMG interface sensing movement "
            "intent', and 'an onboard processor'. § 103 motivation that the "
            "neurally-controlled bolt-on powered exoskeleton was an articulated objective "
            "by 2013."
        ),
        sources=[
            "Elysium (film). TriStar Pictures / Media Rights Capital, 2013.",
        ],
        cpc_classifications=["A61H 3/00", "B25J 9/00", "A61B 5/389", "A61F 2/70"],
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

    print(f"  fiction round 3: added {added}, skipped {skipped} (already present)")
    print("  next:")
    print("    python3 tools/validate.py corpus.jsonl --strict")
    print("    python3 tools/index.py .")
    print("    python3 tools/cross_cuts.py")


if __name__ == "__main__":
    main()
