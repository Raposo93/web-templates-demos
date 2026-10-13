#!/usr/bin/env python3
"""Validate versioned native-page demo packages before release publication."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
contracts = {'tourist-stay': (5, 18), 'tradeworks': (6, 17),
             'table-and-fork': (5, 17), 'learnstudio': (11, 17)}


def check_package(slug, version, package):
    assert slug in contracts, f'Unsupported demo contract: {slug}'
    assert re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', version), f'Invalid version: {version}'
    pages, media = contracts[slug]
    records = json.loads((root / 'releases.json').read_text())
    record = next((v for v in records if v['tag'] == f'{slug}-demo-{version}'), None)
    if record:
        assert hashlib.sha256((package / 'SHA256SUMS').read_bytes()).hexdigest() == record['inventory_sha256'], 'Archived release inventory differs'
    checksums = {}
    for line in (package / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert re.fullmatch(r'[A-Za-z0-9_.-]+', name), f'Invalid asset name: {name}'
        assert name not in checksums, f'Duplicate asset: {name}'
        assert hashlib.sha256((package / name).read_bytes()).hexdigest() == digest, name
        checksums[name] = digest
    assert set(checksums) == {path.name for path in package.iterdir() if path.name != 'SHA256SUMS'}
    for locale in ['es_ES', 'en_US']:
        for demo in ['home-a', 'home-b']:
            manifest = json.loads((package / f'{locale}-{demo}.json').read_text())
            assert manifest['version'] == manifest['theme_version'] == version
            assert manifest['locale'] == locale and manifest['demo'] == demo
            assert len(manifest['pages']) == pages and len(manifest['media']) == media
            names = [asset['file'] for asset in manifest['media']]
            assert len(names) == len(set(names))
            for asset in [manifest['content'], *manifest['media']]:
                assert re.fullmatch(r'[A-Za-z0-9_-]+\.(xml|webp|png)', asset['file'])
                assert checksums[asset['file']] == asset['sha256']
                assert (package / asset['file']).stat().st_size <= 1048576
            xml = (package / manifest['content']['file']).read_text()
            for image in re.findall(r'https://[^/]+\.example/media/([^"\s<]+)', xml):
                assert image in names, f'Unlisted WXR media: {image}'
            assert '<!DOCTYPE' not in xml and '<!ENTITY' not in xml
            assert '127.0.0.1' not in xml and '/wp-content/themes/' not in xml
            items = ET.fromstring(xml).findall('./channel/item')
            wp = '{http://wordpress.org/export/1.2/}'
            assert len(items) == pages
            assert [item.find(wp + 'post_name').text for item in items] == [page['slug'] for page in manifest['pages']]
            assert all(item.find(wp + 'post_type').text == 'page' for item in items)
            assert (package / (demo + '.png')).is_file()
    for name in ['LICENSE', 'RESOURCES.md']:
        assert (package / name).is_file()
    print(f'{slug}: four manifests, native WXR pages and {len(checksums)} verified release assets')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug', choices=contracts)
    parser.add_argument('version')
    parser.add_argument('directory', type=Path, help='Downloaded or generated assets outside the tracked tree')
    args = parser.parse_args()
    check_package(args.slug, args.version, args.directory)
