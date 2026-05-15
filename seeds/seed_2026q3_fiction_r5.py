#!/usr/bin/env python3
"""seed_2026q3_fiction_r5.py — fictional seed batch round 5.

Black Mirror anthology + modern dystopian TV / games (Severance, Westworld,
Altered Carbon, Upgrade, eXistenZ, The Matrix headjack, The Circle).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r5.py
Idempotent — skips ids already present.

Doctrinal note: fictional disclosures are generally non-enabling; their
prior-art value is § 103 motivation-to-combine. Several entries here are
later instances of a concept whose chronological chain runs back through
earlier corpus entries — the chain itself is the prior-art product.
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
    E(
        id="black-mirror-grain-implant",
        canonical_name="Black Mirror 'grain' implant ('The Entire History of You')",
        aliases=["the grain", "Black Mirror grain"],
        first_disclosure_date="2011-12-18",
        disclosure_citation="Black Mirror, 'The Entire History of You' (Channel 4, 18 December 2011); a 'grain' implanted behind the ear continuously records the wearer's audiovisual experience, replayable on the retina or cast to an external screen ('re-do').",
        creator="Charlie Brooker / Jesse Armstrong / Zeppotron",
        creator_country="GB",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["behind-ear", "mastoid"],
        sensors=["sensor-camera-rgb", "sensor-microphone-air"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a behind-the-ear implanted lifelogging device that continuously "
            "captures the wearer's first-person audiovisual stream and replays it onto the "
            "wearer's retina or to an external display with seek/scrub controls. Relevant "
            "to implantable lifelogging claims combining 'a sub-dermal recorder', "
            "'continuous capture of first-person audio/video', 'retinal or external "
            "playback', and 'random-access review'. § 103 motivation that the implanted "
            "always-on experience recorder was an articulated objective by 2011. "
            "Non-enabling on the implant electronics."
        ),
        sources=["Black Mirror, 'The Entire History of You'. Channel 4 / Zeppotron, 2011."],
        cpc_classifications=["A61B 5/0031", "H04N 5/77", "G06F 3/01"],
    ),
    E(
        id="black-mirror-fifteen-million-merits-gaze-enforcement",
        canonical_name="Black Mirror 'Fifteen Million Merits' — gaze-enforced compulsory viewing",
        aliases=["Fifteen Million Merits", "Doppel ad enforcement"],
        first_disclosure_date="2011-12-11",
        disclosure_citation="Black Mirror, 'Fifteen Million Merits' (Channel 4, 11 December 2011); ubiquitous screens show advertising the viewer is required to watch — closing or averting the eyes triggers an alarm and a penalty until the viewer's gaze returns.",
        creator="Charlie Brooker / Konnie Huq / Zeppotron",
        creator_country="GB",
        form_factor="other",
        contact_surface="non-contact",
        sensors=["sensor-camera-eye"],
        algorithms=["algo-eye-gaze-tracking"],
        tier=2,
        notes="Form factor 'other' — environmental screens with gaze sensors, not worn. In scope as contactless gaze monitoring driving an enforcement action.",
        prior_art_notes=(
            "Reference-only. Documents contactless gaze tracking used to detect look-away "
            "and trigger an enforcement response — i.e. attention-verification gating of "
            "media playback. Loosely relevant to attention-monitoring / mandatory-viewing "
            "claims; cf. the earlier neuro-reward gaming device in [[startrek-tng-the-game-neuro-visor]]."
        ),
        sources=["Black Mirror, 'Fifteen Million Merits'. Channel 4 / Zeppotron, 2011."],
        cpc_classifications=["A61B 3/113", "G06V 40/19", "H04N 21/442"],
    ),
    E(
        id="black-mirror-arkangel-implant",
        canonical_name="Black Mirror 'Arkangel' parental-monitoring neural implant",
        aliases=["Arkangel"],
        first_disclosure_date="2017-12-29",
        disclosure_citation="Black Mirror, 'Arkangel' (Netflix, 29 December 2017); a neural implant given to a child providing the parent with GPS location, vital-sign monitoring, a live first-person video feed, and real-time visual censoring (pixelating distressing sights and muting sounds in the child's perception).",
        creator="Charlie Brooker / House of Tomorrow",
        creator_country="GB",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["skull", "visual-cortex"],
        sensors=["sensor-camera-rgb"],
        clinical_endpoints=["location", "multi-parameter-vitals", "cortisol"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses an implanted device that (a) reports the wearer's location and "
            "vitals to a remote guardian, (b) streams the wearer's first-person view, and "
            "(c) modifies the wearer's own perception in real time (visual redaction, "
            "audio attenuation). Relevant to implantable-monitoring claims combining "
            "'location + physiological telemetry to a remote party', 'first-person video "
            "streaming', and 'perceptual filtering of the wearer's sensory input'. § 103 "
            "motivation that the perception-modifying monitoring implant was an articulated "
            "objective by 2017. Cf. [[black-mirror-grain-implant]], [[black-mirror-z-eye-redaction]]."
        ),
        sources=["Black Mirror, 'Arkangel'. Netflix / House of Tomorrow, 2017."],
        cpc_classifications=["A61B 5/0031", "A61B 5/00", "G06F 3/01", "H04W 4/029"],
    ),
    E(
        id="black-mirror-z-eye-redaction",
        canonical_name="Black Mirror 'Z-Eye' ocular implant with selective people-redaction ('White Christmas')",
        aliases=["Z-Eye", "blocking implant"],
        first_disclosure_date="2014-12-16",
        disclosure_citation="Black Mirror, 'White Christmas' (Channel 4, 16 December 2014); the 'Z-Eye' ocular implant lets a user 'block' another person, who is thereafter rendered as a featureless grey silhouette with muffled audio in the user's perception (and the block is reciprocal).",
        creator="Charlie Brooker / Zeppotron",
        creator_country="GB",
        form_factor="implantable",
        form_factor_tags=["contact-lens"],
        contact_surface="ocular",
        anatomical_target=["eye", "visual-cortex"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses an ocular implant that performs real-time, person-specific "
            "augmented-reality redaction — recognizing an individual in view and replacing "
            "their appearance and voice with an obscured rendering. Relevant to AR-eyewear "
            "/ AR-implant claims combining 'person recognition', 'a user-defined block "
            "list', and 'real-time obscuring of the recognized person in the rendered "
            "view'. § 103 motivation that AR person-redaction was an articulated objective "
            "by 2014. Cf. [[they-live-hoffman-lenses]] (the inverse — revealing rather "
            "than hiding)."
        ),
        sources=["Black Mirror, 'White Christmas'. Channel 4 / Zeppotron, 2014."],
        cpc_classifications=["G06V 40/16", "G06T 11/00", "G02B 27/01"],
    ),
    E(
        id="black-mirror-nosedive-rating-overlay",
        canonical_name="Black Mirror 'Nosedive' — AR social-rating overlay",
        aliases=["Nosedive eye implant", "social score overlay"],
        first_disclosure_date="2016-10-21",
        disclosure_citation="Black Mirror, 'Nosedive' (Netflix, 21 October 2016); an ocular implant paired with a handset overlays every person in view with their live aggregate social rating, updated continuously from peer ratings of every interaction.",
        creator="Charlie Brooker / Rashida Jones / Michael Schur / House of Tomorrow",
        creator_country="GB",
        form_factor="implantable",
        form_factor_tags=["contact-lens"],
        contact_surface="ocular",
        anatomical_target=["eye"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses an ocular AR device that recognizes people in view and renders a "
            "live reputation/score badge beside each, with the score continuously updated "
            "from crowd ratings of interactions. Relevant to AR-eyewear claims combining "
            "'person recognition', 'retrieval of a per-person reputation metric', and "
            "'real-time overlay of the metric on the recognized person'. § 103 motivation "
            "that the AR reputation overlay was an articulated objective by 2016. Cf. "
            "[[dragon-ball-z-scouter]] (an earlier scan-and-display-a-metric eyewear)."
        ),
        sources=["Black Mirror, 'Nosedive'. Netflix / House of Tomorrow, 2016."],
        cpc_classifications=["G06V 40/16", "G06Q 50/00", "G02B 27/01"],
    ),
    E(
        id="black-mirror-playtest-implant",
        canonical_name="Black Mirror 'Playtest' — adaptive mixed-reality implant driven by biometric fear response",
        aliases=["Playtest mushroom implant", "SaitoGemu implant"],
        first_disclosure_date="2016-10-21",
        disclosure_citation="Black Mirror, 'Playtest' (Netflix, 21 October 2016); a behind-the-ear implant ('the mushroom') renders mixed-reality content directly into the player's perception and adapts it in real time to the player's measured fears and physiological responses.",
        creator="Charlie Brooker / House of Tomorrow",
        creator_country="GB",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["behind-ear", "temporal-lobe"],
        clinical_endpoints=["affective-state", "fear-response"],
        algorithms=["algo-emotion-recognition"],
        output_modalities=["visual-display", "audio"],
        prior_art_notes=(
            "Discloses an implanted mixed-reality device that both renders content into "
            "the wearer's perception and continuously measures the wearer's affective "
            "state (fear), closing a loop so the content adapts to the measured response. "
            "Relevant to closed-loop AR/VR claims combining 'rendering immersive content', "
            "'biometric/affect sensing of the user', and 'adapting the content to the "
            "sensed state'. § 103 motivation that the affect-adaptive immersive device "
            "was an articulated objective by 2016."
        ),
        sources=["Black Mirror, 'Playtest'. Netflix / House of Tomorrow, 2016."],
        cpc_classifications=["A63F 13/212", "A61B 5/16", "G06F 3/01"],
    ),
    E(
        id="black-mirror-men-against-fire-mass-implant",
        canonical_name="Black Mirror 'Men Against Fire' — 'MASS' military neural implant",
        aliases=["MASS implant", "Men Against Fire"],
        first_disclosure_date="2016-10-21",
        disclosure_citation="Black Mirror, 'Men Against Fire' (Netflix, 21 October 2016); the 'MASS' implant gives soldiers a tactical AR HUD and comms, alters their perception (rendering targeted persons as monstrous 'roaches'), suppresses sensory aversion, and delivers reward/dream conditioning, with physiological telemetry to command.",
        creator="Charlie Brooker / House of Tomorrow",
        creator_country="GB",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["skull", "visual-cortex", "olfactory-cortex"],
        clinical_endpoints=["multi-parameter-vitals", "affective-state"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses an implanted neural device combining a tactical AR HUD, comms, "
            "perception alteration (re-rendering people in view), sensory-aversion "
            "suppression, conditioning via reward/dream stimulation, and physiological "
            "telemetry to a remote commander. Relevant to military-HUD-implant claims; "
            "extends the perception-modification chain — cf. [[black-mirror-z-eye-redaction]], "
            "[[predator-bio-mask]], [[terminator-t800-hud]]. § 103 motivation that the "
            "perception-altering combat implant was an articulated objective by 2016."
        ),
        sources=["Black Mirror, 'Men Against Fire'. Netflix / House of Tomorrow, 2016."],
        cpc_classifications=["A61B 5/0031", "G06F 3/01", "G02B 27/01", "A61M 21/00"],
    ),
    E(
        id="black-mirror-crocodile-recaller",
        canonical_name="Black Mirror 'Crocodile' — portable memory-extraction device ('the recaller')",
        aliases=["recaller", "corroborator", "Crocodile memory device"],
        first_disclosure_date="2017-12-29",
        disclosure_citation="Black Mirror, 'Crocodile' (Netflix, 29 December 2017); a portable device with a small sensor placed on a person's temple reads and displays their memories of an event for insurance/forensic corroboration.",
        creator="Charlie Brooker / House of Tomorrow",
        creator_country="GB",
        form_factor="headband",
        contact_surface="scalp",
        anatomical_target=["temple", "temporal-lobe"],
        sensors=["sensor-dry-eeg-electrode"],
        clinical_endpoints=["episodic-memory"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses a portable temple-applied sensor that decodes and displays a "
            "subject's recalled visual memory of a target event. Relevant to "
            "neural-decoding claims combining 'a scalp/temple electrode', 'evocation of a "
            "specific episodic memory', and 'reconstruction of a visual representation'. "
            "§ 103 motivation that portable memory readout was an articulated objective by "
            "2017. Cf. [[strange-days-squid-recorder]] (recording rather than later readout)."
        ),
        sources=["Black Mirror, 'Crocodile'. Netflix / House of Tomorrow, 2017."],
        cpc_classifications=["A61B 5/372", "A61B 5/24", "G06F 3/01"],
    ),
    E(
        id="black-mirror-striking-vipers-temple-disc",
        canonical_name="Black Mirror 'Striking Vipers' — minimal-form temple disc for full-immersion VR",
        aliases=["Striking Vipers disc", "TCKR VR disc"],
        first_disclosure_date="2019-06-05",
        disclosure_citation="Black Mirror, 'Striking Vipers' (Netflix, 5 June 2019); a small adhesive disc placed on the temple provides full-sensory, full-immersion virtual reality with another networked user, with no headset.",
        creator="Charlie Brooker / House of Tomorrow",
        creator_country="GB",
        form_factor="headband",
        form_factor_tags=["tattoo-electronic"],
        contact_surface="scalp",
        anatomical_target=["temple"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a coin-sized temple-mounted device delivering full-sensory, "
            "networked, multi-user immersive VR without a headset or goggles. Relevant to "
            "minimal-form-factor neural-VR claims combining 'a small scalp-applied "
            "transducer', 'bidirectional sensory I/O', and 'a networked shared virtual "
            "environment'. § 103 motivation that the headset-free VR transducer was an "
            "articulated objective by 2019. Cf. [[ready-player-one-haptic-suit]], "
            "[[sao-nervegear]]."
        ),
        sources=["Black Mirror, 'Striking Vipers'. Netflix / House of Tomorrow, 2019."],
        cpc_classifications=["G06F 3/01", "A61B 5/372", "G02B 27/01"],
    ),
    E(
        id="the-circle-seechange-and-health-wristbands",
        canonical_name="The Circle — 'SeeChange' wearable cameras and employee health wristbands",
        aliases=["SeeChange", "The Circle wristbands", "Circle health bracelets"],
        first_disclosure_date="2013-10-08",
        disclosure_citation="Eggers, Dave. The Circle. Alfred A. Knopf, 2013 (film adaptation 2017); 'SeeChange' miniature wearable/mountable cameras streaming continuously, and employee wristbands (worn in pairs on each wrist) that continuously monitor heart rate, activity, sleep, and other physiological data and upload it to the company.",
        creator="Dave Eggers",
        creator_country="US",
        form_factor="bracelet",
        form_factor_tags=["body-camera"],
        contact_surface="skin",
        anatomical_target=["wrist"],
        sensors=["sensor-ppg", "sensor-accelerometer", "sensor-camera-rgb"],
        clinical_endpoints=["heart-rate", "activity", "sleep"],
        algorithms=["algo-hr", "algo-step-count", "algo-sleep-staging"],
        output_modalities=["data-only"],
        connectivity="continuous wireless upload (fictional)",
        prior_art_notes=(
            "Discloses (a) continuously-worn wristbands with PPG and motion sensing that "
            "stream heart rate, activity, and sleep data to an employer, and (b) tiny "
            "body-wearable always-streaming cameras. Relevant to workplace-wellness "
            "wearable claims combining 'a wrist-worn PPG/motion sensor', 'continuous "
            "physiological streaming to a remote/employer system', and to body-worn-camera "
            "streaming claims. § 103 motivation that the employer-monitored wrist wearable "
            "and the always-streaming wearable camera were articulated objectives by 2013."
        ),
        sources=["Eggers, Dave. The Circle. Alfred A. Knopf, 2013. ISBN 0-385-35139-9."],
        cpc_classifications=["A61B 5/0205", "A61B 5/024", "G16H 40/67", "H04N 7/18"],
    ),
    E(
        id="westworld-host-control-unit",
        canonical_name="Westworld — host 'control unit' and continuous body telemetry",
        aliases=["the pearl", "host control unit", "Westworld brain ball"],
        first_disclosure_date="2016-10-02",
        disclosure_citation="Westworld (HBO, premiered 2 October 2016); each android 'host' contains a removable 'control unit' in the cranium storing its cognition and identity, with continuous telemetry of the host's mechanical/physiological state and behaviour to a central facility.",
        creator="Jonathan Nolan / Lisa Joy / HBO",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["skull", "brain"],
        clinical_endpoints=["body-status", "behavioural-state"],
        output_modalities=["data-only"],
        connectivity="facility network (fictional)",
        prior_art_notes=(
            "Discloses a removable cranial unit that stores an embodied agent's cognition "
            "and identity and that maintains continuous wireless telemetry of body and "
            "behavioural state to a central system. Relevant to implantable-data-store / "
            "implantable-telemetry claims; later instance of the chain through "
            "[[ghost-in-the-shell-cyberbrain]], [[star-trek-borg-implants]]. § 103 "
            "motivation as of 2016."
        ),
        sources=["Westworld (television series). HBO / Bad Robot, 2016."],
        cpc_classifications=["A61B 5/0031", "G06N 3/00", "A61B 5/00"],
    ),
    E(
        id="altered-carbon-cortical-stack",
        canonical_name="Altered Carbon — 'cortical stack' cervical-spine consciousness store",
        aliases=["cortical stack", "the stack"],
        first_disclosure_date="2002-03-01",
        disclosure_citation="Morgan, Richard K. Altered Carbon. Gollancz, 2002 (Netflix adaptation 2018); a 'cortical stack' implanted at the top of the spinal column digitally stores a person's consciousness and memory, removable and transferable between bodies ('sleeves').",
        creator="Richard K. Morgan",
        creator_country="GB",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["cervical-spine", "brainstem"],
        clinical_endpoints=["neural-state"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a cervical-spine implant that continuously stores a person's neural "
            "state/identity in digital form, designed to be removed and re-installed in a "
            "different body. Relevant to implantable neural-data-store claims combining "
            "'a cervical implant', 'continuous capture of neural state', and 'removable, "
            "transferable storage'. § 103 motivation that the spinal consciousness-store "
            "was an articulated objective by 2002. Cf. [[ghost-in-the-shell-cyberbrain]], "
            "[[delany-nova-cyborg-sockets]]."
        ),
        sources=["Morgan, Richard K. Altered Carbon. Gollancz, 2002. ISBN 0-575-07321-2."],
        cpc_classifications=["A61B 5/0031", "A61B 5/372", "A61F 2/44"],
    ),
    E(
        id="upgrade-stem-spinal-implant",
        canonical_name="Upgrade — 'STEM' spinal AI implant with sensorimotor takeover",
        aliases=["STEM implant", "Upgrade chip"],
        first_disclosure_date="2018-03-10",
        disclosure_citation="Upgrade (BH Tilt / Blumhouse), 2018; the 'STEM' chip implanted at the base of the spine interfaces with the host's nervous system, restoring and then augmenting motor control, processing sensory input, and acting as an on-board AI co-pilot for the body.",
        creator="Leigh Whannell / Blumhouse",
        creator_country="AU",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["spine", "spinal-cord"],
        sensors=["sensor-emg"],
        clinical_endpoints=["motor-intent", "sensory-input"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a spinal implant that bridges/replaces damaged neural pathways to "
            "restore motor control, processes the host's sensory input, and provides "
            "on-board computational assistance for movement. Relevant to "
            "spinal-cord-stimulation / motor-restoration implant claims combining 'a "
            "spinal implant interfacing motor and sensory pathways', 'restoration or "
            "augmentation of motor function', and 'an onboard processor'. § 103 motivation "
            "as of 2018. Cf. [[elysium-bolt-on-exoskeleton]]."
        ),
        sources=["Upgrade (film). BH Tilt / Blumhouse, 2018."],
        cpc_classifications=["A61N 1/36", "A61B 5/389", "A61F 2/72"],
    ),
    E(
        id="severance-bifurcation-chip",
        canonical_name="Severance — 'severance' brain implant bifurcating consciousness",
        aliases=["severance chip", "Lumon chip"],
        first_disclosure_date="2022-02-18",
        disclosure_citation="Severance (Apple TV+, premiered 18 February 2022); a surgically implanted brain chip ('the severance procedure') partitions a worker's episodic memory and identity into two states ('innie' and 'outie'), switched automatically by location (descending in the office elevator).",
        creator="Dan Erickson / Ben Stiller / Apple TV+",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["skull", "hippocampus"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses an implanted neural device that gates access to a person's episodic "
            "memory and identity by an external trigger (location), producing two distinct "
            "operative states. Relevant to implantable-neuromodulation claims combining "
            "'a brain implant', 'context-triggered state switching', and 'modulation of "
            "memory access'. § 103 motivation that the context-switched cognitive-state "
            "implant was an articulated objective by 2022."
        ),
        sources=["Severance (television series). Apple TV+ / Red Hour, 2022."],
        cpc_classifications=["A61B 5/0031", "A61N 1/36", "A61B 5/372"],
    ),
    E(
        id="existenz-bioport-and-game-pod",
        canonical_name="eXistenZ — spinal 'bioport' and organic neural game pod",
        aliases=["bioport", "eXistenZ pod", "MetaFlesh game pod"],
        first_disclosure_date="1999-04-23",
        disclosure_citation="eXistenZ (Alliance Atlantis / Dimension Films), released 23 April 1999; a surgically installed 'bioport' at the base of the spine accepts an 'UmbyCord' from an organic game pod, providing a full-immersion neural game interface read and driven through the spinal cord.",
        creator="David Cronenberg / Alliance Atlantis",
        creator_country="CA",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["spine", "spinal-cord"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a surgically installed spinal port that accepts a wired connection "
            "from an external device for full-immersion neural interfacing. Relevant to "
            "implanted-neural-port claims combining 'a percutaneous/sub-dermal port at the "
            "spine', 'a connector to an external device', and 'bidirectional neural I/O'. "
            "§ 103 motivation as of 1999. Cf. [[the-matrix-headjack]], "
            "[[delany-nova-cyborg-sockets]]."
        ),
        sources=["eXistenZ (film). Alliance Atlantis / Dimension Films, 1999."],
        cpc_classifications=["A61B 5/0031", "A61M 39/02", "G06F 3/01"],
    ),
    E(
        id="the-matrix-headjack",
        canonical_name="The Matrix — cranial 'headjack' neural-interface socket",
        aliases=["headjack", "the jack", "Matrix neural socket"],
        first_disclosure_date="1999-03-31",
        disclosure_citation="The Matrix (Warner Bros. / Village Roadshow), released 31 March 1999; a socket implanted at the back of the skull accepts a probe ('jacking in') providing full-sensory bidirectional neural connection to a simulated environment and supporting rapid 'download' of skills into the brain.",
        creator="The Wachowskis / Village Roadshow",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["occiput", "skull", "brain"],
        output_modalities=["data-only"],
        lineage_descendants=["existenz-bioport-and-game-pod"],
        prior_art_notes=(
            "Discloses a cranial socket implant providing a wired, full-sensory, "
            "bidirectional neural connection between the brain and an external system, "
            "including bulk transfer of procedural knowledge into the brain. Relevant to "
            "implanted-neural-port and neural-data-transfer claims. § 103 motivation as of "
            "1999. Cf. [[existenz-bioport-and-game-pod]], [[neuromancer-simstim-and-trodes]], "
            "[[gibson-neuromancer-microsoft-skill-chips]]."
        ),
        sources=["The Matrix (film). Warner Bros. / Village Roadshow, 1999."],
        cpc_classifications=["A61B 5/0031", "A61M 39/02", "G06F 3/01", "G06N 20/00"],
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
    print(f"  fiction round 5: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
