# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Lana(models.Model):
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='lanas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self): return f"{self.marca} {self.color}"

class Herramienta(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Aguja Crochet
    medida = models.CharField(max_length=20) # Ej: 3mm
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='herramientas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self): return f"{self.nombre} - {self.medida}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self): return self.nombre

class Product(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True)
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion = RichTextField(blank=True)
    imagen = models.ImageField(upload_to='products/', blank=True, null=True)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
