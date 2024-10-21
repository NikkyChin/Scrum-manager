from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # Ruta principal de la aplicación 'scrum'
    path('tareas/', views.tareas, name='tareas'),        # Lista de todas las tareas
    path('tarea/<int:id>/', views.detalle_tarea, name='detalle_tarea'),  # Detalle de una tarea específica
    path('sprints/', views.sprints, name='sprints'),    # Lista de todos los sprints
    path('epicas/', views.epicas, name='epicas'),       # Lista de todas las épicas
]
