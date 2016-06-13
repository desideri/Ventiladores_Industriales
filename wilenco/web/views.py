# views.py
from django.shortcuts import render
from web.models import *
from web.serializers import *
#APIREST
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
"""
 Django Views for wilenco project.
 Autor: Wilenco
 Nombre: views.py
 Descripcion: Archivo que contiene las vistas del sitio web.
 Version: 2.1
 Fecha de Creacion: Mayo 30/2016
 Ultima modificacion: junio 07/2016
 Ultimo modificador: Kattya Desiderio
"""

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('noSerie','nombre', 'marca')


def index(request):
    """ Funcion  "index"
        Descripcion: Funcion que hace render el index.
        Fecha de Creacion: Junio 03/2016
        Fecha de Modificacion: Junio 06/2016"""
    return render(request, 'index.html', {})

def contacto(request):
    """  Funcion  "contacto"
         Descripcion: Funcion que hace render la pagina de Contactenos.
         Fecha de Creacion: Junio 03/2016
         Fecha de Modificacion: Junio 06/2016 """
    return render(request, 'contact.html', {})

def product(request):
    """  Funcion  "product"
         Descripcion: Funcion que hace render la pagina de Productos.
         Fecha de Creacion: Junio 03/2016
         Fecha de Modificacion: Junio 06/2016"""
    return render(request, 'product.html', {})

def empresa(request):
    """ Funcion  "empresa"
        Descripcion: Funcion que hace render la pagina de Empresa.
        Fecha de Creacion: Junio 03/2016
        Fecha de Modificacion: Junio 06/2016"""
    return render(request, 'empresa.html', {})

def servicio(request):
    """ Funcion  "servicio"
        Descripcion: Funcion que hace render la pagina de Servicio.
        Fecha de Creacion: Junio 07/2016
        Fecha de Modificacion: Junio 07/2016"""
    return render(request, 'servicio.html', {})
