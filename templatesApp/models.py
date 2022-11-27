from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)

    