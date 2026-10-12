# web-templates-demos

Datos y medios públicos de demostración de cinco temas independientes de `web-templates`. Este repositorio no contiene temas instalables; sus ZIP se entregan por separado.

| Producto | Medios de trabajo | Paquete del asistente | Documentación |
| --- | --- | --- | --- |
| Tourist Stay / Casa Brisa | 16 WebP e identidad | A/B × ES/EN, 0.1.0 | [README](wordpress/themes/tourist-stay/README.md) |
| TradeWorks / Nexo Instalaciones | 15 WebP e identidad | A/B × ES/EN, 0.1.0 | [README](wordpress/themes/tradeworks/README.md) |
| Table & Fork / Patio del Olivo | 15 WebP e identidad | A/B × ES/EN, 0.1.0 | [README](wordpress/themes/table-and-fork/README.md) |
| LearnStudio / Aula Horizonte | 15 WebP e identidad | A/B × ES/EN, 0.1.0 | [README](wordpress/themes/learnstudio/README.md) |
| Hearth & Grain / Nativa Home | 24 WebP e identidad | Pendiente: adaptador WooCommerce | [README](wordpress/themes/hearth-and-grain/README.md) |

## Organización común

Todas las rutas se resuelven desde `wordpress/themes/<slug>/`:

| Contenido | Ruta dentro del producto |
| --- | --- |
| Documentación e inventario de trabajo | `README.md`, `SHA256SUMS` |
| Fotografías de trabajo | `assets/images/demo/` |
| Identidad y fuentes vectoriales | `assets/identity/` |
| Condiciones y licencia | `assets/RESOURCES.md`, `LICENSE` |
| Captura principal y adicionales | `screenshot.png`, `demo/` |
| Entrega completa archivada | `packages/<version>/` |

Los medios de trabajo permiten inspección y subida manual a WordPress. Cada paquete versionado es una entrega completa y plana: imágenes, identidad raster, capturas, manifiestos JSON, WXR, licencias y `SHA256SUMS`. Los nombres `es_ES-home-a.json`, etc., distinguen idioma y composición; no se añaden subcarpetas. Hearth & Grain conserva solo medios y no tiene paquete importable hasta disponer de su adaptador WooCommerce.

El asistente descarga **adjuntos de GitHub Releases**, desde `https://github.com/Raposo93/web-templates-demos/releases/download/<slug>-demo-<version>/<archivo>`, nunca desde el árbol de Git. Mover las carpetas no cambia esas URLs. Las cuatro Releases 0.1.0, sus tags y sus bytes se conservan; las correcciones requieren una nueva versión y contrato coherente del tema. No subas el ZIP de fuentes de este repositorio como tema.

## Generación y validación

Las herramientas y fuentes editables permanecen en cada tema de `web-templates`. Su generador `tools/build-demo.php` exporta los patrones registrados en WordPress desechable con el idioma correcto; `dist/demo-release/` es la salida del generador. Se validan A/B × ES/EN antes de entregar el paquete completo. Si se archiva en este repositorio, se usa `wordpress/themes/<slug>/packages/<version>/`. La automatización prevista en [web-templates #31](https://github.com/Raposo93/web-templates/issues/31) debe publicar los mismos adjuntos planos y no requiere guardar cada futura entrega en Git.

```sh
./check.sh
python3 tools/check-package.py tourist-stay 0.1.0
python3 tools/check-package.py tradeworks 0.1.0
python3 tools/check-demo-packages.py
python3 tools/check-media.py
# In a downloaded release asset directory:
sha256sum -c SHA256SUMS
```

Python 3.9+ y Git se necesitan solo para las comprobaciones de desarrollo. `check-demo-packages.py` recorre las versiones archivadas de los cuatro contratos existentes; `check-package.py` valida una pareja slug/versión con las mismas comprobaciones. `check-media.py` verifica el inventario separado de los cinco productos. No se necesitan herramientas de ejecución para usar las imágenes. Integridad de archivos no acredita compatibilidad adicional del tema: instalación, edición y visualización de WordPress/PHP se documentan en el producto de origen.

El workflow `release-demos.yml` mantiene su alcance histórico: un tag autorizado `tourist-stay-demo-0.1.0` prepara y publica ese paquete desde su commit exacto y rechaza sustituir una Release existente. Los commits normales no publican. La publicación general de versiones futuras corresponde a #31.

Código e identidad: GPL-2.0-or-later. Los permisos no exclusivos de las fotografías sintéticas se documentan por producto y se incluyen en los paquetes: uso en webs creadas con el tema, incluidos proyectos comerciales, sin venta como colección independiente. Son negocios ficticios; no se incluyen originales de alta resolución ni datos reales.

La revisión de consumidores, workflows y compatibilidad de rutas se registra en [MIGRATION.md](MIGRATION.md).
