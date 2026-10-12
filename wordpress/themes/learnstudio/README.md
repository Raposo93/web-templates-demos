# learnstudio: medios de demostración

Recursos de la demo ficticia del tema learnstudio, organizados con las mismas rutas que `web-templates`. No es un tema instalable; los medios de trabajo y el paquete importable de `packages/` se describen por separado.

Incluye 15 fotografías sintéticas WebP en `assets/images/demo/`, identidad PNG/SVG en `assets/identity/`, captura de portada y documentación de procedencia y permisos en `assets/RESOURCES.md`. Las capturas no se importan a Medios. Los SVG son fuentes editables; WordPress no admite su subida de forma nativa.

Para utilizarlos, selecciona los WebP y PNG correspondientes desde Medios → Añadir nuevo en WordPress. Se pueden sustituir por recursos propios. Las demos española e inglesa comparten estos medios. La importación automática de contenidos y sus dependencias se documentan en el repositorio del tema.

Código e identidad: GPL-2.0-or-later (`LICENSE`). Las fotografías tienen el permiso no exclusivo descrito en `assets/RESOURCES.md`; no se permite venderlas como colección independiente. Conserva esa documentación al distribuir los recursos con el tema.

Los derivados se copian sin modificar desde `wordpress/themes/learnstudio/` de `web-templates`, commit `19347eb`. No hay generación en este repositorio: las herramientas y fuentes de generación permanecen en el producto de origen. No se incluyen originales, credenciales, datos de sitios reales ni dependencias de ejecución.

Comprueba integridad desde esta carpeta con `sha256sum -c SHA256SUMS`; desde la raíz, ejecuta `./check.sh`. Esta entrega conserva los formatos originales y no acredita nuevas pruebas de compatibilidad del tema.

## Paquete del asistente 0.1.0

`packages/0.1.0/` contiene los cuatro manifiestos JSON y WXR (A/B × ES/EN), los 17 medios raster, las capturas y licencias del asistente. La Release `learnstudio-demo-0.1.0` entrega estos archivos sin subdirectorios para conservar las URLs del tema. Los recursos de `assets/` permiten inspección manual; el asistente usa la Release inmutable, no las rutas de `main`. No se sustituyen adjuntos publicados.

Antes de publicar, ejecuta `./check.sh` desde la raíz. Crea la Release desde el commit que contiene el paquete comprobado e incluye todos sus archivos, incluido `SHA256SUMS`; verifica después las descargas sin autenticación. La publicación no sustituye las pruebas del asistente en WordPress.
