from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

"""
Validadores
Conjunto de funciones que validan los datos ingresados antes de guardarlos
"""

"""
@is1394 (Israel Fernandez)
Funcion que valida que un string sea un nombre correcto
"""
def validate_nombre(nombre):
    ex_reg = re.compile("[a-zA-Z]+")
    result = re.match(ex_reg,nombre)
    if bool(result) == False:
        raise ValidationError(
        _('%(nombre)s no es valido, inserte un nombre valido'),
        params={'nombre': nombre},
    )

"""
@is1394 (Israel Fernandez)
Funcion que valida que una categoria correcta
"""
def validate_categoria(categoria):
    ex_reg = re.compile("[a-zA-Z]+")
    result = re.match(ex_reg,categoria)
    if bool(result) == False:
        raise ValidationError(
        _('%(categoria)s no es valido, inserte una categoria valida'),
        params={'categoria': categoria},
    )

"""
@is1394 (Israel Fernandez)
Funcion que valida que una marca sea correcta
"""
def validate_marca(marca):
    ex_reg = re.compile("[a-zA-Z]+")
    result = re.match(ex_reg,marca)
    if bool(result) == False:
        raise ValidationError(
        _('%(marca)s no es valido, inserte una marca valida'),
        params={'marca': marca},
    )

"""
@is1394 (Israel Fernandez)
Funcion que valida que el stock  sea consistente
"""
def validate_stock(stock):
    if stock > 100 or stock < 0:
        raise ValidationError(
        _('%(stock)s no es un valor consistente, inserte un valor valido entre 0 - 100'),
        params={'stock': stock},
        )




"""
Modelos
"""
class Categoria(models.Model):
    categoria = models.CharField(max_length=50, validators=[validate_categoria], primary_key=True)

    def __str__(self):
        return "{}".format(self.categoria)

    def __unicode__(self):
        return unicode(str(self))

class Producto(models.Model):
    """
    @is1394 (Israel Fernandez)
    Entidad Producto contiene informacion relevante sobre cada uno de los productos
    ofrecidos por la empresa"""

    noSerie = models.CharField(max_length=10,blank=True,null=True)
    nombre = models.CharField(max_length=50, validators=[validate_nombre])
    stock = models.IntegerField(validators=[validate_stock])
    marca = models.CharField(max_length=50, validators=[validate_marca])
    # categoria = models.CharField(max_length=50,validators=[validate_categoria])
    categoria = models.ForeignKey(Categoria,blank=False,null=False)
    potencia = models.CharField(max_length=50, blank=True,null=True)
    motor = models.CharField(max_length=50, blank=True, null=True)
    presion = models.CharField(max_length=50,blank=True, null=True)
    capacidad = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='img/productos', blank=True,
                               null=True)



    def __str__(self):
        return "{}".format(self.nombre)

    def __unicode__(self):
        return unicode(str(self))

    def save(self, *args, **kwargs):
        self.noSerie  = "PROD" + str(len(Producto.objects.all()) + 1)
        super(Producto, self).save(*args, **kwargs)

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
