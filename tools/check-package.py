#!/usr/bin/env python3
"""Verify the external packages before publishing an immutable demo release."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
output = root / 'packages/0.1.0'
for locale in ['es_ES', 'en_US']:
    for demo in ['home-a', 'home-b']:
        manifest = json.loads((output / f'{locale}-{demo}.json').read_text())
        assert manifest['version'] == manifest['theme_version'] == '0.1.0'
        assert manifest['locale'] == locale and manifest['demo'] == demo
        assert len(manifest['pages']) == 5 and len(manifest['media']) == 18
        for resource in [manifest['content'], *manifest['media']]:
            assert re.fullmatch(r'[a-zA-Z0-9_-]+\.(xml|webp|png)', resource['file'])
            assert hashlib.sha256((output / resource['file']).read_bytes()).hexdigest() == resource['sha256']
        xml = (output / manifest['content']['file']).read_text()
        assert '127.0.0.1' not in xml and '/wp-content/themes/' not in xml
        items = ET.fromstring(xml).findall('./channel/item')
        assert len(items) == 5
        assert [item.find('{http://wordpress.org/export/1.2/}post_name').text for item in items] == [page['slug'] for page in manifest['pages']]
        for image in re.findall(r'https://casabrisa.example/media/([^"\s<]+)', xml):
            assert image in {resource['file'] for resource in manifest['media']}
        print(f'{locale} {demo}: five pages, 18 verified localizable media assets')
for name in ['home-a.png', 'home-b.png', 'LICENSE', 'RESOURCES.md']:
    assert (output / name).is_file(), f'Missing release asset: {name}'
print('External demo packages verified')
