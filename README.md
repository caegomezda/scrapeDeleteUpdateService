# Herramienta para la Selección y Eliminación Automatizada de Elementos

## Descripción Breve
Esta herramienta permite seleccionar listas de elementos que desees eliminar de una página o plataforma web y automatiza el proceso de eliminación. Diseñada para usuarios que buscan simplificar tareas repetitivas, es adaptable a múltiples escenarios, utilizando navegación controlada por Selenium y personalización de acciones específicas como validación y confirmación de eliminación.

---

## Idea
La idea surge para resolver la necesidad de automatizar la eliminación de elementos en plataformas o páginas web que manejan grandes volúmenes de contenido, como registros, publicaciones o comentarios. Esta herramienta:

1. Identifica los elementos seleccionados por el usuario.
2. Automatiza el clic en las opciones de eliminación.
3. Maneja confirmaciones o ventanas emergentes asociadas al proceso.
4. Ofrece la flexibilidad de trabajar en entornos dinámicos cargados por JavaScript.

---

## Plan

### Etapa 1: Definición del Alcance
- Analizar las plataformas de destino para entender su estructura DOM.
- Permitir la configuración de selectores CSS/XPath dinámicos para identificar elementos.

### Etapa 2: Implementación de Selección de Elementos
- Desarrollar funciones para resaltar y seleccionar elementos interactivos en la página.
- Guardar las listas de elementos seleccionados en un archivo local para su procesamiento posterior.

### Etapa 3: Automatización del Proceso de Eliminación
- Programar clics automáticos en los botones de eliminación.
- Manejar pop-ups o alertas de confirmación.
- Agregar tiempos de espera para evitar errores en plataformas lentas.

### Etapa 4: Pruebas y Validación
- Probar la herramienta en diferentes navegadores y plataformas.
- Garantizar la estabilidad en entornos dinámicos y cargados por JavaScript.

### Etapa 5: Documentación y Mejora Continua
- Documentar el uso y los ajustes de la herramienta.
- Recopilar retroalimentación para mejoras futuras.

---

## Herramientas Usadas

### Principales
- **Python**: Lenguaje principal del proyecto.
- **Selenium**: Automatización de navegadores web para interacción con páginas dinámicas.
- **tqdm**: Progreso visual durante procesos largos como el scraping o eliminación.
- **JSON**: Almacenamiento de configuraciones y datos extraídos.

### Secundarias
- **Google Chrome / ChromeDriver**: Navegador principal para la automatización.
- **GitHub**: Gestión de versiones y colaboración.
- **Urllib**: Manipulación y validación de URLs relativas y absolutas.

---

## Cómo Contribuir
1. Clona el repositorio.
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcion`.
3. Realiza los cambios y realiza pruebas.
4. Haz un pull request y espera retroalimentación.

---

¡Gracias por contribuir a hacer las tareas repetitivas más simples y eficientes!

