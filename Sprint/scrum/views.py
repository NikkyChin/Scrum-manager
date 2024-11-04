from django.shortcuts import render
from django.urls import reverse_lazy


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def base(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})