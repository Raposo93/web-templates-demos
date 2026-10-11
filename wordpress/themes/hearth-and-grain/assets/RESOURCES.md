# Recursos de Hearth & Grain / Nativa Home

Código e identidad geométrica original: GPL-2.0-or-later, según `../LICENSE`. Marca ficticia independiente del nombre del tema. Identidad editable en `tools/build-identity.py`; SVG y PNG locales. Tipografías Georgia y sans serif del sistema, sin archivos ni peticiones de fuentes externas.

## Fotografías

24 imágenes sintéticas aportadas por el autor en `originals/nativa-home/`: cuatro ambientes, dieciséis referencias de producto y cuatro detalles. Se revisó una hoja de contacto antes de incorporarlas. Los pares 05/06, 07/08 y 12/13 son colores del mismo producto; los detalles 21–24 se asocian a las fichas correspondientes. Todos los objetos, medidas, precios y textos son ficticios.

[Manifiesto original aportado](SOURCE-MANIFEST.md), conservado íntegro: su encabezado «Casa Oliva» es una denominación de trabajo de la colección; la marca de la demo es Nativa Home. Cada fotografía tiene procedencia S1 y condiciones U1, con dimensiones y correspondencias documentadas. El manifiesto documenta la procedencia y las condiciones del servicio; los permisos concedidos por el titular a quienes reciben el tema se especifican en la sección «Permisos de uso de las imágenes de demostración». No se les atribuye GPL, CC0 ni dominio público. El ZIP sigue siendo un prototipo para revisión; esta autorización de imágenes no equivale a validar todo el tema para su distribución comercial.

El tema incluye las 24 versiones WebP regeneradas desde los PNG aportados: calidad 88, método 6, recorte centrado mínimo para las proporciones, sin ampliación. Dimensiones: hero 1664 × 936; ambientes 1536 × 1024; productos 1200 × 1200; detalles 1120 × 1400. Peso conjunto aproximado 4 MiB. El script reproducible es `tools/optimize-images.py`; los originales se conservan en la colección de `originals/nativa-home/`, fuera del ZIP y de Git, según la convención del repositorio. La demo importa las imágenes a Medios y usa IDs nativos y tamaños responsivos.

## Bloques y licencias

Las plantillas comerciales parten de las plantillas de bloques de WooCommerce 11.2.0 (`templates/templates/blockified`), adaptadas al tema. WooCommerce: Automattic, GPL-3.0-or-later, https://github.com/woocommerce/woocommerce. La licencia GPL-2.0-or-later del tema permite su distribución conjunta bajo GPLv3 cuando proceda. Se conserva su licencia y los avisos de copyright en `../LICENSE-WOOCOMMERCE`. El complemento no está incluido en el ZIP; debe instalarse por separado. Los bloques de carrito y checkout se generan con `WC_Install::create_pages()`; no se implementa lógica comercial propia.

## Permisos de uso de las imágenes de demostración

El titular del proyecto autoriza, en la medida de sus derechos, a quienes obtengan este tema a **utilizar, copiar, adaptar y modificar las imágenes de demostración incluidas para crear y mantener sitios web realizados con este tema**, incluidos sitios de clientes y proyectos comerciales. Se permite redistribuirlas como recursos incluidos en el paquete del tema y publicarlas, originales o modificadas, como parte de dichos sitios.

Esta autorización es **no exclusiva**: no transfiere titularidad ni garantiza exclusividad sobre las imágenes o los resultados generados por IA. No autoriza vender o redistribuir las imágenes como un banco de fotografías, colección independiente o producto separado del tema. Está sujeta a la legislación aplicable, a las condiciones del servicio de generación y a posibles derechos de terceros. La GPL del código y la identidad no se extiende a las fotografías. Las escenas son sintéticas y no deben presentarse como fotografías de negocios, productos o personas reales.
