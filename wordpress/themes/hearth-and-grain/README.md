# hearth-and-grain: medios de demostración

Recursos de la demo ficticia del tema hearth-and-grain, organizados con las mismas rutas que `web-templates`. No es un tema instalable ni un paquete de importación.

Incluye 24 fotografías sintéticas WebP en `assets/images/demo/`, identidad PNG/SVG en `assets/identity/`, captura de portada y documentación de procedencia y permisos en `assets/RESOURCES.md`. Las capturas no se importan a Medios. Los SVG son fuentes editables; WordPress no admite su subida de forma nativa.

Para utilizarlos, selecciona los WebP y PNG correspondientes desde Medios → Añadir nuevo en WordPress. Se pueden sustituir por recursos propios. Las demos española e inglesa comparten estos medios. La importación automática de contenidos y sus dependencias se documentan en el repositorio del tema.

Código e identidad: GPL-2.0-or-later (`LICENSE`). Las fotografías tienen el permiso no exclusivo descrito en `assets/RESOURCES.md`; no se permite venderlas como colección independiente. Conserva esa documentación al distribuir los recursos con el tema.

Los derivados se copian sin modificar desde `wordpress/themes/hearth-and-grain/` de `web-templates`, commit `19347eb`. No hay generación en este repositorio: las herramientas y fuentes de generación permanecen en el producto de origen. No se incluyen originales, credenciales, datos de sitios reales ni dependencias de ejecución.

Comprueba integridad desde esta carpeta con `sha256sum -c SHA256SUMS`; desde la raíz, ejecuta `./check.sh`. Esta entrega conserva los formatos originales y no acredita nuevas pruebas de compatibilidad del tema.

El adaptador de importación WooCommerce sigue pendiente en web-templates #26. Este catálogo conserva solo medios manuales: no incluye `packages/`, manifiestos JSON ni WXR, y los comprobadores de paquetes no exigen ese adaptador.
