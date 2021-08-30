from django.db import models

# la columna id se crea automaticamente, es entero y se autoincrementa

# Create your models here.
class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    equipo=models.CharField(max_length=50)

class Equipo(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)