from django.db import models

class Producto(models.Model):
    """
    @is1394 (Israel Fernandez)
    Entidad Producto contiene informacion relevante sobre cada uno de los productos
    ofrecidos por la empresa"""
    noSerie = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/productos', blank=True,
                               null=True)


class Solicitud(models.Model):
    """
    @desideri (Kattya Desiderio)
    Clase  "Solicitud"
    Descripcion: Entidad para receptar la Solicitud de
    Instalacion/Mantenimiento.
    Fecha de Creacion: Junio 03/2016
    Fecha de Modificacion: Junio 06/2016"""
    tipo = models.BooleanField(default=False) #0 Mantemiento / 1 Instalacion
    descripcion = models.CharField(max_length=50) # Descripcion que desee dar
                                                  # el cliente
    fechaCreada = models.DateField(auto_now=True)   # Fecha de la Creacion de
                                                    #  la Solicitud
    fechaEscojida = models.DateField() # Fecha tentativa del cliente para el
                                       # Mantemiento/Instalacion
    nombre = models.CharField(max_length=50)   # Nombre
    apellido = models.CharField(max_length=50) # Apellido
    cedulaCliente = models.CharField(max_length=10) # Cedula


class Cotizador(models.Model):
    """
    @Jsayala (Jorge Ayala)
    Entidad Cotizador contiene informacion relevante sobre cada cliente que
    solicita una cotizacion, como fecha, id de cotizacion,  descripcion de
    obra o producto a cotizar"""
    cotizadorID = models.CharField(max_length=10)
    fechaDeSolicitud = models.DateField()
    nombresCliente = models.CharField(max_length=20)
    apellidosCliente = models.CharField(max_length=20)
    telefonoCliente = models.CharField(max_length=15)
    mailCliente = models.CharField(max_length=50)
    descripcionObra = models.CharField(max_length=50)
