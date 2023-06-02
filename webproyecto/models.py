from django.db import models


# Create your models here.
class categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)

    def __str__(self) -> str:
        return super().__str__()

class Anime(models.Model):
    idAnime = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=45)
    anio=models.IntegerField()
    descripcion=models.TextField()
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)
#Cosas de prueba 

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='galeria/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.nombre


class Usuario(models.Model):
    run=models.IntegerField(null=False, blank=True)
    nombre=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    numero=models.CharField(max_length=12)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    

#nuevo
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    descripcion = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    




    