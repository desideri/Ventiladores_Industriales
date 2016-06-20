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
    categoria = models.CharField(max_length=50)
    potencia = models.CharField(max_length=50, blank=True,null=True)
    motor = models.CharField(max_length=50, blank=True, null=True)
    presion = models.CharField(max_length=50,blank=True, null=True)
    capacidad = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='img/productos', blank=True,
                               null=True)

class Cliente(models.Model):
    """
    @is1394 (Israel Fernandez)
    Entidad Cliente contiene informacion relevante sobre cada cliente registrado"""
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

class Solicitud(models.Model):
    """
    @desideri (Kattya Desiderio)
    Clase  "Solicitud"
    Descripcion: Entidad para receptar la Solicitud de
    Instalacion/Mantenimiento.
    Fecha de Creacion: Junio 03/2016
    Fecha de Modificacion: Junio 06/2016"""

    tipo = (('MANT', 'Mantenimiento'),('INST','Instalacion'))

    tipoSolicitud = models.CharField(max_length=4,choices=tipo)
    descripcion = models.TextField() # Descripcion que desee dar
                                                  # el cliente
    fechaCreada = models.DateField(auto_now=True)   # Fecha de la Creacion de
                                                    #  la Solicitud
    fechaEscojida = models.DateField() # Fecha tentativa del cliente para el
                                       # Mantemiento/Instalacion
    cliente = models.ForeignKey(Cliente)


class Cotizacion(models.Model):
    """
    @Jsayala (Jorge Ayala)
    Entidad Cotizacion contiene informacion relevante sobre cada cliente que
    solicita una cotizacion, como fecha, id de cotizacion,  descripcion de
    obra o producto a cotizar"""
    cotizadorID = models.CharField(max_length=10)
    fechaDeSolicitud = models.DateField(auto_now=True)
    cliente = models.ForeignKey(Cliente,null=False)
    producto = models.ManyToManyField(Producto, blank=False, null=False)
    descripcionObra = models.TextField()
