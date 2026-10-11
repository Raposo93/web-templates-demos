#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python3 tools/check-package.py
python3 tools/check-media.py
git diff --check
