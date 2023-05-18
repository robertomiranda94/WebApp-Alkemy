from django.db import models

# Create your models here
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)


class Servicio(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=200)
	precio = models.FloatField(default=0.0)
	activo = models.BooleanField(default=True)

class Coordinador(models.Model):
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    numero_documento = models.IntegerField(blank=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    activo = models.BooleanField(default=True)