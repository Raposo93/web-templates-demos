# Recursos de Table & Fork

Código e identidad Patio del Olivo: GPL-2.0-or-later, según `../LICENSE`. El nombre del restaurante es contenido ficticio independiente de la identidad comercial Table & Fork. La marca gráfica se crea con geometría original, sin tipografías ni iconos de terceros; fuente editable en `tools/build-identity.py`, salida SVG y PNG locales.

## Fotografías aportadas

El autor facilitó `originals/table-and-fork/` para implementar el issue #9. Su manifiesto identifica quince imágenes generadas con la herramienta integrada de imágenes. No representan un restaurante, platos, empleados o clientes reales. La colección mantiene mobiliario, iluminación y vajilla recurrentes; las escenas gastronómicas usan referencias del mismo local.

Las imágenes fueron generadas con la herramienta de imágenes de OpenAI para la demo solicitada por el titular del repositorio. No proceden de bancos fotográficos ni de fotografías de terceros incorporadas deliberadamente. Según las condiciones aplicables de OpenAI, el usuario es propietario del resultado generado en la medida permitida por la legislación vigente, sujeto a dichas condiciones y a posibles derechos de terceros. Se documenta su procedencia y se incluyen como recursos de demostración redistribuibles por el titular; no se afirma que las imágenes sean de dominio público, que tengan copyright exclusivo garantizado ni que la licencia GPL del código se extienda automáticamente a ellas. La autorización de uso para los destinatarios se detalla a continuación; antes de distribuir comercialmente debe comprobarse el cumplimiento de las condiciones vigentes del servicio y de posibles derechos de terceros.

## Inventario previo a la selección

Se revisó el manifiesto antes de incorporar los recursos. Se necesitan comedor para la portada, fachada para ubicación, terraza y barra para ambiente, mesa preparada para reservas y una selección coherente de platos para destacados y galería. La carta no necesita fotografía para cada plato. Se usan estas quince escenas, con nombres que conservan la correspondencia con los originales:

| Archivo WebP | Contenido y uso |
| --- | --- |
| 01-hero-restaurant | Comedor principal; hero y galería |
| 02-restaurant-facade | Fachada; contacto y galería |
| 03-outdoor-terrace | Terraza; ambiente y galería |
| 04-dining-room | Comedor desde otro ángulo; restaurante y galería |
| 05-restaurant-bar | Barra y cafetera; restaurante y galería |
| 06-table-setting | Mesa para dos; cierre de reserva y galería |
| 07-tomato-salad | Ensalada; destacado, patrón de plato y galería |
| 08-homemade-croquettes | Croquetas; galería |
| 09-roasted-vegetables | Verduras; galería |
| 10-grilled-sea-bream | Dorada; patrón de plato con foto y galería |
| 11-mushroom-rice | Arroz; destacado y galería |
| 12-roast-chicken | Pollo; galería |
| 13-baked-cheesecake | Tarta de queso; destacado y galería |
| 14-crema-catalana | Crema catalana; galería |
| 15-table-service | Servicio de mesa; restaurante y galería |

Los derivados locales de `images/demo/` se generan una sola vez desde PNG, sin metadatos ni ampliación, con Pillow, calidad 80, método 6 y máximo 1600 × 1200. La portada queda a 1600 × 900; paisajes 1536 × 1024 y platos 1448 × 1086. Tamaño conjunto: aproximadamente 3,1 MiB. Los originales y los WebP ampliados del manifiesto no forman parte del tema.

No hay fuentes, bibliotecas visuales, mapas incrustados ni recursos remotos obligatorios. Los enlaces a mapas y reservas solo abren servicios externos cuando el visitante los pulsa.

## Permisos de uso de las imágenes de demostración

El titular del proyecto autoriza, en la medida de sus derechos, a quienes obtengan este tema a **utilizar, copiar, adaptar y modificar las imágenes de demostración incluidas para crear y mantener sitios web realizados con este tema**, incluidos sitios de clientes y proyectos comerciales. Se permite redistribuirlas como recursos incluidos en el paquete del tema y publicarlas, originales o modificadas, como parte de dichos sitios.

Esta autorización es **no exclusiva**: no transfiere titularidad ni garantiza exclusividad sobre las imágenes o los resultados generados por IA. No autoriza vender o redistribuir las imágenes como un banco de fotografías, colección independiente o producto separado del tema. Está sujeta a la legislación aplicable, a las condiciones del servicio de generación y a posibles derechos de terceros. La GPL del código y la identidad no se extiende a las fotografías. Las escenas son sintéticas y no deben presentarse como fotografías de negocios, productos o personas reales.

## Entrega separada de demos

Las fotografías permanecen en la carpeta fuente para generación y pruebas, pero se excluyen del ZIP instalable. Se entregan en el paquete externo de demo, con estas mismas condiciones de uso. Las capturas A/B son vistas locales de las composiciones existentes. El sustituto visual SVG es geometría original bajo GPL-2.0-or-later; no añade recursos de terceros. La Release externa sigue pendiente; consulta `DEMO-RELEASE.md`.
