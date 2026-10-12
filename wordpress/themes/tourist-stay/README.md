# Tourist Stay: medios y paquetes de demostración

Recursos de Casa Brisa, alojamiento ficticio del tema Tourist Stay. Esta carpeta no es un tema instalable. Incluye 16 fotografías sintéticas WebP en `assets/images/demo/`, logo e icono PNG y sus fuentes SVG en `assets/identity/`, captura principal `screenshot.png` y captura adicional `demo/home-b.png`.

Los medios de trabajo se copian sin modificar desde el tema de `web-templates`. Se pueden subir los WebP y PNG a Medios → Añadir nuevo y sustituirlos por recursos propios; WordPress no admite SVG de forma nativa. No hay dependencias de ejecución ni generación en este repositorio. Las fuentes editables y herramientas de generación permanecen en el tema de origen.

Código e identidad: GPL-2.0-or-later (`LICENSE`). Las fotografías tienen el permiso no exclusivo de `assets/RESOURCES.md`: uso en webs creadas con el tema, incluso comerciales, sin venta o distribución como colección independiente. No representan un alojamiento real. Conserva las condiciones al distribuir los recursos.

## Paquete del asistente 0.1.0

`packages/0.1.0/` conserva los 31 archivos y bytes del paquete histórico antes situado en la raíz. Incluye cuatro manifiestos JSON y WXR (A/B × ES/EN), 18 medios raster, dos capturas, licencias y `SHA256SUMS`. Cada composición crea cinco páginas nativas editables; no incluye reservas, pagos ni inventario.

El asistente instala opcionalmente One Click Demo Import con consentimiento y descarga desde la [Release inmutable](https://github.com/Raposo93/web-templates-demos/releases/tag/tourist-stay-demo-0.1.0), con adjuntos planos. La migración no cambia esas URLs ni el contrato del tema. No se sustituye ningún adjunto publicado ni se crean copias de compatibilidad de la antigua carpeta: los consumidores revisados usan Releases.

El mantenedor genera WXR/JSON desde los patrones con `tools/build-demo.php` del tema, en WordPress desechable para cada idioma y composición; la salida es `dist/demo-release/`. Si se archiva una entrega aquí, su ruta es `wordpress/themes/tourist-stay/packages/<version>/`, sin subdirectorios. Las futuras entregas pueden publicarse sin guardarlas en Git; requieren nueva versión y contrato coherente en el tema.

Desde la raíz ejecuta `python3 tools/check-package.py tourist-stay 0.1.0` o `./check.sh`; dentro de esta carpeta, `sha256sum -c SHA256SUMS`. Las comprobaciones de integridad no acreditan compatibilidad adicional de WordPress/PHP: instalación, edición y visualización se documentan en el tema de origen.
