#!/usr/bin/env python3
"""Verify the complete media inventory and resource documentation."""
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for theme, expected in {
    'tradeworks': 15,
    'table-and-fork': 15,
    'learnstudio': 15,
    'hearth-and-grain': 24,
}.items():
    product = root / 'wordpress/themes' / theme
    listed = set()
    for line in (product / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        path = product / name
        assert path.resolve().is_relative_to(product.resolve()), f'Invalid path: {name}'
        assert name not in listed, f'Duplicate checksum: {name}'
        listed.add(name)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Checksum mismatch: {path}'
    actual = {str(path.relative_to(product)) for path in product.rglob('*')
              if path.is_file() and path.name != 'SHA256SUMS'}
    assert actual == listed, f'Incomplete inventory: {theme}'
    photos = list((product / 'assets/images/demo').glob('*.webp'))
    assert len(photos) == expected, f'Unexpected photograph count: {theme}'
    for path in photos:
        data = path.read_bytes()
        assert data[:4] == b'RIFF' and data[8:12] == b'WEBP', f'Invalid WebP: {path}'
    for name in ['README.md', 'LICENSE', 'assets/RESOURCES.md', 'screenshot.png']:
        assert (product / name).is_file(), f'Missing resource: {theme}/{name}'
    assert len(list((product / 'assets/identity').glob('*.png'))) == 2
    print(f'{theme}: {len(photos)} photographs, identity and {len(listed)} verified files')
print('Demo media verified')
