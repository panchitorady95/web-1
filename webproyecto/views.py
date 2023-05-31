from django.shortcuts import render
#nuevo
from .models import Imagen



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

