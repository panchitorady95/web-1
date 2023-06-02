
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView #Importacion para deslogearse
from .views import *
#nuevo
from . import views
urlpatterns = [
    path('', index, name='index'),
    path('formulario/', formulario,name='FORMU'),
    path('inicio/', inicio,name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    
]

