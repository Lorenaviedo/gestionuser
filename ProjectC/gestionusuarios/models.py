from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

