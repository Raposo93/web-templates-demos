# Recursos de LearnStudio

Código e identidad original Aula Horizonte: GPL-2.0-or-later, según `../LICENSE`. La marca separada de LearnStudio utiliza un libro abierto y un horizonte geométricos originales, sin fuentes o iconos de terceros. Fuente: `tools/build-identity.py`; PNG nativos y SVG editable en `identity/`.

## Procedencia y continuidad

Las quince fotografías se generan consecutivamente con la herramienta integrada **imagegen de OpenAI** para el issue #11 el 10 de octubre de 2026. No se utilizan fotografías de terceros ni bancos de imágenes como entrada; las referencias son resultados previos de la misma colección. Las escenas, instalaciones y personas son sintéticas y ficticias. No deben presentarse como fotografías de una academia o docentes reales.

El conjunto mantiene recepción de roble, pared salvia, pavimento claro, aulas con mesas de roble y sillas verdes, luz mediterránea suave y dos docentes con vestuario recurrente. La hoja de continuidad y el conjunto de prompts están en [IMAGE-PROMPTS.md](IMAGE-PROMPTS.md). El inventario completo con nombres, usos, dimensiones originales/derivadas, proporciones, alt ES/EN, referencia a escenas previas y SHA-256 está en [images/manifest.json](images/manifest.json).

Los originales PNG a la resolución devuelta por la herramienta se conservan y entregan aparte en `originals/learnstudio/images/originals/`, según la convención raíz de no incorporarlos a Git. Los WebP del tema se generan una vez desde esos originales: máximo 1600 × 1200, sin ampliación, RGB, sin metadatos, calidad 80 y método 6. El conjunto WebP ocupa 1.809.476 bytes (1,73 MiB). WordPress genera sus miniaturas al importarlos a Medios. No hay tipografías, bibliotecas visuales, mapas incrustados ni recursos remotos obligatorios.

## Condiciones verificadas y permiso no exclusivo

Se consultaron el 10 de octubre de 2026 las secciones «Content» de las [condiciones europeas de uso de OpenAI](https://openai.com/policies/eu-terms-of-use/) y «Customer Content» del [acuerdo de servicios para empresas](https://openai.com/policies/services-agreement/). Ambos atribuyen el resultado al usuario o cliente, entre las partes y en la medida permitida por la ley; también indican que puede no ser único y que el usuario debe respetar posibles derechos de terceros. La modalidad y condiciones de la cuenta que genera los recursos siguen siendo aplicables. Esta documentación no asegura copyright exclusivo ni convierte las imágenes en dominio público.

El titular del proyecto autoriza, en la medida de sus derechos, a quienes obtengan LearnStudio a **utilizar, copiar, adaptar y modificar las imágenes incluidas para crear y mantener sitios web realizados con este tema**, incluidos proyectos comerciales y sitios de clientes. Se permite redistribuirlas como recursos incluidos en el paquete del tema y publicarlas, originales o modificadas, como parte de dichas webs.

El permiso es **no exclusivo** y no transfiere titularidad ni garantiza exclusividad. No autoriza vender o redistribuir las imágenes como banco de fotografías, colección independiente o producto separado del tema. Está sujeto a la legislación aplicable, a las condiciones del servicio utilizado y a derechos de terceros que pudieran existir. La GPL del código y la identidad no se extiende automáticamente a las fotografías. Las imágenes deben seguir identificándose como sintéticas cuando se utilicen como demostración, sin atribuir experiencias o instalaciones reales a personas o negocios.


## Entrega separada de demos

Las fotografías permanecen en la carpeta fuente para generación y pruebas, pero se excluyen del ZIP instalable. Se entregan en el paquete externo de demo, con estas mismas condiciones de uso. Las capturas A/B son vistas locales de las composiciones existentes. El sustituto visual SVG es geometría original bajo GPL-2.0-or-later; no añade recursos de terceros. La Release externa sigue pendiente; consulta `DEMO-RELEASE.md`.
