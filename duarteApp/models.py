from django.db import models

# Create your models here.


class Automovil(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()
    diseño = models.CharField(max_length=100)
    cilindraje = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.marca}"
