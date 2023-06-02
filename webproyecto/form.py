from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Imagen



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

class UsuarioForm (forms.ModelForm):

    class Meta: 
        model = Usuario
        fields = ['run','nombre','correo','numero']

#nuevo
class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ('imagen', 'descripcion')


