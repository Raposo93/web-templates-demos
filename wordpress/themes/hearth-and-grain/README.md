# Hearth & Grain: medios de demostración

24 fotografías sintéticas de Nativa Home, negocio ficticio, en `assets/images/demo/`; identidad PNG/SVG en `assets/identity/`, captura principal y documentación de recursos. Esta carpeta no contiene un tema instalable.

Este catálogo es la fuente canónica de las fotografías optimizadas. `web-templates` consume un commit fijo y hashes por archivo mediante `demo/media.json` y su herramienta `fetch-demo-media.py`. Los originales y generadores permanecen fuera del catálogo; actualizar fotos requiere revisar permisos, renovar `SHA256SUMS` y actualizar explícitamente el inventario del consumidor. No se cambia un commit fijado ni una Release publicada.

Para uso manual, sube los WebP y PNG a Medios en WordPress y sustituye contenido e identidad de ejemplo. Los SVG son fuentes editables, sin habilitar su subida nativa. No se requieren herramientas para usar las fotos.

No hay paquete importable hasta disponer del adaptador WooCommerce; aquí se conservan medios de trabajo.

Desde esta carpeta: `sha256sum -c SHA256SUMS`. Desde la raíz: `./check.sh`. La comprobación de paquetes descargados se describe en el [README raíz](../../../README.md); los entornos WordPress/PHP comprobados están documentados en el tema de origen.

Código e identidad: [GPL-2.0-or-later](LICENSE). Fotografías: permiso no exclusivo para webs creadas con el tema, incluidos proyectos comerciales, sin venta como colección independiente. Condiciones completas en [assets/RESOURCES.md](assets/RESOURCES.md); consérvalas al distribuir los medios.
