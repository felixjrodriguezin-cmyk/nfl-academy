# NFL Academy

Biblioteca de clases HTML interactivas en español. Proyecto independiente y educativo, sin afiliación con la NFL.

## Publicación

GitHub Pages publica exclusivamente la carpeta `docs` de la rama `main`. El archivo de entrada es `docs/index.html`. `.nojekyll` conserva los HTML, CSS y JavaScript tal como se prepararon. No hay servidor, base de datos, analítica ni envío de respuestas.

El repositorio y el sitio son públicos. Nunca añadir conversaciones, respuestas del alumno, notas privadas, credenciales o documentos de otros proyectos.

La portada enumera solo ediciones cuyos archivos existen. La edición del 27 de octubre de 2026 conserva el contenido y el corte de datos de la clase original; su migración web corrige retratos, navegación, adaptación móvil y copia del examen, y excluye el historial personal de puntuaciones. No es una actualización de las noticias a una fecha posterior.

## Añadir una edición futura

1. Preparar y revisar un HTML sin información privada, con nombre `NFL_Academy_YYYY-MM-DD.html`.
2. Guardarlo en `docs/ediciones/` y añadir un registro a `docs/ediciones.json`, siguiendo el formato existente. No reemplazar una edición anterior por una de otra fecha.
3. Ejecutar `python3 scripts/build_index.py` para actualizar la portada. Se rechazan fechas duplicadas y enlaces a archivos inexistentes.
4. Comprobar botones, simuladores, examen correcto e incorrecto, reinicio, copia y alternativa manual, anclas, imágenes y fuentes. Revisar anchos de 320, 390, 768 y 1024 píxeles sin contenido fuera de pantalla. Separar pruebas con tamaño móvil de pruebas reales en iPhone/iPad.
5. Revisar los archivos incluidos en el cambio, confirmar y subir a `main`. GitHub Pages despliega los cambios automáticamente al recibirlos. No se necesita otra tarea programada.
6. Esperar a que Pages termine y abrir la URL pública, incluida la nueva edición. Verificar que devuelve el contenido correcto antes de anunciarla como publicada.

El generador de portada utiliza solo Python estándar, sin instalaciones adicionales. La publicación se puede hacer mediante la interfaz de GitHub o desde una sesión local autorizada con acceso de escritura a este repositorio.

## Integración con la única tarea diaria existente

La tarea actual puede incorporar los pasos anteriores después de crear y validar cada clase, conservando su identidad, horario y destino. Antes de cada publicación, debe verificar que la ejecución dispone de este repositorio y de autorización GitHub vigente. Si el entorno no tiene acceso de escritura, debe entregar el HTML real y señalar que la publicación sigue pendiente; nunca inventar una URL ni afirmar que subió archivos.

Esta preparación no modifica ninguna tarea ni su horario. El acceso GitHub de una sesión interactiva no demuestra acceso de una ejecución futura. No se incluyen contraseñas ni tokens en el repositorio.

## Safari en iPhone/iPad

Abrir la dirección HTTPS del sitio en Safari. Desde Compartir se puede guardar en favoritos o añadir a la pantalla de inicio. Las clases y los retratos externos requieren internet. El examen funciona en el navegador; el botón de copiar ofrece texto seleccionable si se rechaza el portapapeles. Los resultados no se sincronizan automáticamente con ChatGPT ni entre dispositivos.

## Fotografías y fuentes

Los retratos son imágenes directas de ESPN, identificadas mediante su roster público por nombre e identificador. No se alojan copias en este repositorio. Cada ficha permite abrir la fotografía en grande y conserva un respaldo con iniciales si la fuente deja de responder. ESPN y los demás titulares conservan sus derechos sobre fotografías y marcas.

Las fuentes deportivas enlazadas pertenecen a terceros y pueden cambiar o requerir acceso propio. Que una página responda no constituye una auditoría completa de sus cifras ni de la reproducción de vídeos en cada región.
