from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import ListarTarea, EliminarTarea

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('listar_tareas/', ListarTarea.as_view(), name='listar_tareas'),
    path('eliminar_tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]