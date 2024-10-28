from django.db import models

estado=[
    (1,'Activo'),
    (2,'Inactivo')
]

class Jugador(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    tag= models.CharField(max_length=50)
    edad= models.CharField(max_length=50)
    correo= models.CharField(max_length=50)
    estado= models.IntegerField(
        null=False, blank=False, choices=estado
    )

# Create your models here.
