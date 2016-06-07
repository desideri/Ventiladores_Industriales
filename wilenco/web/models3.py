from django.db import models
"""
@Jsayala (Jorge Ayala)
Entidad Cotizador contiene informacion relevante sobre cada el cliente que solicita una
cotizacion, como fecha, id de cotizacion,  descripcion de obra o producto a cotizar
"""
class Cotizador(models.Model):
    """ Modelo Cotizador """
    cotizadorID = models.CharField(max_length=10)
    fechaDeSolicitud = models.DateField()
    nombresCliente = models.CharField(max_length=20)
    apellidosCliente = models.CharField(max_length=20)
    telefonoCliente = models.CharField(max_length=15)
    mailCliente = models.CharField(max_length=50)
    descripcionObra = models.CharField(max_length=50)
    
	
