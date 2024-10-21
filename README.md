# Scrum Management App

Esta es una aplicación de gestión de proyectos SCRUM, que permite la administración de tareas, sprints y épicas. Diseñada para facilitar la planificación y el seguimiento de proyectos utilizando la metodología SCRUM.

## Contenido

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características

- Gestión de usuarios (responsables, Scrum Masters y miembros del equipo).
- Creación y seguimiento de tareas distribuidas en diferentes sprints y épicas.
- Visualización de tareas, sprints y épicas en listas.
- Sistema de autenticación básico (sin autenticación de usuarios por el momento).
  
## Tecnologías Utilizadas

- [Django](https://www.djangoproject.com/) - Framework web.
- [SQLite](https://www.sqlite.org/index.html) - Base de datos ligera utilizada para el desarrollo.
- [HTML/CSS](https://developer.mozilla.org/es/docs/Web) - Para el diseño y estilo de la interfaz de usuario.

## Instalación

1. **Clona el repositorio:**


   git clone https://github.com/tu_usuario/Sprint.git


2. **Navega al directorio del proyecto:**


   cd Sprint


3. **Crea un entorno virtual:**


   python -m venv env


4. **Activa el entorno virtual:**

   - En Windows:
  
     .\env\Scripts\activate


   - En macOS/Linux:

     source env/bin/activate


5. **Instala las dependencias:**

 
   pip install -r requirements.txt


6. **Aplica las migraciones:**


   python manage.py migrate


7. **Crea datos de prueba (opcional):**

   Puedes crear un conjunto de datos de prueba ejecutando el siguiente comando:


   python manage.py loaddata fixtures/datos_prueba.json


8. **Ejecuta el servidor de desarrollo:**


   python manage.py runserver
  

9. **Accede a la aplicación:**

   Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Uso

- **Página de Inicio**: Muestra un panel de control con enlaces a las secciones de tareas, sprints y épicas.
- **Tareas**: Puedes ver, agregar, editar y eliminar tareas.
- **Sprints**: Puedes ver los sprints disponibles y sus detalles.
- **Épicas**: Puedes ver las épicas y sus descripciones.

