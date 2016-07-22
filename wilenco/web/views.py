# views.py
import json
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
"""Para el correo electronico"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage

"""
 Django Views for wilenco project.
 Autor: Wilenco
 Nombre: views.py
 Descripcion: Archivo que contiene las vistas del sitio web.
 Version: 2.1
 Fecha de Creacion: Mayo 30/2016
 Ultima modificacion: Julio 06/2016
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
    productos = Producto.objects.all()
    return render(request, 'product.html', {'productos':productos})

def cotizacion(request):
    """  Funcion  "cotizacion"
         Descripcion: Funcion que hace render la pagina de cotizacion.
         Fecha de Creacion: Junio 19/2016
         Fecha de Modificacion: Junio 20/2016"""
    return render(request, 'cotizacion.html', {})

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

def filtrar_productos(request):
    """
        Funcion: "filtrar_productos"
        Descripcion: Funcion que devuelve un json con datos de los productos
                     que han sido solicitados por el cliente de acuerdo con
                     criterios como marca, tipo.
        Fecha de Creacion: Junio 19/2016
        Fecha de Modificacion: Junio 19/2016
    """
    if (request.method == 'POST'):
        marcas_solicitadas = request.POST['marcas_para_filtrado']
        productos_devueltos = {'productos_por_marca':[]}
        for marca in marcas_solicitadas:
            productos_de_esta_marca = Producto.objects.filter(marca=marca)
            for producto in productos_de_esta_marca:
                productos_devueltos['productos_por_marca'].append( json.dumps({'nombre': producto.nombre ,'imagen': producto.imagen}))
        productos_devueltos_json = json.dumps(productos_devueltos)
    return HttpResponse(productos_devueltos_json, content_type='application/json')

def enviarContacto(request):
    """
        Funcion: ""
        Descripcion:
        Fecha de Creacion: Julio 06/2016
        Fecha de Modificacion: Julio 07/2016
    """
        #if (request.method == 'POST'):
    nombre = request.GET['nombre']
    """email = request.POST.get('email', '')
    telefono = request.POST.get('telefono', '')"""
    asunto = request.GET['asunto']
    print nombre + '-'+ asunto
    mensaje = nombre + '-'  + asunto
    """mensaje = nombre + '-' + email +  '-' + telefono + '-'  + asunto"""
    status = send_mail('kattyadesiderio@gmail.com','Mensaje ...', mensaje)
    data=[]
    data.append(status)
    return HttpResponse(json.dumps(data))

def send_mail(recipient, subject, body):
    import smtplib

    gmail_user = 'kattyadesiderio@gmail.com'
    gmail_pwd = '-----'
    FROM = 'kattyadesiderio@gmail.com'
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO),SUBJECT,TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.startls()
        server.login(gmail_user, gmail_pwd)
        server.send_mail(FROM, TO, message)
        server.close()
        return 'correo enviado con exito.'
    except:
        return 'envio de correo fallido'

def get_categorias(request):
    data = {
        'categorias' : []
    }
    categorias = Producto.objects.values('categoria').distinct()
    for categoria in categorias:
        data['categorias'].append(categoria['categoria'])
    # print q.query
    return HttpResponse(json.dumps(data))

def get_marcas(request):
    data = {
        'marcas' : []
    }
    marcas = Producto.objects.values('marca').distinct()
    for marca in marcas:
        data['marcas'].append(marca['marca'])
    # print q.query
    return HttpResponse(json.dumps(data))
