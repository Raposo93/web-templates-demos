#!/usr/bin/env python3
"""Validate one theme/version package using the shared demo contract checks."""
import argparse
import runpy
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('slug', help='Theme slug, for example tourist-stay')
parser.add_argument('version', help='Package version, for example 0.1.0')
args = parser.parse_args()
checker = runpy.run_path(str(Path(__file__).with_name('check-demo-packages.py')))
checker['check_package'](args.slug, args.version)
