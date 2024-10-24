# Scrum Management App

Esta es una aplicación de gestión de proyectos SCRUM, que permite la administración de tareas, sprints y épicas. Diseñada para facilitar la planificación y el seguimiento de proyectos utilizando la metodología SCRUM.

## Contenido

- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)

  
## Tecnologías Utilizadas

- [Django](https://www.djangoproject.com/) - Framework web.
- [SQLite](https://www.sqlite.org/index.html) - Base de datos ligera utilizada para el desarrollo.

## Instalación

1. **Clona el repositorio:**


   git clone [https://github.com/tu_usuario/Sprint.git](https://github.com/NikkyChin/Scrum-manager)


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


8. **Ejecuta el shell para consultas:**


   python manage.py shell
  

- **Página de Inicio**: Muestra un panel de control con enlaces a las secciones de tareas, sprints y épicas.
- **Tareas**: Puedes ver, agregar, editar y eliminar tareas.
- **Sprints**: Puedes ver los sprints disponibles y sus detalles.
- **Épicas**: Puedes ver las épicas y sus descripciones.

