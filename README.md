# Biblioteca de Estudios Bíblicos

Sitio estático para GitHub Pages. Sin dependencias web, fuentes externas ni proceso de compilación. Las páginas y sus índices funcionan sin JavaScript; el menú móvil y los controles de lectura lo utilizan.

## Vista previa antes de subir

Descomprime la carpeta y abre `index.html` en tu navegador. Puedes navegar a los dos estudios sin conexión. Para servirlo localmente, desde esta carpeta:

```bash
python3 -m http.server 8000
```

Abre http://localhost:8000. El ZIP incluye `vista-previa.html` fuera de la carpeta del sitio: ábrelo para recorrer ambas páginas desde un solo archivo. No subas ese archivo al repositorio.

## Subir desde la interfaz web de GitHub

1. En tu repositorio, crea la rama `test` a partir de `main` y selecciónala.
2. Selecciona **Add file → Upload files**.
3. Arrastra el CONTENIDO de `estudios-biblicos`, incluidos `assets`, `herramientas` y los tres HTML, a la raíz del repositorio. No subas el ZIP ni una carpeta contenedora adicional.
4. Confirma el commit en `test`.
5. Revisa los cambios y crea un pull request de `test` hacia `main` cuando quieras publicarlos.

Una rama `test` no obtiene por sí sola una URL de GitHub Pages. Si Pages publica desde `main`, la versión pública cambiará después del merge. Usa la vista local para revisar antes. Los archivos `apocalipsis.html` y `pablo.html` mantienen sus nombres y los enlaces relativos funcionan bajo la ruta del repositorio.

## Agregar un estudio

1. Duplica `pablo.html` con un nombre sencillo, por ejemplo `romanos.html`.
2. Edita su `<title>`, descripción, encabezado, etiqueta, introducción y contenido dentro de `<article class="article">`. Usa títulos `h2` para secciones y `h3` para subsecciones. Ajusta o elimina el enlace `next-study` del final.
3. Agrega una entrada a `estudios.json`, respetando el formato:

```json
{
  "archivo": "romanos.html",
  "titulo": "Romanos",
  "descripcion": "Estudio de la carta a los Romanos.",
  "etiqueta": "CARTAS · ESTUDIO"
}
```

4. Desde la carpeta del sitio ejecuta:

```bash
python3 herramientas/actualizar_indice.py
```

5. Revisa localmente y sube TODOS los HTML actualizados, la nueva página y `estudios.json` a la rama `test`.

El script actualiza el menú compartido, las tarjetas de inicio y los índices de secciones. El JSON no se carga en el navegador: el HTML generado funciona al abrirlo directamente. Evita renombrar los archivos existentes si deseas conservar sus URLs.

## Diseño y mantenimiento

- Estilos comunes en `assets/estilos.css`; interacciones en `assets/app.js`.
- Paleta propia inspirada en Monokai Pro; no incluye iconos ni código del tema adjunto.
- Lectura normal, grande y muy grande; la preferencia se guarda cuando el navegador lo permite.
- Navegación por teclado, enlace para saltar al contenido y respeto por movimiento reducido.
- Texto y enlaces de estudio conservados. Se corrigió la errata del título de Apocalipsis.
- Los recursos externos de Drive y Spotify mantienen sus enlaces originales; su disponibilidad depende de sus propietarios.

Para revertir, revierte el commit o el pull request en GitHub. Conserva un respaldo de tu repositorio antes de sustituir archivos.
