from django.db import models

# Create your models here.
class Django_Seminario(models.Model):
    nombrePersona      = models.CharField(max_length=50)
    telefono           = models.IntegerField()
    fechaSeminario     = models.DateField()
    empresaInstitucion = models.CharField(max_length=50)
    email              = models.EmailField()
    profesion          = models.CharField(max_length=50)
    observaciones      = models.CharField(max_length=200)

