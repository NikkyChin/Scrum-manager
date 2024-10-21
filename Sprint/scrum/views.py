from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea, Epica, Sprint

# Vista para listar todas las tareas
class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'
    context_object_name = 'tareas'

# Vista para mostrar el detalle de una tarea
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'
    context_object_name = 'tarea'

# Vista para crear una nueva tarea
class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'criterios_aceptacion', 'prioridad', 'estado', 'esfuerzo_estimado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
    success_url = reverse_lazy('tarea-list')

# Vista para actualizar una tarea existente
class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'criterios_aceptacion', 'prioridad', 'estado', 'esfuerzo_estimado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
    success_url = reverse_lazy('tarea-list')

# Vista para eliminar una tarea
class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea-list')

# Vistas para Epicas (CRUD similar a Tarea)
class EpicaListView(ListView):
    model = Epica
    template_name = 'epicas/epica_list.html'
    context_object_name = 'epicas'

class EpicaDetailView(DetailView):
    model = Epica
    template_name = 'epicas/epica_detail.html'
    context_object_name = 'epica'

class EpicaCreateView(CreateView):
    model = Epica
    template_name = 'epicas/epica_form.html'
    fields = ['nombre', 'descripcion', 'criterios_aceptacion', 'estado', 'responsable', 'tareas_asociadas', 'esfuerzo_estimado_total', 'fecha_inicio', 'fecha_fin', 'progreso', 'dependencias']
    success_url = reverse_lazy('epica-list')

class EpicaUpdateView(UpdateView):
    model = Epica
    template_name = 'epicas/epica_form.html'
    fields = ['nombre', 'descripcion', 'criterios_aceptacion', 'estado', 'responsable', 'tareas_asociadas', 'esfuerzo_estimado_total', 'fecha_inicio', 'fecha_fin', 'progreso', 'dependencias']
    success_url = reverse_lazy('epica-list')

class EpicaDeleteView(DeleteView):
    model = Epica
    template_name = 'epicas/epica_confirm_delete.html'
    success_url = reverse_lazy('epica-list')

# Vistas para Sprints (CRUD similar a Tarea)
class SprintListView(ListView):
    model = Sprint
    template_name = 'sprints/sprint_list.html'
    context_object_name = 'sprints'

class SprintDetailView(DetailView):
    model = Sprint
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'sprint'

class SprintCreateView(CreateView):
    model = Sprint
    template_name = 'sprints/sprint_form.html'
    fields = ['nombre', 'objetivo', 'fecha_inicio', 'fecha_fin', 'velocidad', 'scrum_master', 'equipo_desarrollo', 'backlog_sprint']
    success_url = reverse_lazy('sprint-list')

class SprintUpdateView(UpdateView):
    model = Sprint
    template_name = 'sprints/sprint_form.html'
    fields = ['nombre', 'objetivo', 'fecha_inicio', 'fecha_fin', 'velocidad', 'scrum_master', 'equipo_desarrollo', 'backlog_sprint']
    success_url = reverse_lazy('sprint-list')

class SprintDeleteView(DeleteView):
    model = Sprint
    template_name = 'sprints/sprint_confirm_delete.html'
    success_url = reverse_lazy('sprint-list')
