from django.db import models

# Create your models here.
"""
@is1394 (Israel Fernandez)
Entidad Producto contiene informacion relevante sobre cada uno de los productos
ofrecidos por la empresa
"""
class Producto(models.Model):
    """ Modelo Producto """
    noSerie = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/productos', blank=True, null=True)
	