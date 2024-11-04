from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from scrum.models import Tarea
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

def base(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('listar_tareas')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class ListarTarea(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea/listar_tareas.html'
    context_object_name = 'tarea'
    ordering = ['fecha_publicacion']
    permission_required = ('scrum.listar_tareas')

    def get_queryset(self):
        return Tarea.objects.all()
    
class EliminarTarea(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tarea/eliminar_tarea.html'
    success_url = reverse_lazy('listar_tareas')
    permission_required = ('scrum.delete_tarea')
