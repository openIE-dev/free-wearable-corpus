#!/usr/bin/env python3
"""new_entry.py — interactive scaffolder for new corpus entries.

Walks a contributor through the schema fields, applies sensible defaults,
and writes the new entry to a fresh JSONL file ready to be reviewed and
appended to corpus.jsonl via a PR.

Usage:
    python3 tools/new_entry.py             # interactive
    python3 tools/new_entry.py --append    # append to corpus.jsonl directly
    python3 tools/new_entry.py --tier 2    # reference-only entry (no prior_art_notes required)
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

CORPUS_OPTIONS = ["private", "open", "fictional", "academic", "regulatory", "standards"]
IP_STATUS_OPTIONS = [
    "patented", "open-permissive", "open-copyleft", "public-domain",
    "fictional", "regulatory-filing", "standards", "trade-secret", "unknown",
]
FORM_FACTORS = [
    "watch", "bracelet", "ring", "glasses", "goggles", "contact-lens",
    "earbud", "over-ear-headphone", "hearing-aid", "headband", "cap",
    "helmet", "patch", "garment", "belt", "pendant", "armband", "legband",
    "sock", "insole", "shoe", "body-camera", "exoskeleton", "implantable",
    "ingestible", "dental", "tattoo-electronic", "fictional-other", "other",
]


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-")


def existing_ids():
    p = ROOT / "corpus.jsonl"
    if not p.exists() or p.stat().st_size == 0:
        return set()
    return {json.loads(l)["id"] for l in p.read_text().splitlines() if l.strip()}


def known_tags(field):
    p = ROOT / "corpus.jsonl"
    if not p.exists() or p.stat().st_size == 0:
        return []
    counts = {}
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        for t in e.get(field) or []:
            counts[t] = counts.get(t, 0) + 1
    return [t for t, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]


def ask(prompt, default=None, required=False, options=None, multi=False, hint=None):
    label = prompt
    if options:
        label += f"\n  options: {', '.join(options)}"
    if hint:
        label += f"\n  ({hint})"
    label += f"\n  [default: {default}] " if default is not None else "\n> "
    while True:
        try:
            v = input(label).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.", file=sys.stderr)
            sys.exit(1)
        if not v and default is not None:
            v = default
        if not v:
            if required:
                print("  required.")
                continue
            return None
        if multi:
            return [x.strip() for x in v.split(",") if x.strip()]
        return v


def ask_yes_no(prompt, default=False):
    suffix = " [Y/n] " if default else " [y/N] "
    while True:
        try:
            v = input(prompt + suffix).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.", file=sys.stderr)
            sys.exit(1)
        if not v:
            return default
        if v in ("y", "yes"):
            return True
        if v in ("n", "no"):
            return False


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--append", action="store_true", help="append directly to corpus.jsonl")
    p.add_argument("--draft", action="store_true", help="mark draft: true")
    p.add_argument("--tier", type=int, default=1, choices=(1, 2),
                   help="entry tier (1 = full commons-grade, 2 = reference-only)")
    args = p.parse_args()

    print("=" * 60)
    print("  Free Wearable Corpus — new entry scaffolder")
    print("=" * 60)
    print()
    print(f"Walking schema v0.1, Tier {args.tier}.")
    print("Press enter to leave a non-required field blank.")
    print()
    if args.tier == 1:
        print("Tier 1 quality bar:")
        print("  - disclosure_citation resolves to a primary source")
        print("  - first_disclosure_date defensible against challenge")
        print("  - prior_art_notes is element-by-element 102/103 analysis")
        print("  - sources non-empty and primary")
        print("  - at least one of {form_factor, sensors, algorithms} tagged")
    else:
        print("Tier 2 (reference-only) bar:")
        print("  - disclosure_citation resolves to a primary source")
        print("  - first_disclosure_date defensible")
        print("  - sources non-empty")
        print("  - prior_art_notes NOT required (Tier 2 populates the long tail)")
    print()
    input("Press enter to begin… ")
    print()

    entry = {"schema_version": 1, "tier": args.tier}

    # ---- identity ----
    entry["canonical_name"] = ask("Canonical name", required=True,
                                  hint="e.g. 'Fitbit Charge', 'OpenBCI Cyton', 'Dick Tracy Wrist Radio'")
    suggested_id = slugify(entry["canonical_name"])
    seen = existing_ids()
    while True:
        eid = ask("ID (kebab-case slug)", default=suggested_id, required=True)
        if eid in seen:
            print(f"  '{eid}' already exists — pick another.")
            suggested_id = eid + "-2"
            continue
        if not re.match(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$", eid):
            print("  ids must be lowercase, alphanumeric + hyphens, no leading/trailing hyphen.")
            continue
        entry["id"] = eid
        break

    aliases = ask("Aliases (comma-separated)", multi=True)
    if aliases:
        entry["aliases"] = aliases

    entry["corpus"] = ask("Corpus", required=True, options=CORPUS_OPTIONS)
    while entry["corpus"] not in CORPUS_OPTIONS:
        entry["corpus"] = ask(f"Must be one of {CORPUS_OPTIONS}", required=True)

    # ---- disclosure ----
    print()
    print("--- Disclosure ---")
    entry["first_disclosure_date"] = ask(
        "First disclosure date (YYYY, YYYY-MM, or YYYY-MM-DD)", required=True,
        hint="earliest verifiable public disclosure"
    )
    entry["disclosure_citation"] = ask(
        "Disclosure citation", required=True,
        hint="DOI, ISBN, URL, patent #, 510(k) #, episode ID, standards doc #"
    )
    entry["creator"] = ask("Creator (person/org/studio/author/agency)", required=True)
    cc = ask("Creator country (ISO-alpha-2)", hint="optional")
    if cc:
        entry["creator_country"] = cc

    # ---- form factor / contact ----
    print()
    print("--- Form factor & body contact ---")
    entry["form_factor"] = ask("Primary form factor", options=FORM_FACTORS,
                               required=True, default="watch")
    while entry["form_factor"] not in FORM_FACTORS:
        entry["form_factor"] = ask(f"Must be one of {FORM_FACTORS}", required=True)
    extra_ff = ask("Additional form-factor tags (comma-separated)", multi=True,
                   hint="multi-form devices, e.g. watch+strap or glasses+earbud combo")
    if extra_ff:
        entry["form_factor_tags"] = extra_ff
    contact = ask("Contact surface",
                  hint="skin | scalp | ear | nasal | dental | ocular | vascular | sub-dermal | textile-mediated | non-contact")
    if contact:
        entry["contact_surface"] = contact
    target = ask("Anatomical target regions (comma-separated)", multi=True,
                 hint="wrist, temporal-lobe, finger, chest, scalp-Fpz, etc.")
    if target:
        entry["anatomical_target"] = target

    # ---- sensors ----
    print()
    print("--- Sensors ---")
    print("Tags currently in use (top 15):")
    for t in known_tags("sensors")[:15]:
        print(f"  {t}")
    print("See SCHEMA.md for the full sensor taxonomy.")
    sensors = ask("Sensors (comma-separated tags)", multi=True)
    if sensors:
        entry["sensors"] = sensors
    sd = ask("Sensor details (free text)",
             hint="wavelengths, electrode geometry, sampling rate, channel count")
    if sd:
        entry["sensor_details"] = sd

    # ---- actuators / outputs ----
    print()
    print("--- Actuators / outputs ---")
    actuators = ask("Actuators (comma-separated)", multi=True,
                    hint="haptic-eccentric, haptic-piezo, electrical-stim-tens, optical-stim, audio, display, drug-delivery")
    if actuators:
        entry["actuators"] = actuators
    outputs = ask("Output modalities (comma-separated)", multi=True,
                  hint="haptic | visual-display | audio | electrical-stim | thermal | drug-delivery | data-only")
    if outputs:
        entry["output_modalities"] = outputs

    # ---- compute / connectivity / power ----
    print()
    print("--- Compute / power ---")
    compute = ask("Compute", hint="MCU, accelerator, edge-vs-cloud split")
    if compute:
        entry["compute"] = compute
    conn = ask("Connectivity", hint="ble | wifi | nfc | lte-m | thread | wired | sneakernet | none")
    if conn:
        entry["connectivity"] = conn
    power = ask("Power source", hint="cr2032 | li-ion-rechargeable | nfc-harvested | piezoharvest | tethered | fictional")
    if power:
        entry["power_source"] = power
    runtime = ask("Runtime", hint="hours or days, free text")
    if runtime:
        entry["runtime"] = runtime

    # ---- algorithms / clinical ----
    print()
    print("--- Algorithms / clinical endpoints ---")
    print("Algorithm tags currently in use (top 15):")
    for t in known_tags("algorithms")[:15]:
        print(f"  {t}")
    algorithms = ask("Algorithms (comma-separated)", multi=True)
    if algorithms:
        entry["algorithms"] = algorithms
    endpoints = ask("Clinical endpoints (comma-separated)", multi=True,
                    hint="spo2, glucose, blood-pressure, eeg-bandpower, etc.")
    if endpoints:
        entry["clinical_endpoints"] = endpoints

    # ---- IP ----
    print()
    print("--- Intellectual property ---")
    entry["ip_status"] = ask("IP status", options=IP_STATUS_OPTIONS,
                             required=True, default="unknown")
    while entry["ip_status"] not in IP_STATUS_OPTIONS:
        entry["ip_status"] = ask(f"Must be one of {IP_STATUS_OPTIONS}", required=True)
    if entry["ip_status"] == "patented":
        cites = ask("Patent numbers (comma-separated)", multi=True,
                    hint="e.g. US10737394B2, WO2021123456A1")
        if cites:
            entry["ip_citations"] = cites
    elif entry["ip_status"] == "regulatory-filing":
        cites = ask("Regulatory filing numbers (comma-separated)", multi=True,
                    hint="510(k) numbers, De Novo, PMA, CE technical file")
        if cites:
            entry["ip_citations"] = cites
    elif entry["ip_status"] == "standards":
        cites = ask("Standards doc identifiers (comma-separated)", multi=True,
                    hint="IEEE 11073-10406, Bluetooth SIG HRP, ISO/IEC 80601-2-61")
        if cites:
            entry["ip_citations"] = cites

    # ---- regulatory ----
    print()
    print("--- Regulatory pathway (optional) ---")
    pathway = ask("Regulatory pathway",
                  hint="fda-510k | fda-de-novo | fda-pma | ce-mdr | ce-ivdr | exempt | none | fictional")
    if pathway:
        entry["regulatory_pathway"] = pathway
    preds = ask("Regulatory predicates (comma-separated entry ids or filing numbers)", multi=True)
    if preds:
        entry["regulatory_predicates"] = preds
    trials = ask("Clinical trial IDs (comma-separated, NCT/ISRCTN)", multi=True)
    if trials:
        entry["clinical_trials"] = trials

    # ---- prior art notes ----
    if args.tier == 1:
        print()
        print("--- Prior art notes ---")
        print("The heart of the entry. Element-by-element 102/103 analysis.")
        print("Identify form factor + sensor + algorithm components disclosed,")
        print("and what claim phrases each could anticipate. Be specific.")
        notes = ask("Prior art notes", hint="multi-sentence")
        if notes:
            entry["prior_art_notes"] = notes

    # ---- lineage ----
    print()
    print("--- Lineage (optional) ---")
    anc = ask("Lineage ancestors (comma-separated entry ids)", multi=True)
    des = ask("Lineage descendants (comma-separated entry ids)", multi=True)
    if anc:
        entry["lineage_ancestors"] = anc
    if des:
        entry["lineage_descendants"] = des

    # ---- sources ----
    print()
    print("--- Sources ---")
    sources = ask("Source citations (comma-separated)", multi=True, required=True,
                  hint="primary references; DOIs, ISBNs, filing numbers, episode IDs")
    entry["sources"] = sources or []

    cpc = ask("CPC classifications (comma-separated)", multi=True,
              hint="A61B 5/02416 for PPG, A61B 5/24 for EEG, G04G 21/* for smartwatch")
    if cpc:
        entry["cpc_classifications"] = cpc

    # ---- notes / draft ----
    print()
    notes = ask("Free-form notes")
    if notes:
        entry["notes"] = notes

    # Quality bar check
    quality_blockers = []
    if args.tier == 1 and not entry.get("prior_art_notes"):
        quality_blockers.append("prior_art_notes empty (Tier 1)")
    if not entry.get("disclosure_citation"):
        quality_blockers.append("disclosure_citation empty")
    if not entry.get("sources"):
        quality_blockers.append("sources empty")

    if args.draft or quality_blockers:
        entry["draft"] = True
        if quality_blockers:
            print()
            print("Quality bar not yet met:")
            for q in quality_blockers:
                print(f"  - {q}")
            print("Marking draft: true.")

    entry["last_updated"] = ask("Last updated (YYYY-MM-DD)",
        default=__import__("datetime").date.today().isoformat())

    # ---- preview ----
    print()
    print("=" * 60)
    print("  Preview")
    print("=" * 60)
    print(json.dumps(entry, indent=2, ensure_ascii=False))
    print()

    if args.append:
        if not ask_yes_no("Append to corpus.jsonl?", default=False):
            print("Aborted before append.")
            return
        with (ROOT / "corpus.jsonl").open("a") as f:
            f.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"  Appended to corpus.jsonl. Now run:")
        print(f"    python3 tools/validate.py corpus.jsonl --strict")
        print(f"    python3 tools/index.py .")
        print(f"    python3 tools/cross_cuts.py")
    else:
        out = ROOT / f"entry-{entry['id']}.jsonl"
        out.write_text(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"  Wrote {out}")
        print()
        print("Review, edit if needed, then merge into corpus.jsonl:")
        print(f"  cat entry-{entry['id']}.jsonl >> corpus.jsonl")
        print(f"  python3 tools/validate.py corpus.jsonl --strict")
        print(f"  python3 tools/index.py .")
        print(f"  python3 tools/cross_cuts.py")


if __name__ == "__main__":
    main()
