# Migración común de demos — issue #1

## Rutas y contratos revisados

El paquete histórico Tourist Stay 0.1.0 pasa de `packages/0.1.0/` a `wordpress/themes/tourist-stay/packages/0.1.0/`. Se conservan sus 31 nombres y bytes, incluido `SHA256SUMS`. El producto incorpora el mismo inventario de trabajo que los otros cuatro: fotografías derivadas, identidad PNG/SVG, condiciones, licencia y capturas. No se añaden originales ni copias de la antigua carpeta.

Las fotografías, identidad raster, capturas A/B y licencias de trabajo coinciden byte a byte con los paquetes de los cuatro temas. La documentación de recursos de Tourist Stay distingue las rutas del tema fuente; el paquete histórico mantiene su documento con las referencias adaptadas al formato plano. Los cinco inventarios de trabajo cubren todos los archivos fuera de `packages/`; cada paquete tiene sus propias sumas completas. Hearth & Grain conserva 24 fotografías, identidad, captura y documentación, sin fabricar WXR/JSON ni exigir un adaptador WooCommerce.

| Referencia | Resultado |
| --- | --- |
| README raíz público | Índice de cinco temas, rutas comunes, distinción trabajo/entrega/Release, comandos y dependencia Python |
| `tools/check-demo-packages.py` | Una resolución por slug/versión para los cuatro contratos; recorre versiones archivadas |
| `tools/check-package.py` | Entrada slug/versión al mismo comprobador, sin excepción de Tourist Stay |
| `tools/check-media.py`, `check.sh` | Inventario de los cinco productos y comprobación conjunta de los cuatro paquetes |
| `.github/workflows/release-demos.yml` público | Ruta de validación y artefacto actualizada; invocación con slug/versión; tag, nombres planos y rechazo a reemplazo conservados |
| Manifiestos JSON y WXR públicos | Sin modificaciones: nombres planos, URLs ficticias y hashes del contrato no dependen de la carpeta del árbol |
| Los cuatro `inc/setup-config.php` en `web-templates` | Se conservan `base`, `version`, `previews`, nombres de medios y capturas: usan Releases y rutas locales del tema |
| Fuentes `wordpress/shared/demo-setup/` y sus copias generadas | Generador: `dist/demo-release/`; importador y pruebas: Releases. No contienen la ruta pública antigua; sin cambios de código que regenerar |
| `.github/workflows/release-tourist-stay-demos.yml` privado | Produce artefacto desde `wordpress/themes/tourist-stay/dist/demo-release/`; no consume el árbol público; conservado |
| `.github/workflows/release-theme.yml` privado | Construye ZIPs en `release-artifacts/`; no consume el paquete público; conservado |
| `tourist-stay/DEMO-RELEASE.md` y README común del asistente | Documentan la ruta migrada, referencias conservadas y contrato para #31 |

La búsqueda en los dos checkouts no encontró consumidores directos de la antigua ruta del árbol fuera de su documentación, comprobador y workflow públicos. No se puede acreditar ausencia de consumidores externos desconocidos. Las URLs de Releases son el contrato público de descarga documentado. Los enlaces históricos fijados a tags o commits siguen resolviendo la ruta antigua en esos árboles, sin mover etiquetas ni reescribir historial. No se mantiene un duplicado en `main` por precaución.

Para [web-templates #31](https://github.com/Raposo93/web-templates/issues/31): la ruta de archivo será `wordpress/themes/<slug>/packages/<version>/` cuando se decida guardar una entrega en Git. La salida del generador seguirá siendo `dist/demo-release/` y los adjuntos públicos seguirán siendo planos en `<slug>-demo-<version>`. No se requiere archivar cada versión futura. Esta migración no implementa la publicación automática ni publica nuevas versiones.

## Validación

- `./check.sh` en ambos repositorios: fuentes comunes, verificadores de los cinco temas, sintaxis PHP y pruebas del lanzamiento en el privado; cuatro paquetes y cinco inventarios en el público.
- `python3 tools/check-package.py tourist-stay 0.1.0` y `python3 tools/check-package.py tradeworks 0.1.0`: resolución genérica aplicada a dos productos.
- Comparación de todos los archivos de los cuatro paquetes contra el commit anterior y contra las descargas públicas: mismos nombres y bytes; Tourist Stay conserva los 31 archivos durante el traslado.
- Descarga HTTPS sin autenticación de las cuatro Releases 0.1.0: 31 archivos Tourist Stay y 30 por cada otro tema, incluyendo `SHA256SUMS` (121 descargas). Cada manifiesto, WXR, medio, captura y licencia coincide con las sumas publicadas y el archivo local.
- Apertura y verificación de los raster de trabajo de los cinco temas con Pillow: formatos válidos y capturas de 1200 × 900. Comparación del contrato cargado por PHP desde los cuatro `setup-config.php`: URL, versión, orden de medios y rutas de capturas coinciden con los paquetes.
- Importación desde ZIP instalable limpio de los cuatro temas, A/B × ES/EN (16 casos), con HTTPS público sin fixtures. Se regeneran y validan los ZIP desde las fuentes actuales; cinco casos que usaron inicialmente archivos históricos se repiten con esos ZIP. Los archivos instalados de los 16 casos coinciden byte a byte con los ZIP regenerados. La suite verifica consentimiento, nonces, medios locales, páginas/navegación, bloques editables e imágenes cargadas sin desbordamiento a 1200/390/320 px. Cada caso usa WordPress y base de datos independientes; servidor y navegador se detienen y el puerto se libera antes del siguiente. Entorno comprobado: WordPress 6.6.10, PHP 8.4.26 y MariaDB 11.8.6.
- `actionlint` sobre los tres workflows revisados: sin errores. La validación y la ruta del artefacto público existen; las entradas/salidas de los workflows privados se conservan. No se ejecutó publicación en GitHub.
- Los tags y metadatos de adjuntos públicos se comparan antes/después; no se ejecutan operaciones de escritura sobre Releases.
- `git diff --check` en ambos repositorios.

Las evidencias locales de descargas e importaciones se conservan en `/home/codex/.cache/demo-paths-validation/`; no son una dependencia del producto ni se incorporan a Git. Los ZIP de prueba se generan desde las fuentes actuales y se comprueban con `check-theme.py --package`; los ZIP históricos versionados se conservan en el commit. Las pruebas no acreditan versiones de WordPress/PHP distintas de las utilizadas ni preparación comercial.

## Coordinación de publicación — web-templates #31

`release-demos.yml` deja de publicar el piloto histórico: valida los archivos archivados usando las rutas `wordpress/themes/<slug>/packages/<version>/`. La publicación canónica se prepara desde el commit etiquetado en el repositorio del tema y usa su adaptador; no necesita nuevas carpetas de paquetes en este repositorio. No se mueven ni reescriben los archivos, tags, hashes o adjuntos históricos. Las URLs planas de las Releases anteriores se conservan. Los nuevos adaptadores cambian versión/base junto al tema, antes de etiquetarlo. El repositorio privado incorpora generación nativa por idioma, publicación en borrador, verificación completa y recuperación sin sustitución de entregas públicas.
