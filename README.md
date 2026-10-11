# Tourist Stay demos

Public, versioned demo data for the Tourist Stay WordPress block theme. This repository contains only demo packages and their release checks; the installable theme is delivered separately.

Version 0.1.0 contains the existing Home A (experience and photography) and Home B (accommodation and amenities) compositions, independently in Spanish and English. Each demo adds five editable native pages and imports 16 synthetic photographs plus the Casa Brisa logo and icon into WordPress Media. No bookings, payments or inventory are included.

Download assets from the `tourist-stay-demo-0.1.0` Release. The theme's consent-based setup uses the JSON manifests, WXR files, photographs and screenshots directly. Do not upload a source archive from this repository as a WordPress theme. The theme verifies the matching package version and each data/image hash before import.

Code, identity and geometric resources: GPL-2.0-or-later. Photograph permissions, origin and restrictions are in `packages/0.1.0/RESOURCES.md` and are included in every Release. These are synthetic illustrations of a fictitious property, not photographs of real accommodation. They may be used on websites created with the theme, including commercial projects, but not sold or distributed as an independent photograph collection.

Release assets are immutable. Corrections require a new version and matching theme contract; old releases remain available for existing buyers. `SHA256SUMS` covers all release resources. Verify with `sha256sum -c SHA256SUMS` in a downloaded asset directory.

Maintainers generate the packages from the theme's existing patterns using its `tools/build-demo.php`, validate all four composition/language combinations, then add the generated output under `packages/<version>/`. Run `python3 tools/check-package.py` before committing. An authorized push of the tag `tourist-stay-demo-0.1.0` runs the release workflow against that exact commit. Ordinary commits do not publish. A retry refuses to replace an existing Release.
