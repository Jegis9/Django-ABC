from django.db import models

# Create your models here.
class Task(models.Model):
    carnet = models.CharField(max_length=50)  # Suponiendo que el carnet es un texto de hasta 50 caracteres
    nombres = models.CharField(max_length=100)  # Suponiendo que los nombres tienen un máximo de 100 caracteres
    apellidos = models.CharField(max_length=100)  # Suponiendo que los apellidos tienen un máximo de 100 caracteres
    correoelectronico = models.EmailField()  # Campo de correo electrónico válido
    fechaNacimiento = models.DateField()  # Campo de fecha de nacimiento
