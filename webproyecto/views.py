from django.shortcuts import render
#nuevo
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .models import * 
from webproyecto.form import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def formulario(request):
    return render(request,"formulario.html")

def inicio(request):
    return render(request,"inicio.html")
#nuevo
def galeria(request):
    imagenes = Imagen.objects.all()
    return render(request, 'galeria.html', {'imagenes': imagenes})

def registro(request):
    datos = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            
            user_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        datos["form"] = formulario
    return render(request, 'registration/registro.html', datos)

def login(request):
    messages.success(request, "Has iniciado correctamente")
    return render(request, 'registration/login.html')
