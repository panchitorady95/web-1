from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)

    def __str__(self) -> str:
        return super().__str__()

class Anime(models.Model):
    idAnime = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=45)
    año=models.IntegerField()
    descripcion=models.TextField()
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)
#Cosas de prueba 

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='galeria/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.nombre


    