from django.db import models

class Usuarios(models.Model):
    UserAcces = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=20)
    ApellidoPaterno = models.CharField(max_length=20)
    ApellidoMaterno = models.CharField(max_length=20)
    Correo =  models.EmailField(max_length=70)
    Telefono = models.IntegerField(max_length=10)
    Pass = models.CharField(max_length=80)
    Roll = models.CharField(max_length=20)

class Proyectos(models.Model):
    IdProyect = models.CharField(max_length=20, primary_key=True)
    ProyectName = models.CharField(max_length=80)
    UserAccesArq = models.CharField(max_length=20)
    UserAccesAdm = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)

class Materiales(models.Model):
    IdKey = models.CharField(max_length=40, primary_key=True)
    IdProyect = models.ForeignKey(Proyectos, null=False, blank=False, on_delete=models.CASCADE)
    IdMaterial =  models.CharField(max_length=20)
    MaterialName = models.CharField(max_length=80)
    MaterialDeseado = models.IntegerField(max_length=10)
    MaterialEntregado = models.IntegerField(max_length=10)
    UndiadMaterial = models.CharField(max_length=20)
    FechaEntrega = models.DateField()
    



# Create your models here