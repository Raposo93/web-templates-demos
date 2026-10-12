#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python3 tools/check-media.py
python3 tools/check-demo-packages.py
git diff --check
