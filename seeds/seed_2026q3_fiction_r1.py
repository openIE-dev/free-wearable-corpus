#!/usr/bin/env python3
"""seed_2026q3_fiction_r1.py — fictional seed batch round 1.

Watch / bracelet / eyewear / body-measurement fiction. Run from repo root:

    python3 seeds/seed_2026q3_fiction_r1.py

Appends entries to corpus.jsonl (idempotent — skips ids already present),
then reminds you to validate + regenerate.

Doctrinal note: fictional disclosures are generally non-enabling and are
therefore weak 35 U.S.C. § 102 anticipation references. Their value is as
§ 103 motivation-to-combine evidence — they establish that a POSITA would
have been motivated toward the claimed combination. The prior_art_notes
below say so where relevant. See OBVIOUSNESS_TEMPLATE.md "doctrinal limits".
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
    # ---------------- WATCH / WRIST ----------------
    E(
        id="dick-tracy-2way-wrist-radio",
        canonical_name="Dick Tracy 2-Way Wrist Radio",
        aliases=["Tracy wrist radio"],
        first_disclosure_date="1946-01-13",
        disclosure_citation="Dick Tracy comic strip, Chester Gould; the '2-Way Wrist Radio' introduced January 13, 1946 (Chicago Tribune syndicate).",
        creator="Chester Gould",
        creator_country="US",
        form_factor="watch",
        actuators=["audio"],
        output_modalities=["audio", "data-only"],
        connectivity="two-way radio (fictional)",
        prior_art_notes=(
            "Earliest broadly-disseminated depiction of a wrist-mounted, full-duplex "
            "voice-communication device worn on the wrist like a watch. Discloses the "
            "form-factor element ('a wristworn communication device') and the bidirectional "
            "audio I/O element of modern wristworn-comm and smartwatch-telephony claims. "
            "Non-enabling (no circuit disclosure) so weak as § 102 art, but strong § 103 "
            "motivation evidence: by 1946 a POSITA would have been motivated to place "
            "two-way voice comms on the wrist. Pair with enabling radio/telephony art."
        ),
        sources=[
            "Gould, Chester. Dick Tracy (comic strip). Chicago Tribune syndicate, 1946.",
            "Roberts, Garyn G. Dick Tracy and American Culture. McFarland, 1993. ISBN 0-89950-739-1.",
        ],
        cpc_classifications=["G04G 21/04", "H04M 1/05"],
    ),
    E(
        id="dick-tracy-2way-wrist-tv",
        canonical_name="Dick Tracy 2-Way Wrist TV",
        aliases=["Tracy wrist TV"],
        first_disclosure_date="1964",
        disclosure_citation="Dick Tracy comic strip, Chester Gould; the '2-Way Wrist TV' introduced 1964, succeeding the 1946 wrist radio.",
        creator="Chester Gould",
        creator_country="US",
        form_factor="watch",
        sensors=["sensor-camera-rgb"],
        actuators=["audio"],
        output_modalities=["audio", "visual-display"],
        connectivity="two-way video radio (fictional)",
        lineage_ancestors=["dick-tracy-2way-wrist-radio"],
        prior_art_notes=(
            "Adds a camera and a video display to the wristworn-comm form factor — i.e. "
            "wristworn two-way video calling. Discloses the 'a display' element, the 'an "
            "image sensor' element, and the 'configured to transmit/receive video' element "
            "of wristworn-videophone and smartwatch-camera claims. Non-enabling; serves "
            "§ 103 motivation that wristworn video telephony was a known objective by 1964."
        ),
        sources=[
            "Gould, Chester. Dick Tracy (comic strip). Chicago Tribune syndicate, 1964.",
        ],
        cpc_classifications=["G04G 21/04", "H04N 7/14"],
    ),
    E(
        id="jetsons-wrist-communicator",
        canonical_name="The Jetsons wrist communicator / video watch",
        aliases=["Jetsons watch-phone"],
        first_disclosure_date="1962-09-23",
        disclosure_citation="The Jetsons (Hanna-Barbera animated series), premiered September 23, 1962, ABC; recurring wristworn video-communication device.",
        creator="Hanna-Barbera Productions",
        creator_country="US",
        form_factor="watch",
        sensors=["sensor-camera-rgb"],
        actuators=["audio"],
        output_modalities=["audio", "visual-display"],
        prior_art_notes=(
            "Mass-audience depiction of a wristworn device combining a display, a camera, "
            "and two-way audio for video calling, plus ancillary timekeeping. Reinforces "
            "the § 103 record that a wristworn videophone/smartwatch combining display + "
            "camera + audio + clock was an articulated design objective by the early 1960s."
        ),
        sources=[
            "The Jetsons. Hanna-Barbera Productions / Screen Gems, 1962-1963.",
        ],
        cpc_classifications=["G04G 21/04", "H04N 7/14"],
    ),
    E(
        id="knight-rider-comlink-watch",
        canonical_name="Knight Rider Comlink wristwatch",
        aliases=["Michael Knight comlink"],
        first_disclosure_date="1982-09-26",
        disclosure_citation="Knight Rider (NBC television series), premiered September 26, 1982; the 'Comlink' wristwatch links the wearer to the vehicle AI KITT.",
        creator="Glen A. Larson / Universal Television",
        creator_country="US",
        form_factor="watch",
        actuators=["audio"],
        output_modalities=["audio", "data-only"],
        connectivity="wireless link to remote computer (fictional)",
        prior_art_notes=(
            "Discloses a wristworn voice terminal that is a thin client to a remote compute "
            "agent — i.e. wristworn always-available access to a networked assistant, with "
            "voice in/out. Relevant to smartwatch-as-companion-device and wristworn-"
            "voice-assistant claims; § 103 motivation that the 'watch as remote-agent "
            "terminal' pattern predates modern implementations."
        ),
        sources=[
            "Knight Rider. Universal Television, 1982-1986.",
        ],
        cpc_classifications=["G04G 21/04", "G06F 1/163"],
    ),
    E(
        id="inspector-gadget-wrist-computer",
        canonical_name="Inspector Gadget's wrist computer ('Gadget-phone')",
        aliases=["Gadget-phone", "Inspector Gadget wristwatch"],
        first_disclosure_date="1983-09-12",
        disclosure_citation="Inspector Gadget (DIC animated series), premiered 1983; the multi-function wrist device used for video communication with HQ.",
        creator="DIC Audiovisuel",
        creator_country="FR",
        form_factor="watch",
        sensors=["sensor-camera-rgb"],
        actuators=["audio"],
        output_modalities=["audio", "visual-display"],
        prior_art_notes=(
            "Wristworn multi-function device with display, camera, two-way audio, and "
            "general-purpose 'computer' framing. Cumulative § 103 motivation evidence for "
            "the wristworn-multifunction-computer (smartwatch) concept circa early 1980s."
        ),
        sources=[
            "Inspector Gadget. DIC Audiovisuel / Cuckoo's Nest Studios, 1983.",
        ],
        cpc_classifications=["G04G 21/04", "G06F 1/163"],
    ),
    # ---------------- BRACELET / BADGE ----------------
    E(
        id="wonder-woman-bracelets",
        canonical_name="Wonder Woman's bracelets (Bracelets of Submission)",
        aliases=["Bracelets of Submission", "Amazonium bracelets"],
        first_disclosure_date="1941-12",
        disclosure_citation="All Star Comics #8 (cover date December 1941, published October 1941), DC Comics; first appearance of Wonder Woman and her wrist-worn bracelets.",
        creator="William Moulton Marston / DC Comics",
        creator_country="US",
        form_factor="bracelet",
        tier=2,
        prior_art_notes=(
            "Reference-only. Documents a worn-on-the-wrist functional device (here, a "
            "deflective shield). No physiological-sensing disclosure; limited prior-art "
            "applicability beyond the bare 'bracelet/wristband as a functional body-worn "
            "object' concept. Included for completeness of the bracelet form-factor "
            "cross-cut. Promote to Tier 1 only if a sensing/measurement reading is added."
        ),
        sources=[
            "Marston, William Moulton (as 'Charles Moulton'). All Star Comics #8. DC Comics, 1941.",
        ],
    ),
    E(
        id="star-trek-tng-combadge",
        canonical_name="Star Trek combadge (Starfleet communicator badge)",
        aliases=["combadge", "Starfleet comm badge"],
        first_disclosure_date="1987-09-28",
        disclosure_citation="Star Trek: The Next Generation, 'Encounter at Farpoint' (premiered September 28, 1987); chest-worn combadge providing voice-activated communications and (in later depictions) crew biometric/location lock.",
        creator="Gene Roddenberry / Paramount Television",
        creator_country="US",
        form_factor="pendant",
        form_factor_tags=["garment"],
        actuators=["audio"],
        output_modalities=["audio", "data-only"],
        clinical_endpoints=["location", "wearer-identity"],
        connectivity="ship-wide wireless mesh (fictional)",
        prior_art_notes=(
            "Discloses a chest-worn, garment-attached badge that is (a) a hands-free, "
            "voice-activated communicator, (b) a continuous wearer-identification token, "
            "and (c) a real-time location beacon usable to resolve who-is-where. Relevant "
            "to wearable-badge claims combining voice UI + identity + indoor positioning "
            "(hospital/enterprise comm-badge patents, e.g. the Vocera lineage). § 103 "
            "motivation that the voice-badge + identity + location triad was a stated "
            "objective by 1987."
        ),
        sources=[
            "Star Trek: The Next Generation. Paramount Television, 1987.",
            "Sternbach, Rick; Okuda, Michael. Star Trek: The Next Generation Technical Manual. Pocket Books, 1991. ISBN 0-671-70427-3.",
        ],
        cpc_classifications=["G06F 1/163", "G08B 21/02", "H04W 4/029"],
    ),
    # ---------------- IMPLANTABLE / BODY-EMBEDDED ----------------
    E(
        id="logans-run-lifeclock",
        canonical_name="Logan's Run 'Lifeclock' palm crystal",
        aliases=["Lifeclock", "palm flower crystal"],
        first_disclosure_date="1967",
        disclosure_citation="Nolan, William F.; Johnson, George Clayton. Logan's Run. Dial Press, 1967 — the palm-embedded crystal that changes color as the bearer approaches the mandated termination age. (Film: MGM, 1976, with the palm 'Lifeclock'.)",
        creator="William F. Nolan and George Clayton Johnson",
        creator_country="US",
        form_factor="implantable",
        form_factor_tags=["tattoo-electronic"],
        contact_surface="sub-dermal",
        anatomical_target=["palm"],
        output_modalities=["visual-display"],
        clinical_endpoints=["age", "time-remaining"],
        prior_art_notes=(
            "Discloses a body-embedded, color-coded status display readable directly off "
            "the skin — a sub-dermal indicator that changes hue to communicate a tracked "
            "state variable. Relevant to (a) implantable/epidermal display claims and "
            "(b) color-mapped wearable status-indicator claims (the now-common "
            "green/amber/red 'zone' UI on fitness wearables). Non-enabling; § 103 "
            "motivation that a body-worn color-state display was an articulated concept by "
            "1967. Note: the crystal is a countdown timer, not a sensor — value is the "
            "display+colormap element, not measurement."
        ),
        sources=[
            "Nolan, William F.; Johnson, George Clayton. Logan's Run. Dial Press, 1967.",
            "Logan's Run (film). Metro-Goldwyn-Mayer, 1976.",
        ],
        cpc_classifications=["A61B 5/00", "G09F 9/00"],
    ),
    # ---------------- EYEWEAR / HUD ----------------
    E(
        id="terminator-t800-hud",
        canonical_name="Terminator T-800 vision HUD",
        aliases=["T-800 POV display", "Terminator vision"],
        first_disclosure_date="1984-10-26",
        disclosure_citation="The Terminator (Orion Pictures), released October 26, 1984; the T-800's first-person heads-up display overlaying target identification, status readouts, and option menus on a machine-vision feed.",
        creator="James Cameron / Hemdale Film / Orion Pictures",
        creator_country="US",
        form_factor="fictional-other",
        form_factor_tags=["goggles", "helmet"],
        sensors=["sensor-camera-rgb", "sensor-camera-ir"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses a head-/eye-locked augmented-reality overlay: a live camera feed "
            "annotated in real time with object/threat identification, persistent status "
            "indicators, and selectable text menus. Relevant to AR-HUD eyewear and helmet "
            "claims combining 'an image sensor', 'a near-eye display', and 'a processor "
            "configured to overlay object-recognition results'. § 103 motivation that the "
            "annotated-live-feed near-eye HUD was a concrete design objective by 1984. "
            "Non-enabling on the recognition pipeline; pair with enabling computer-vision art."
        ),
        sources=[
            "The Terminator (film). Orion Pictures, 1984.",
        ],
        cpc_classifications=["G02B 27/01", "G06F 3/01", "G06V 20/20"],
    ),
    E(
        id="star-trek-tng-visor",
        canonical_name="Geordi La Forge's VISOR (Star Trek: TNG)",
        aliases=["VISOR", "Visual Instrument and Sensory Organ Replacement"],
        first_disclosure_date="1987-09-28",
        disclosure_citation="Star Trek: The Next Generation, 'Encounter at Farpoint' (premiered September 28, 1987); the VISOR — eyewear that senses across the electromagnetic spectrum and couples the signal to the wearer's optic nerves.",
        creator="Gene Roddenberry / Paramount Television",
        creator_country="US",
        form_factor="glasses",
        contact_surface="sub-dermal",
        anatomical_target=["temples", "optic-nerve"],
        sensors=["sensor-camera-ir", "sensor-camera-thermal"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses sensory-substitution eyewear: a head-worn multi-spectral sensor "
            "(IR/thermal and beyond) whose output is rendered to the wearer as perception, "
            "via direct neural coupling at the temples. Relevant to (a) sensory-substitution "
            "/ vision-aid eyewear claims and (b) eyewear claims that visualize "
            "non-visible-spectrum data (thermal/IR/UV overlay glasses). § 103 motivation "
            "that head-worn EM-spectrum-extending eyewear was an articulated objective by "
            "1987. Non-enabling on the neural interface."
        ),
        sources=[
            "Star Trek: The Next Generation. Paramount Television, 1987.",
            "Sternbach, Rick; Okuda, Michael. Star Trek: The Next Generation Technical Manual. Pocket Books, 1991. ISBN 0-671-70427-3.",
        ],
        cpc_classifications=["G02B 27/01", "A61F 9/08", "G02C 11/00"],
    ),
    E(
        id="they-live-hoffman-lenses",
        canonical_name="They Live 'Hoffman lenses' (information-overlay sunglasses)",
        aliases=["Hoffman lenses", "They Live sunglasses"],
        first_disclosure_date="1988-11-04",
        disclosure_citation="They Live (Universal Pictures), released November 4, 1988; sunglasses whose lenses reveal an otherwise-hidden information layer (true content of signage, currency, media) overlaid on the visual field.",
        creator="John Carpenter / Universal Pictures",
        creator_country="US",
        form_factor="glasses",
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses eyewear that reveals a parallel information layer registered to "
            "objects in the visual field — semantic annotation of the real world through "
            "the lens. The mechanism shown is passive optical, not electronic, so it is a "
            "weak § 102 reference for electronic AR eyewear; its value is § 103 motivation "
            "that 'put on glasses, see annotations on real-world objects' was a stated "
            "objective by 1988, contributing to obviousness of electronic AR-eyewear "
            "annotation claims when combined with enabling display/tracking art."
        ),
        sources=[
            "They Live (film). Universal Pictures, 1988.",
        ],
        cpc_classifications=["G02B 27/01", "G06F 3/01"],
    ),
    E(
        id="snow-crash-gargoyle-rig",
        canonical_name="Snow Crash 'Gargoyle' wearable computer rig",
        aliases=["gargoyle rig", "Snow Crash wearable computer"],
        first_disclosure_date="1992",
        disclosure_citation="Stephenson, Neal. Snow Crash. Bantam Books, 1992 — the 'gargoyles': people wearing head-mounted display goggles, body-worn computers, and continuous-capture sensors, with voice query and head tracking.",
        creator="Neal Stephenson",
        creator_country="US",
        form_factor="glasses",
        form_factor_tags=["goggles", "garment", "body-camera"],
        sensors=["sensor-camera-rgb", "sensor-microphone-air", "sensor-accelerometer"],
        output_modalities=["visual-display", "audio"],
        connectivity="continuous wireless uplink (fictional)",
        prior_art_notes=(
            "Discloses an integrated head-worn AR rig: near-eye display goggles + body-worn "
            "processor + always-on cameras and microphones + head-tracking, with voice "
            "queries against a networked database and continuous capture/upload of the "
            "wearer's surroundings. Relevant to AR-glasses claims combining 'a near-eye "
            "display', 'an outward-facing camera', 'an inertial sensor for head pose', "
            "'a microphone for voice input', and 'continuous data capture/transmission'. "
            "§ 103 motivation that the always-on capture-and-query AR wearable was a "
            "concrete objective by 1992. Non-enabling; pair with enabling HMD/SLAM art."
        ),
        sources=[
            "Stephenson, Neal. Snow Crash. Bantam Books, 1992. ISBN 0-553-08853-X.",
        ],
        cpc_classifications=["G02B 27/01", "G06F 3/01", "G06F 1/163", "H04N 7/18"],
    ),
    E(
        id="rainbows-end-ar-contact-lens",
        canonical_name="Rainbows End AR contact lenses and 'wearing'",
        aliases=["Rainbows End contacts", "Epiphany/Illuminata wearing"],
        first_disclosure_date="2006",
        disclosure_citation="Vinge, Vernor. Rainbows End. Tor Books, 2006 — augmented-reality contact lenses plus clothing-integrated compute ('wearing'), with gaze and gesture control, persistent shared overlays, view-sharing, and a developer ecosystem of competing AR platforms.",
        creator="Vernor Vinge",
        creator_country="US",
        form_factor="contact-lens",
        form_factor_tags=["garment", "glasses"],
        contact_surface="ocular",
        anatomical_target=["cornea"],
        sensors=["sensor-camera-eye", "sensor-camera-rgb"],
        algorithms=["algo-eye-gaze-tracking"],
        output_modalities=["visual-display"],
        connectivity="ubiquitous wireless mesh (fictional)",
        prior_art_notes=(
            "Among the most specific fictional anticipations of modern AR eyewear: "
            "discloses (a) AR contact lenses rendering registered overlays, (b) "
            "clothing-integrated computing and sensing as the host platform, (c) gaze "
            "tracking and subtle gesture as the primary input modality, (d) multi-user "
            "shared/synchronized overlays and view-sharing, and (e) an open developer "
            "ecosystem with competing AR layers. Relevant to AR-contact-lens claims, "
            "gaze-controlled AR claims, and shared/collaborative-AR claims. § 103 "
            "motivation, circa 2006, toward essentially the entire modern AR-eyewear "
            "feature set. Non-enabling on optics and power; pair with enabling "
            "contact-lens-display and low-power-display art."
        ),
        sources=[
            "Vinge, Vernor. Rainbows End. Tor Books, 2006. ISBN 0-312-85684-9.",
        ],
        cpc_classifications=["G02C 7/04", "G02B 27/01", "G06F 3/01", "A61B 3/113"],
    ),
    E(
        id="halting-state-ar-glasses",
        canonical_name="Halting State AR glasses ('CopSpace' and ARG overlays)",
        aliases=["CopSpace glasses", "Halting State specs"],
        first_disclosure_date="2007",
        disclosure_citation="Stross, Charles. Halting State. Ace Books, 2007 — networked AR glasses with role-specific overlay layers (police 'CopSpace'), shared annotations, gaze interaction, and alternate-reality-game overlays as a plot mechanism.",
        creator="Charles Stross",
        creator_country="GB",
        form_factor="glasses",
        sensors=["sensor-camera-rgb", "sensor-camera-eye"],
        algorithms=["algo-eye-gaze-tracking"],
        output_modalities=["visual-display", "audio"],
        connectivity="mobile data network (fictional)",
        lineage_ancestors=["snow-crash-gargoyle-rig", "rainbows-end-ar-contact-lens"],
        prior_art_notes=(
            "Discloses AR glasses with switchable, permission-scoped overlay layers (an "
            "enterprise/role 'channel' model), networked shared annotations registered to "
            "physical locations, gaze-driven UI, and overlapping game/social overlay "
            "layers. Relevant to AR-eyewear claims about layer/channel management, "
            "location-anchored shared annotations, and access-controlled AR content. "
            "§ 103 motivation, circa 2007, that multi-layer permissioned networked AR "
            "eyewear was a concrete objective."
        ),
        sources=[
            "Stross, Charles. Halting State. Ace Books, 2007. ISBN 0-441-01498-4.",
        ],
        cpc_classifications=["G02B 27/01", "G06F 3/01", "H04L 67/131"],
    ),
    E(
        id="predator-bio-mask",
        canonical_name="Predator bio-mask (multi-spectral helmet HUD)",
        aliases=["Yautja bio-mask"],
        first_disclosure_date="1987-06-12",
        disclosure_citation="Predator (20th Century Fox), released June 12, 1987; the creature's helmet/mask providing thermal vision, spectral mode-switching, optical zoom, recording/playback, and audio language capture/synthesis.",
        creator="John McTiernan / 20th Century Fox",
        creator_country="US",
        form_factor="helmet",
        form_factor_tags=["goggles"],
        sensors=["sensor-camera-thermal", "sensor-camera-ir", "sensor-microphone-air"],
        output_modalities=["visual-display", "audio"],
        prior_art_notes=(
            "Discloses a head-worn enclosure integrating switchable multi-spectral imaging "
            "(thermal/IR/visible), digital zoom, on-board recording and playback, and "
            "captured-audio processing/synthesis, with a HUD presenting mode and status. "
            "Relevant to helmet/eyewear claims combining 'a thermal imager', 'a mode "
            "selector among imaging spectra', 'a near-eye display', and 'audio capture and "
            "synthesis'. § 103 motivation that the multi-spectral recording head-display "
            "was an articulated objective by 1987."
        ),
        sources=[
            "Predator (film). 20th Century Fox, 1987.",
        ],
        cpc_classifications=["G02B 27/01", "H04N 5/33", "G06F 3/01"],
    ),
    E(
        id="iron-man-helmet-hud",
        canonical_name="Iron Man helmet HUD with biometric monitoring",
        aliases=["Mark III HUD", "JARVIS helmet display"],
        first_disclosure_date="2008-05-02",
        disclosure_citation="Iron Man (Marvel Studios / Paramount), released May 2, 2008; the suit helmet's interior HUD presenting wearer vitals, environmental/tactical data, and a conversational voice AI (JARVIS). (Armor concept originates Tales of Suspense #39, Marvel Comics, March 1963.)",
        creator="Marvel Studios",
        creator_country="US",
        form_factor="helmet",
        sensors=["sensor-accelerometer"],
        clinical_endpoints=["heart-rate", "respiratory-rate", "blood-oxygen"],
        algorithms=["algo-hr", "algo-respiratory-rate"],
        output_modalities=["visual-display", "audio"],
        prior_art_notes=(
            "Discloses a helmet whose interior near-eye display continuously presents the "
            "wearer's physiological state (HR, respiration, O2, fatigue) alongside "
            "environmental/tactical overlays, mediated by a hands-free conversational voice "
            "assistant. Relevant to helmet- and headgear-integrated biometric-monitoring "
            "claims combining 'sensors disposed to contact the wearer', 'a head-mounted "
            "display presenting physiological metrics', and 'a voice interface'. § 103 "
            "motivation that the vitals-in-the-helmet-HUD concept was an articulated "
            "objective by 2008 (and the broader powered-helmet-display lineage by 1963)."
        ),
        sources=[
            "Iron Man (film). Marvel Studios / Paramount Pictures, 2008.",
            "Lee, Stan; Lieber, Larry; Kirby, Jack; Heck, Don. Tales of Suspense #39. Marvel Comics, 1963.",
        ],
        cpc_classifications=["G02B 27/01", "A61B 5/00", "A42B 3/04", "G06F 3/16"],
    ),
    # ---------------- BODY MEASUREMENT (own cross-cut) ----------------
    E(
        id="star-trek-biobed",
        canonical_name="Star Trek sickbay biobed (wireless physiological telemetry)",
        aliases=["biobed", "diagnostic bed"],
        first_disclosure_date="1966-09-08",
        disclosure_citation="Star Trek (The Original Series), premiered September 8, 1966; the sickbay 'biobed' continuously displaying a patient's vital signs (heart rate, blood pressure, respiration, temperature, brain activity) on an overhead panel without wired connection. Elaborated in Star Trek: The Next Generation (1987).",
        creator="Gene Roddenberry / Desilu Productions",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        clinical_endpoints=["heart-rate", "blood-pressure", "respiratory-rate", "body-temperature", "neural-activity"],
        output_modalities=["visual-display"],
        notes="Form factor is 'other' — the biobed is a fixed instrument, not worn — but it is in scope as continuous, contactless body measurement, which is the corpus's second mandate alongside wearables.",
        prior_art_notes=(
            "Discloses continuous, wireless, multi-parameter physiological telemetry "
            "(HR, BP, respiration, temperature, neural activity) with a real-time "
            "graphical readout, without skin-attached leads. Relevant to non-contact / "
            "contactless vitals-monitoring claims and to wireless-multiparameter-telemetry "
            "claims generally (the modern remote-patient-monitoring and 'hospital bed with "
            "integrated sensors' patent space). § 103 motivation that contactless "
            "continuous multi-vital telemetry was an articulated objective by 1966. "
            "Non-enabling on the sensing modality."
        ),
        sources=[
            "Star Trek (The Original Series). Desilu Productions / Paramount, 1966.",
            "Sternbach, Rick; Okuda, Michael. Star Trek: The Next Generation Technical Manual. Pocket Books, 1991. ISBN 0-671-70427-3.",
        ],
        cpc_classifications=["A61B 5/0205", "A61B 5/00", "A61G 7/05"],
    ),
    E(
        id="minority-report-retinal-id-ads",
        canonical_name="Minority Report ambient retinal identification and personalization",
        aliases=["Minority Report mall scene", "g-speak retinal ads"],
        first_disclosure_date="2002-06-21",
        disclosure_citation="Minority Report (20th Century Fox / DreamWorks), released June 21, 2002; environmental cameras performing continuous retinal/iris identification of passers-by to deliver individually personalized advertising and access control. (Based on Philip K. Dick, 'The Minority Report', Fantastic Universe, 1956.)",
        creator="Steven Spielberg / DreamWorks / 20th Century Fox",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        sensors=["sensor-camera-ir", "sensor-camera-eye"],
        notes="Form factor 'other' — the identification is performed by environmental scanners reading the body, not by a worn device. In scope as contactless body measurement (biometric identification).",
        prior_art_notes=(
            "Discloses continuous, contactless retinal/iris biometric identification of "
            "individuals in a public space, with the identity used to trigger personalized "
            "content and access decisions in real time. Relevant to (a) contactless "
            "ocular-biometric identification claims and (b) identity-triggered "
            "personalization claims. § 103 motivation that always-on ambient retinal ID "
            "with downstream personalization was an articulated objective by 2002. "
            "Non-enabling on the optical pipeline; pair with enabling iris-recognition art."
        ),
        sources=[
            "Minority Report (film). 20th Century Fox / DreamWorks, 2002.",
            "Dick, Philip K. 'The Minority Report'. Fantastic Universe, January 1956.",
        ],
        cpc_classifications=["G06V 40/18", "A61B 3/12", "G06Q 30/02"],
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

    print(f"  fiction round 1: added {added}, skipped {skipped} (already present)")
    print("  next:")
    print("    python3 tools/validate.py corpus.jsonl --strict")
    print("    python3 tools/index.py .")
    print("    python3 tools/cross_cuts.py")


if __name__ == "__main__":
    main()
