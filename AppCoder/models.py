from django.db import models

# Create your models here.




class Articulo(models.Model):
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.cantidad}"

class Carrito(models.Model):
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.cantidad}"

   
class Cliente (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    contrasena=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   