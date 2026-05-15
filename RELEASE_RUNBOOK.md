---
title: Release runbook
layout: default
nav_order: 8
---

# Release Runbook

Step-by-step procedure for cutting a quarterly release.

## Step 1: Verify the corpus is releasable

```bash
python3 tools/validate.py corpus.jsonl --strict
python3 tools/index.py .
python3 tools/cross_cuts.py
```

Address any errors or quality failures. Commit regenerated derived
artifacts.

## Step 2: Install OpenTimestamps client (one-time)

```bash
pip install opentimestamps-client
# or
pipx install opentimestamps-client
```

Confirm: `ots --version`.

## Step 3: Run the release ceremony

```bash
./release.sh 2026.Q3
```

The script will:

1. Validate the corpus passes strict mode
2. Regenerate derived artifacts
3. Build a deterministic tarball (same content + same version tag =
   same SHA-256)
4. Submit the hash to FreeTSA (RFC 3161, free)
5. Submit the hash to DigiCert (RFC 3161, free)
6. Submit to OpenTimestamps (Bitcoin anchoring, free)
7. Write `MANIFEST.md` documenting the release
8. Commit the release directory and tag the commit `2026.Q3`

If FreeTSA or DigiCert is temporarily down, the script warns and
continues — as long as at least one RFC 3161 layer succeeds plus
OpenTimestamps, the release is valid.

## Step 4: Push the release

```bash
git push origin main
git push origin 2026.Q3
```

## Step 5: Upgrade the OpenTimestamps proof (in ~6 hours)

```bash
ots upgrade releases/2026.Q3/corpus-2026.Q3.tar.gz.ots
git add releases/2026.Q3/corpus-2026.Q3.tar.gz.ots
git commit -m "release: upgrade 2026.Q3 OpenTimestamps proof"
git push
```

This is when the Bitcoin-anchored proof becomes verifiable.

## Step 6: Discoverability submissions

After the release tag is pushed and the OTS proof upgraded, the corpus
exists publicly with cryptographic proof of pre-existence. The remaining
work is making sure consumers actually find it.

### Zenodo DOI

Fastest path to a citable DOI:

1. https://zenodo.org/account/settings/github/
2. Sign in with GitHub
3. Find `openie-dev/free-wearable-corpus` and toggle it on
4. Trigger a Zenodo deposit by creating a GitHub release pointing at the
   `2026.Q3` tag
5. Zenodo automatically mints a DOI and archives the release tarball

Once the DOI is assigned, add it to README and MANIFEST.md.

### Wayback Machine

```
https://web.archive.org/save/https://github.com/openie-dev/free-wearable-corpus
https://web.archive.org/save/https://github.com/openie-dev/free-wearable-corpus/releases/tag/2026.Q3
```

### Google Patents NPL / Google Scholar

Add the repo URL to openie.dev with descriptive anchor text. Submit the
URL to Google Search Console.

## Quarterly cadence

- 2026.Q3 in early July 2026
- 2026.Q4 in early October 2026
- 2027.Q1 in early January 2027

## If something goes wrong

The release script is idempotent within a version. If a step fails, fix
the underlying issue and re-run — the deterministic tarball means the
hash stays stable.

Once a git tag is pushed to the public remote, do not delete and re-tag.
If something needs fixing after the tag is pushed, cut a new tag
(`2026.Q3.1`) or move on to the next quarter.
