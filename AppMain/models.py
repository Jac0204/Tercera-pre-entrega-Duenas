from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=8)
    email = models.EmailField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    activo = models.BooleanField(default=True)


