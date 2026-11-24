#!/usr/bin/env bash
# verify_release.sh — verify a Free Wearable Corpus release independently
#
# Usage:
#   ./tools/verify_release.sh <version-tag>

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <version-tag>"
  exit 1
fi

VERSION="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
RELEASE_DIR="${REPO_ROOT}/releases/${VERSION}"
TARBALL_NAME="corpus-${VERSION}.tar.gz"
WAI_NAME="corpus-${VERSION}.wai"

if [ ! -d "$RELEASE_DIR" ]; then
  echo "ERROR: $RELEASE_DIR not found."
  exit 1
fi

cd "$RELEASE_DIR"

echo "=== Verifying release ${VERSION} ==="
echo ""

echo "1. SHA-256 verification"
if sha256sum -c SHA256SUMS; then
  echo "   PASS: artifact SHA-256 hashes match SHA256SUMS"
else
  echo "   FAIL: SHA-256 verification failed"
  exit 1
fi
echo ""

echo "1b. WAI1 container, BLAKE3 digests & Ed25519 signatures (offline)"
if [ -f "$WAI_NAME" ] || [ -f "WAI_RECEIPT.json" ]; then
  if python3 "${REPO_ROOT}/tools/emit_wai_commons.py" --verify .; then
    echo "   PASS: WAI1 envelope, BLAKE3SUMS, and Ed25519 receipts verified offline"
  else
    echo "   FAIL: WAI1 / BLAKE3 / Ed25519 verification failed"
    exit 1
  fi
else
  echo "   NOT PRESENT (pre-WAI release)"
fi
echo ""

echo "2. FreeTSA RFC 3161 timestamp"
if [ -f freetsa.tsr ]; then
  if [ ! -f freetsa-cacert.pem ] || [ ! -f freetsa-tsa.crt ]; then
    echo "   SKIPPED (CA chain not downloaded locally)"
  else
    if openssl ts -verify -in freetsa.tsr \
        -data "$TARBALL_NAME" \
        -CAfile freetsa-cacert.pem \
        -untrusted freetsa-tsa.crt 2>/dev/null; then
      TS=$(openssl ts -reply -in freetsa.tsr -text 2>/dev/null | grep "Time stamp:" | head -1)
      echo "   PASS: $TS"
    else
      echo "   FAIL: FreeTSA timestamp does not verify"
      exit 1
    fi
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

echo "3. DigiCert RFC 3161 timestamp"
if [ -f digicert.tsr ]; then
  if [ ! -f digicert-chain.pem ]; then
    echo "   SKIPPED (DigiCert chain not downloaded locally)"
  else
    if openssl ts -verify -in digicert.tsr \
        -data "$TARBALL_NAME" \
        -CAfile digicert-chain.pem 2>/dev/null; then
      TS=$(openssl ts -reply -in digicert.tsr -text 2>/dev/null | grep "Time stamp:" | head -1)
      echo "   PASS: $TS"
    else
      echo "   FAIL: DigiCert timestamp does not verify"
      exit 1
    fi
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

echo "4. OpenTimestamps Bitcoin anchoring"
if [ -f "${TARBALL_NAME}.ots" ]; then
  if command -v ots >/dev/null 2>&1; then
    OUT=$(ots verify "${TARBALL_NAME}.ots" -f "$TARBALL_NAME" 2>&1 || true)
    echo "$OUT" | sed 's/^/   /'
    if [ -f "WAI_RECEIPT.json.ots" ]; then
      OUT_WAI=$(ots verify "WAI_RECEIPT.json.ots" -f "WAI_RECEIPT.json" 2>&1 || true)
      echo "$OUT_WAI" | sed 's/^/   /'
    fi
  else
    echo "   SKIPPED ('ots' not installed)"
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

echo "=== Verification complete ==="
