# web-templates-demos

Fuente canónica pública de fotografías optimizadas y medios de cinco temas independientes. Los temas instalables y sus generadores viven en `web-templates`; sus ZIP se entregan por separado.

| Producto | Fotos | Documentación |
| --- | ---: | --- |
| Tourist Stay / Casa Brisa | 16 | [README](wordpress/themes/tourist-stay/README.md) |
| TradeWorks / Nexo Instalaciones | 15 | [README](wordpress/themes/tradeworks/README.md) |
| Table & Fork / Patio del Olivo | 15 | [README](wordpress/themes/table-and-fork/README.md) |
| LearnStudio / Aula Horizonte | 15 | [README](wordpress/themes/learnstudio/README.md) |
| Hearth & Grain / Nativa Home | 24 | [README](wordpress/themes/hearth-and-grain/README.md) |

Cada producto conserva `assets/images/demo/`, identidad, capturas de entrega, licencia, condiciones de recursos y `SHA256SUMS`. El consumidor privado fija un commit completo y SHA-256 por fotografía, restaura las mismas rutas locales y no necesita autenticación. No consume `main` dinámicamente.

## Entregas

Los asistentes descargan adjuntos de [GitHub Releases](https://github.com/Raposo93/web-templates-demos/releases) desde `releases/download/<slug>-demo-<version>/<archivo>`. No usan el árbol Git. Las carpetas `packages/<version>/` se retiraron tras comprobar por descarga anónima los seis paquetes completos y su igualdad byte a byte. [releases.json](releases.json) es el registro histórico de esos seis paquetes retirados del árbol: conserva sus URLs y hashes de inventario. No es un índice completo de Releases ni se actualiza con cada publicación; el listado completo y vigente está en GitHub Releases. Releases, tags y URLs siguen intactos; los archivos también se recuperan desde Git anterior a la limpieza.

Nuevos paquetes se generan desde el tema etiquetado, se validan y publican mediante `web-templates/tools/release-demo.py` antes de distribuir el ZIP. No se archivan en Git. Hearth & Grain necesita un adaptador WooCommerce antes de ofrecer paquetes importables.

## Desarrollo y comprobaciones

Python 3.9+ y Git solo para mantenimiento:

```sh
./check.sh
# Download a complete release into an ignored directory, then verify it:
gh release download tourist-stay-demo-0.1.0 --repo Raposo93/web-templates-demos \
  --dir release-artifacts/tourist-stay-demo-0.1.0
python3 tools/check-demo-packages.py tourist-stay 0.1.0 \
  release-artifacts/tourist-stay-demo-0.1.0
```

`check.sh` verifica los inventarios completos de medios sin red. El verificador de paquetes exige inventario exacto, hashes, cuatro contratos JSON/WXR, páginas y medios raster; también contrasta el hash histórico de `releases.json` cuando existe. GitHub CLI solo se necesita para el ejemplo de descarga; los adjuntos públicos pueden descargarse anónimamente por HTTPS.

El workflow `release-demos.yml` comprueba medios en commits/PR y manualmente, con `contents: read`; no publica ni responde a tags. Los procedimientos de generación/publicación están en [PUBLISHING.md del repositorio de temas](https://github.com/Raposo93/web-templates/blob/main/PUBLISHING.md). No se duplica el publicador ni se certifica compatibilidad WordPress por comprobar hashes.

Código e identidad: GPL-2.0-or-later. Fotografías sintéticas: permisos no exclusivos documentados por producto, para webs realizadas con el tema, incluso comerciales, sin venta como colección independiente. No hay datos de negocios reales ni originales de alta resolución.
