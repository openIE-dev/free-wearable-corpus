#!/usr/bin/env python3
"""seed_2026q3_fiction_r4.py — fictional seed batch round 4.

Thickening the thin form factors: rings, dental, footwear/powered legwear,
contact lenses, belt, headgear — plus the deep "bionics" antecedents
(Cyborg / The Six Million Dollar Man, The Bionic Woman, Darth Vader's
life-support suit).

Run from repo root:

    python3 seeds/seed_2026q3_fiction_r4.py

Idempotent — skips ids already present.

Notes:
- Several entries here are necessarily Tier 2 (reference-only): fiction's
  ring, dental, belt, and headgear depictions rarely disclose enough to
  carry a full element-by-element analysis. They reserve the slug, anchor
  the form-factor cross-cut, and document the concept's earliest appearance.
- One entry (Mercury's winged sandals) carries an ISO 8601 negative year
  ("-0600", astronomical year numbering ≈ 601 BCE). The index tables slice
  the year to four characters, so it renders as "-060" there; the cross-cut
  pages show the full string. Harmless.
- Dental fiction is still sparse — `kingsman-poison-tooth` is the one
  reasonably-citable example; the "transmitter in a molar" pulp trope is
  omitted for lack of a clean primary source.

Doctrinal note (same as rounds 1-3): fictional disclosures are generally
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
    # ---------------- RINGS ----------------
    E(
        id="lotr-one-ring",
        canonical_name="The One Ring (Tolkien)",
        aliases=["the One Ring", "Sauron's ring", "Isildur's Bane"],
        first_disclosure_date="1937-09-21",
        disclosure_citation="Tolkien, J.R.R. The Hobbit. George Allen & Unwin, 1937 (its nature elaborated in The Lord of the Rings, 1954-1955) — a finger-worn ring that renders the wearer invisible (alters the wearer's perceptual visibility), maintains a remote link to its maker (who senses when it is worn), and exhibits intent-responsive behaviour of its own.",
        creator="J.R.R. Tolkien",
        creator_country="GB",
        form_factor="ring",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents a finger-worn device that, when worn, (a) changes "
            "the wearer's state with respect to external observation, (b) establishes a "
            "covert remote link back to a controlling party, and (c) responds to/asserts "
            "intent. Thin as prior art (magical, non-enabling) but contributes the "
            "'finger-worn device with a remote link and intent-responsive behaviour' "
            "concept circa 1937 to the smart-ring form-factor cross-cut."
        ),
        sources=[
            "Tolkien, J.R.R. The Hobbit. George Allen & Unwin, 1937.",
            "Tolkien, J.R.R. The Lord of the Rings. George Allen & Unwin, 1954-1955.",
        ],
        cpc_classifications=["G06F 1/163"],
    ),
    E(
        id="flash-costume-ring",
        canonical_name="The Flash's costume ring (compacted-garment storage ring)",
        aliases=["Flash ring", "Barry Allen costume ring"],
        first_disclosure_date="1959-10",
        disclosure_citation="The Flash #105 (cover date Feb-Mar 1959; on sale October 1959), DC Comics — a finger-worn ring containing the wearer's full bodysuit compressed inside, ejected and self-expanding on a button press, and re-stowed afterward.",
        creator="John Broome / Carmine Infantino / DC Comics",
        creator_country="US",
        form_factor="ring",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents a finger-worn ring used as a compact storage and "
            "deployment device for a flexible worn article (a full garment) — release on "
            "command, self-expansion, and re-compaction. Contributes the 'ring as a "
            "deployment carrier for a compacted flexible wearable' concept circa 1959 to "
            "the smart-ring form-factor cross-cut; loosely relevant to ring-stored "
            "deployable-textile / deployable-display claims."
        ),
        sources=[
            "Broome, John; Infantino, Carmine. The Flash #105. DC Comics, 1959.",
        ],
        cpc_classifications=["G06F 1/163", "A41D 1/00"],
    ),
    E(
        id="mandarin-ten-rings",
        canonical_name="The Ten Rings (Marvel — the Mandarin / Wenwu)",
        aliases=["the Ten Rings", "Mandarin's rings"],
        first_disclosure_date="1964-02",
        disclosure_citation="Tales of Suspense #50 (cover date February 1964), Marvel Comics — a set of finger-worn rings (depicted as forearm bands in Shang-Chi and the Legend of the Ten Rings, 2021), each an energy-projecting device responsive to the wielder's command.",
        creator="Stan Lee / Don Heck / Marvel Comics",
        creator_country="US",
        form_factor="ring",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents a set of finger-/forearm-worn devices each capable "
            "of directed energy output under the wearer's command, worn as a coordinated "
            "array. Thin as prior art but contributes the 'array of finger-worn output "
            "devices under unified wearer control' concept circa 1964 to the smart-ring "
            "form-factor cross-cut."
        ),
        sources=[
            "Lee, Stan; Heck, Don. Tales of Suspense #50. Marvel Comics, 1964.",
        ],
        cpc_classifications=["G06F 1/163", "G06F 3/01"],
    ),
    # ---------------- DENTAL ----------------
    E(
        id="kingsman-poison-tooth",
        canonical_name="Kingsman lethal-capsule molar (dental implant with deployable payload)",
        aliases=["Kingsman poison tooth", "kill-pill molar"],
        first_disclosure_date="2014-12-13",
        disclosure_citation="Kingsman: The Secret Service (20th Century Fox / Marv Films), 2014 — an agency-issued capsule concealed within a back molar, deployable by the wearer's bite/tongue action.",
        creator="Matthew Vaughn / Marv Films",
        creator_country="GB",
        form_factor="dental",
        contact_surface="dental",
        anatomical_target=["molar", "oral-cavity"],
        tier=2,
        output_modalities=["drug-delivery"],
        prior_art_notes=(
            "Reference-only — the only reasonably-citable fictional dental device. "
            "Documents a tooth-mounted housing containing a deployable payload, released "
            "by the wearer's intentional oral action. Loosely relevant to "
            "intraoral/dental-appliance claims that house and release a substance on a "
            "trigger (dental drug-eluting appliances; intraoral capsule devices). "
            "Promote/expand if a richer dental fiction example surfaces."
        ),
        sources=[
            "Kingsman: The Secret Service (film). 20th Century Fox / Marv Films, 2014.",
        ],
        cpc_classifications=["A61C 19/00", "A61K 9/00"],
    ),
    # ---------------- SUBDERMAL HAND DEVICE (contact-lens-adjacent epidermal electronics) ----------------
    E(
        id="total-recall-2012-palm-phone",
        canonical_name="Total Recall (2012) — subdermal palm phone with through-skin display",
        aliases=["hand phone (Total Recall 2012)", "palm communicator"],
        first_disclosure_date="2012-08-03",
        disclosure_citation="Total Recall (Columbia Pictures), released August 3, 2012; a telephone implanted in the wearer's hand — dial pad and display visible through the skin of the palm, speaker/microphone in the hand, glass surfaces used as touch interfaces.",
        creator="Len Wiseman / Columbia Pictures",
        creator_country="US",
        form_factor="implantable",
        form_factor_tags=["tattoo-electronic"],
        contact_surface="sub-dermal",
        anatomical_target=["palm", "hand"],
        sensors=["sensor-microphone-air"],
        output_modalities=["visual-display", "audio"],
        connectivity="cellular (fictional)",
        prior_art_notes=(
            "Discloses a subdermally-implanted electronic device with a display rendered "
            "so as to be visible through the overlying skin, touch input on the skin "
            "surface, and audio I/O — i.e. an epidermal/sub-dermal communicator in the "
            "hand. Relevant to implantable / electronic-skin claims combining 'a "
            "sub-dermal electronic device', 'a display perceptible through the skin', and "
            "'touch input at the skin surface'. § 103 motivation that the through-skin "
            "sub-dermal display device was an articulated objective by 2012. Non-enabling "
            "on the display/skin optics; pair with enabling flexible-display and "
            "biocompatible-electronics art."
        ),
        sources=[
            "Total Recall (film). Columbia Pictures, 2012.",
        ],
        cpc_classifications=["A61B 5/00", "G06F 1/16", "H04M 1/05", "A61B 5/0031"],
    ),
    # ---------------- FOOTWEAR / POWERED LEGWEAR ----------------
    E(
        id="mercury-winged-sandals-talaria",
        canonical_name="Winged sandals of Hermes/Mercury (the talaria)",
        aliases=["talaria", "winged sandals", "Hermes' sandals"],
        first_disclosure_date="-0600",
        disclosure_citation="Greek mythology; Hesiod, Theogony (c. 700 BCE) and the Homeric Hymn to Hermes (c. 6th century BCE) attribute to Hermes a pair of winged sandals (talaria) that confer flight on the wearer. (ISO 8601 negative year used; ≈ 601 BCE astronomical numbering.)",
        creator="Greek mythological tradition (Hesiod; Homeric Hymns)",
        creator_country="GR",
        form_factor="shoe",
        tier=2,
        output_modalities=["data-only"],
        notes="Deep mythological antecedent — likely the earliest entry in the corpus by date. ISO 8601 negative year; the index tables slice the year to four characters and render '-060'.",
        prior_art_notes=(
            "Reference-only. Earliest recorded depiction of footwear that confers an "
            "augmented locomotion capability on the wearer — the foundational 'powered/"
            "augmented shoe' concept. Non-enabling, but documents that the worn-footwear-"
            "as-a-locomotion-augmentation-platform idea is roughly 2,600 years old, which "
            "is relevant context for any patent claiming the bare concept of "
            "locomotion-augmenting footwear."
        ),
        sources=[
            "Hesiod. Theogony. c. 700 BCE.",
            "Homeric Hymn to Hermes. c. 6th century BCE.",
        ],
        cpc_classifications=["A43B 3/00", "A43B 5/00"],
    ),
    E(
        id="seven-league-boots-perrault",
        canonical_name="Seven-league boots (bottes de sept lieues)",
        aliases=["seven-league boots", "bottes de sept lieues"],
        first_disclosure_date="1697",
        disclosure_citation="Perrault, Charles. 'Le Petit Poucet' ('Hop-o'-My-Thumb'), in Histoires ou contes du temps passé, 1697 — boots that let the wearer cover seven leagues at a single stride, fitting any wearer.",
        creator="Charles Perrault",
        creator_country="FR",
        form_factor="shoe",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents footwear that augments the wearer's stride/range "
            "and self-adjusts to fit any wearer — the augmented-locomotion-shoe concept "
            "in early-modern European fiction. Contributes to the footwear form-factor "
            "cross-cut and to the long-pedigree context for locomotion-augmenting and "
            "self-fitting footwear claims."
        ),
        sources=[
            "Perrault, Charles. Histoires ou contes du temps passé, avec des moralités. Claude Barbin, 1697.",
        ],
        cpc_classifications=["A43B 3/00", "A43B 3/34"],
    ),
    E(
        id="wizard-of-oz-ruby-slippers",
        canonical_name="Ruby slippers (The Wizard of Oz) / silver shoes (Baum)",
        aliases=["ruby slippers", "silver shoes of Oz"],
        first_disclosure_date="1900-05-17",
        disclosure_citation="Baum, L. Frank. The Wonderful Wizard of Oz. George M. Hill Co., 1900 — the silver shoes (recolored ruby for the 1939 MGM film) that transport the wearer to a chosen destination when the wearer activates them by a deliberate action (clicking the heels together) coupled with stated intent.",
        creator="L. Frank Baum",
        creator_country="US",
        form_factor="shoe",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents footwear with a wearer-activated function triggered "
            "by an intentional gesture (heel-click) combined with a spoken target — i.e. "
            "gesture-plus-voice activation of a wearable's function. Thin and non-enabling, "
            "but contributes the 'footwear function invoked by a deliberate foot gesture "
            "and a spoken command' concept circa 1900 to the footwear cross-cut."
        ),
        sources=[
            "Baum, L. Frank. The Wonderful Wizard of Oz. George M. Hill Co., 1900.",
            "The Wizard of Oz (film). Metro-Goldwyn-Mayer, 1939.",
        ],
        cpc_classifications=["A43B 3/00", "G06F 3/01"],
    ),
    E(
        id="wallace-gromit-techno-trousers",
        canonical_name="Wallace & Gromit 'Techno Trousers' (powered automated legwear)",
        aliases=["Techno Trousers", "Wrong Trousers", "Ex-NASA techno trousers"],
        first_disclosure_date="1993-12-17",
        disclosure_citation="The Wrong Trousers (Aardman Animations / BBC), broadcast December 17, 1993 — robotic trousers worn around the legs that walk under their own power, can be programmed to follow a route, and can be remotely commandeered, with the wearer carried along inside.",
        creator="Nick Park / Aardman Animations",
        creator_country="GB",
        form_factor="garment",
        form_factor_tags=["exoskeleton", "legband"],
        contact_surface="skin",
        anatomical_target=["legs", "hips"],
        output_modalities=["data-only"],
        connectivity="remote control link (fictional)",
        prior_art_notes=(
            "Discloses a powered lower-body garment (trousers) that actuates the wearer's "
            "legs to produce locomotion, executes a pre-programmed route autonomously, and "
            "accepts override commands over a remote link. Relevant to powered-legwear / "
            "lower-body-exoskeleton claims combining 'a garment worn about the legs', "
            "'actuators driving leg motion', 'an autonomous gait controller', and 'a remote "
            "command interface'. § 103 motivation that the powered, autonomously-walking "
            "lower-body garment was an articulated objective by 1993."
        ),
        sources=[
            "The Wrong Trousers (film). Aardman Animations / BBC, 1993.",
        ],
        cpc_classifications=["A61H 3/00", "B25J 9/00", "A41D 1/06"],
    ),
    # ---------------- CONTACT LENS / GLASSES ----------------
    E(
        id="mi-ghost-protocol-contact-lens-camera",
        canonical_name="Mission: Impossible – Ghost Protocol — contact-lens camera and document scanner",
        aliases=["Ghost Protocol contact lenses", "blink-to-capture lenses"],
        first_disclosure_date="2011-12-16",
        disclosure_citation="Mission: Impossible – Ghost Protocol (Paramount Pictures), released December 16, 2011; contact lenses that capture imagery on a deliberate double-blink, store and wirelessly transmit it, and scan documents for relay to a body-worn printer.",
        creator="Brad Bird / Paramount Pictures",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea"],
        sensors=["sensor-camera-rgb", "sensor-camera-eye"],
        output_modalities=["data-only"],
        connectivity="short-range wireless (fictional)",
        prior_art_notes=(
            "Discloses a corneal contact lens incorporating an image sensor, triggered by "
            "an intentional eyelid gesture (double-blink), with on-lens or near-body "
            "storage and wireless transmission of the captured imagery. Relevant to "
            "contact-lens claims combining 'a contact lens', 'an image sensor', 'a "
            "blink-detection trigger', and 'wireless transmission of captured images'. "
            "§ 103 motivation that the camera-bearing, blink-triggered contact lens was "
            "an articulated objective by 2011. Non-enabling on lens-scale optics/power; "
            "pair with enabling contact-lens-electronics art."
        ),
        lineage_ancestors=["rainbows-end-ar-contact-lens"],
        sources=[
            "Mission: Impossible – Ghost Protocol (film). Paramount Pictures, 2011.",
        ],
        cpc_classifications=["G02C 7/04", "A61B 3/113", "H04N 23/00", "G02C 11/00"],
    ),
    E(
        id="kingsman-ar-glasses",
        canonical_name="Kingsman AR glasses (HUD, recording, X-ray, scanning, holographic conferencing)",
        aliases=["Kingsman glasses", "Kingsman spectacles"],
        first_disclosure_date="2014-12-13",
        disclosure_citation="Kingsman: The Secret Service (20th Century Fox / Marv Films), 2014; agency eyeglasses providing a heads-up information overlay, point-of-view video recording, see-through (X-ray-style) imaging, object/person scanning, and rendering of remote participants as holographic avatars seated around a table.",
        creator="Matthew Vaughn / Marv Films",
        creator_country="GB",
        form_factor="glasses",
        sensors=["sensor-camera-rgb", "sensor-camera-ir"],
        output_modalities=["visual-display", "data-only"],
        connectivity="wireless (fictional)",
        prior_art_notes=(
            "Discloses eyeglasses integrating: a near-eye information HUD; an outward "
            "camera with POV recording; a see-through imaging mode; an object/person "
            "scanning-and-identification function; and shared telepresence rendering "
            "remote participants as registered holographic avatars in the wearer's view. "
            "Relevant to AR-glasses claims combining 'an eyewear frame', 'a near-eye "
            "display', 'an outward camera', 'recording', 'on-view object/person "
            "identification', and 'shared/telepresence AR'. § 103 motivation that the "
            "fully-featured AR information eyewear was an articulated objective by 2014."
        ),
        lineage_ancestors=["snow-crash-gargoyle-rig", "rainbows-end-ar-contact-lens"],
        sources=[
            "Kingsman: The Secret Service (film). 20th Century Fox / Marv Films, 2014.",
        ],
        cpc_classifications=["G02B 27/01", "G06F 3/01", "G06V 40/16", "H04N 7/15"],
    ),
    # ---------------- BELT / HEADGEAR ----------------
    E(
        id="batman-utility-belt",
        canonical_name="Batman's utility belt",
        aliases=["Bat-utility belt"],
        first_disclosure_date="1939-05",
        disclosure_citation="Detective Comics #29 (cover date July 1939; on sale May 1939), DC Comics — a worn waist belt with compartmented pouches carrying an array of tools and devices, the canonical 'belt as a wearable equipment platform'.",
        creator="Bob Kane / Bill Finger / DC Comics",
        creator_country="US",
        form_factor="belt",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents a worn waist belt structured as a modular carrier "
            "for an array of functional devices and tools — the belt-as-wearable-platform "
            "concept. Thin as prior art on its own, but opens the belt form-factor "
            "cross-cut and is the long-pedigree antecedent for waist-worn modular-device "
            "and tool-platform belt claims."
        ),
        sources=[
            "Kane, Bob; Finger, Bill. Detective Comics #29. DC Comics, 1939.",
        ],
        cpc_classifications=["A45F 5/00", "G06F 1/163"],
    ),
    E(
        id="inspector-gadget-gadget-hat",
        canonical_name="Inspector Gadget's headgear ('Gadget-copter' hat)",
        aliases=["Gadget hat", "Go-go-gadget hat"],
        first_disclosure_date="1983-09-12",
        disclosure_citation="Inspector Gadget (DIC animated series), premiered 1983; the protagonist's hat houses an array of voice-commanded deployable mechanisms — a helicopter rotor, a parachute, springs, and more.",
        creator="DIC Audiovisuel",
        creator_country="FR",
        form_factor="cap",
        form_factor_tags=["helmet"],
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Documents headgear functioning as a host platform for "
            "multiple voice-commanded deployable mechanisms. Thin as prior art but "
            "contributes the 'headgear as a multi-function deployable-mechanism platform "
            "under voice control' concept circa 1983 to the headgear cross-cut."
        ),
        sources=[
            "Inspector Gadget. DIC Audiovisuel / Cuckoo's Nest Studios, 1983.",
        ],
        cpc_classifications=["A42B 1/00", "A42B 3/04", "G06F 3/16"],
    ),
    # ---------------- BIONICS ANTECEDENTS ----------------
    E(
        id="caidin-cyborg-bionics",
        canonical_name="Cyborg / The Six Million Dollar Man — bionic eye and limbs with sensing",
        aliases=["Steve Austin bionics", "bionic eye", "The Six Million Dollar Man"],
        first_disclosure_date="1972",
        disclosure_citation="Caidin, Martin. Cyborg. Arbor House, 1972 (television series The Six Million Dollar Man, ABC, 1973-1978) — a man fitted with a prosthetic eye providing zoom, telescopic, and infrared vision; prosthetic limbs with augmented force; and integrated sensing and telemetry of the prosthetics' state.",
        creator="Martin Caidin",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["eye", "arm", "legs"],
        sensors=["sensor-camera-ir"],
        clinical_endpoints=["prosthetic-status"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a prosthetic ocular implant offering switchable imaging modes "
            "(optical zoom, telescopic magnification, infrared) feeding the wearer's "
            "visual perception, together with powered prosthetic limbs whose force output "
            "and internal state are sensed and reported. Relevant to ocular-sensor-implant "
            "claims combining 'a prosthetic eye', 'multi-mode imaging', and 'coupling to "
            "the visual system', and to powered-prosthesis claims combining 'an actuator', "
            "'force/state sensing', and 'telemetry'. § 103 motivation that the multi-mode "
            "ocular implant and the sensored powered prosthesis were articulated objectives "
            "by 1972. Non-enabling; pair with enabling retinal-prosthesis / "
            "powered-prosthesis art."
        ),
        sources=[
            "Caidin, Martin. Cyborg. Arbor House, 1972.",
            "The Six Million Dollar Man (television series). ABC / Universal, 1973-1978.",
        ],
        cpc_classifications=["A61F 2/14", "A61F 9/08", "A61F 2/72", "A61B 5/00"],
    ),
    E(
        id="bionic-woman-bionic-ear",
        canonical_name="The Bionic Woman — bionic ear (augmented, frequency-selective hearing)",
        aliases=["Jaime Sommers bionic ear", "bionic hearing"],
        first_disclosure_date="1976-01-14",
        disclosure_citation="The Bionic Woman (ABC, premiered January 14, 1976) — a prosthetic ear giving the wearer greatly amplified hearing with the ability to tune to and isolate specific sound sources and frequencies at a distance.",
        creator="Kenneth Johnson / Universal Television",
        creator_country="US",
        form_factor="hearing-aid",
        form_factor_tags=["implantable"],
        contact_surface="ear",
        anatomical_target=["ear", "cochlea"],
        sensors=["sensor-microphone-air"],
        clinical_endpoints=["auditory-perception"],
        output_modalities=["audio"],
        prior_art_notes=(
            "Discloses a prosthetic hearing device providing amplified hearing plus "
            "directional/frequency-selective listening — the wearer can steer toward and "
            "isolate a chosen sound source or band. Relevant to hearing-device claims "
            "combining 'a worn or implanted hearing prosthesis', 'amplification', and "
            "'beamforming / frequency-selective source isolation' (modern hearable and "
            "hearing-aid 'focus' / 'conversation isolation' features). § 103 motivation "
            "that the steerable, frequency-selective augmented-hearing device was an "
            "articulated objective by 1976. Non-enabling; pair with enabling "
            "beamforming-hearing-aid art."
        ),
        lineage_ancestors=["caidin-cyborg-bionics"],
        sources=[
            "The Bionic Woman (television series). ABC / Universal, 1976.",
        ],
        cpc_classifications=["H04R 25/00", "H04R 25/40", "A61F 2/18"],
    ),
    E(
        id="darth-vader-life-support-suit",
        canonical_name="Darth Vader life-support suit (wearable respiratory support and biometric monitoring)",
        aliases=["Vader suit", "Vader armor", "Vader life-support system"],
        first_disclosure_date="1977-05-25",
        disclosure_citation="Star Wars (Episode IV: A New Hope) (Lucasfilm / 20th Century Fox), released May 25, 1977; a full-body armored garment integrating a respiratory support apparatus, prosthetic-limb control, body-state monitoring, voice processing, and a chest-mounted control/status panel, keeping a critically injured wearer functional.",
        creator="George Lucas / Lucasfilm",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["exoskeleton", "helmet"],
        contact_surface="skin",
        anatomical_target=["torso", "limbs", "head", "airway"],
        clinical_endpoints=["respiration", "heart-rate", "prosthetic-status"],
        actuators=["audio"],
        output_modalities=["audio", "visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a wearable, full-body life-support garment integrating: an "
            "ambulatory respiratory-assist system; continuous monitoring of the wearer's "
            "vital signs and prosthetic-limb state; a wearer-accessible control/status "
            "panel; prosthetic-limb actuation/control; and voice capture and processing. "
            "Relevant to wearable life-support and body-monitoring-garment claims combining "
            "'a body-worn garment', 'an integrated respiratory-support module', 'sensors "
            "monitoring the wearer's vitals', 'an onboard status display/control', and "
            "'prosthesis integration'. § 103 motivation that the ambulatory wearable "
            "life-support-and-monitoring suit was an articulated objective by 1977."
        ),
        sources=[
            "Star Wars (Episode IV: A New Hope) (film). Lucasfilm / 20th Century Fox, 1977.",
        ],
        cpc_classifications=["A61M 16/00", "A61B 5/00", "A41D 13/00", "A61F 2/70"],
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

    print(f"  fiction round 4: added {added}, skipped {skipped} (already present)")
    print("  next:")
    print("    python3 tools/validate.py corpus.jsonl --strict")
    print("    python3 tools/index.py .")
    print("    python3 tools/cross_cuts.py")


if __name__ == "__main__":
    main()
