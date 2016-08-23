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
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from push_notifications.models import GCMDevice
from django.views.decorators.csrf import csrf_exempt

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

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('categoria')

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitdSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

def exportServicios(request):
    data = []
    solicitudes = Solicitud.objects.all()
    for solicitud in solicitudes:
        # cliente = Cliente.objects.get(pk=solicitud.cliente.id)
        solicitudic = {
            "tipo": solicitud.tipoSolicitud,
            "descripcion": solicitud.descripcion,
            "fechaCreada": "{}/{}/{}".format(solicitud.fechaCreada.year,solicitud.fechaCreada.month,solicitud.fechaCreada.day),
            "fechaEscojida": "{}/{}/{}".format(solicitud.fechaEscojida.year, solicitud.fechaEscojida.month, solicitud.fechaEscojida.day),
            "cliente" : {
                "nombre": solicitud.cliente.nombre,
                "cedula": solicitud.cliente.cedula,
                "direccion": solicitud.cliente.direccion,
                "telefono": solicitud.cliente.telefono,
                "email": solicitud.cliente.email
            }
        }
        data.append(solicitudic)
    return HttpResponse(json.dumps(data))

def exportCotizacion(request):
    data = []
    cotizaciones = Cotizacion.objects.all()
    for cotizacion in cotizaciones:
        prodcot = ProductosEnCotizacion.objects.filter(cotizacion=cotizacion.id)
        productos = []
        for element in prodcot:
            producto  = {
                "nombre": element.producto.nombre,
                "categoria": element.producto.categoria.categoria,
                "marca": element.producto.marca,
                "cantidad": element.cantidad
            }
            productos.append(producto)

        cotizaciondic = {
            "descripcion": cotizacion.descripcionObra,
            "totalproductos": cotizacion.total_productos,
            "cliente":{
                "nombre": cotizacion.cliente.nombre,
                "cedula": cotizacion.cliente.cedula,
                "direccion": cotizacion.cliente.direccion,
                "telefono": cotizacion.cliente.telefono,
                "email": cotizacion.cliente.email
            },
            "productos":productos
        }
        data.append(cotizaciondic)
    return HttpResponse(json.dumps(data))

def save_cotizacion(request):
    if request.method == 'POST':
        cliente = None
        try:
            cliente = Cliente.objects.get(cedula=request.POST['cedula'])
        except:
            cliente = Cliente.objects.create(cedula=request.POST['cedula'], nombre=request.POST['nombre'], direccion=request.POST['direccion'], telefono=request.POST['telefono'], email=request.POST['email'])

        cotizacion = Cotizacion.objects.create(cliente=cliente,descripcionObra=request.POST['descripcion'],total_productos=request.POST['total_productos'])
        productos = json.loads(request.POST['productos'])
        for element in productos:
            producto = Producto.objects.get(nombre=element['nombre'], marca=element['marca'], capacidad=element['capacidad'])
            pro_cot = ProductosEnCotizacion.objects.create(cotizacion= cotizacion, producto=producto, cantidad = element['cantidad'])

        return HttpResponse("datos guardados")
        

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

def enviarContacto(request):
    """
         Funcion: "enviarContacto"
         Descripcion: Esta funcion permite al usuario de la pagina enviar los
         datos que ingreso en el formulario de contactenos del sitio web.
         Fecha de Creacion: Julio 06/2016
         Fecha de Modificacion: Julio 23/2016
     """
    if (request.method == 'POST'):
        """nombre,email,telefono,asunto"""
        nombre = request.POST.get('nombre', None)
        asunto = "Infomacion de contacto de" + " " + nombre
        from_email = request.POST.get('email', None)
        to_email=settings.EMAIL_HOST_USER
        telefono = request.POST.get('telefono', None)
        contenido_mensaje = request.POST.get('mensaje', None)
        if asunto and contenido_mensaje and from_email:
            try:
                 titulo = '<h2>Formulario de Cont&aacute;ctenos</h2><br>'
                 c_nombre = '<p ><strong>Nombre: </strong>' + nombre
                 c_email = '</p><br><p><strong>Email: </strong>' + from_email
                 c_telefono ='</p><br><p><strong>Tel&eacute;fono: </strong>' + telefono
                 c_mensaje = '</p><br><p><strong>Mensaje: </strong>' + contenido_mensaje + '</p>'
                 html_content = titulo + c_nombre + c_email + c_telefono + c_mensaje
                 msg = EmailMultiAlternatives(asunto, html_content, from_email, [to_email])
                 msg.content_subtype = "html"
                 msg.send()
                 return HttpResponseRedirect('/contacto/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')


def enviarCotizacion(request):
    """
        Funcion: "enviarCotizacion"
        Descripcion: Esta funcion permite al usuario de la pagina enviar los
        datos que ingreso en el formulario de cotizacion del sitio web.
        Fecha de Creacion: Julio 24/2016
        Fecha de Modificacion: Julio 24/2016
    """
    if (request.method == 'POST'):
        """nombre,email,telefono,asunto"""
        nombre = request.POST.get('nombre', None)
        apellido = request.POST.get('apellido', None)
        asunto = "Cotizacion de " + " " + nombre + " " + apellido
        from_email = request.POST.get('email', None)
        to_email=settings.EMAIL_HOST_USER
        cedula = request.POST.get('cedula', None)
        telefono = request.POST.get('telefono', None)
        direccion = request.POST.get('direccion', None)
        descripcion = request.POST.get('descripcion', None)
        if asunto and from_email:
            try:
                titulo = '<h2>Formulario de Cotizaci&oacute;n</h2><br>'
                c_articulos= '<h3>Lista de Productos Cotizados</h3><br>'
                c_divCli= '<h3>Datos del Cliente</h3>'
                c_nombre = '<br><p><strong>Cliente: </strong>' + nombre + " " + apellido
                c_cedula = '</p><br><p><strong>C&eacute;dula: </strong>' + cedula
                c_email = '</p><br><p><strong>Email: </strong>' + from_email
                c_telefono ='</p><br><p><strong>Tel&eacute;fono: </strong>' + telefono
                c_direccion ='</p><br><p><strong>Direcci&oacute;n: </strong>' + direccion
                c_divObra= '</p><br><h3>Datos de la Obra</h3>'
                c_mensaje = '<br><p><strong>Descripci&oacute;n de la Obra: </strong>' + descripcion + '</p>'
                html_content = titulo + c_articulos + c_divCli + c_nombre + c_cedula + c_email + c_telefono + c_direccion + c_divObra + c_mensaje
                msg = EmailMultiAlternatives(asunto, html_content, from_email, [to_email])
                msg.content_subtype = "html"
                msg.send()
                return HttpResponseRedirect('/cotizacion/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

def enviarServicio(request):
    """
        Funcion: "enviarServicio"
        Descripcion: Esta funcion permite al usuario de la pagina enviar los
        datos que ingreso en el formulario de contactenos del sitio web.
        Fecha de Creacion: Julio 24/2016
        Fecha de Modificacion: Julio 24/2016
    """
    if (request.method == 'POST'):
        nombre =  request.POST.get('nombre', None)
        apellido =  request.POST.get('apellido', None)
        cedula =  request.POST.get('cedula', None)
        from_email =  request.POST.get('email', None)
        telefono =  request.POST.get('telefono', None)
        direccion =  request.POST.get('direccion', None)
        fecha =  request.POST.get('fecha', None)
        tipo =  request.POST.get('tipo', None)
        descripcion =  request.POST.get('descripcion', None)
        to_email=settings.EMAIL_HOST_USER
        asunto = "Agendar Servicio de " + tipo +  " para " + nombre + " " + apellido
        if asunto and from_email:
            try:
                titulo = '<h2>Formulario de Servicio</h2><br>'
                c_divCli= '<h3>Datos del Cliente</h3><br>'
                c_nombre = '<p><strong>Nombre: </strong>' + nombre
                c_apellido = '</p><br><p><strong>Apellido: </strong>' + apellido
                c_cedula = '</p><br><p><strong>Cedula: </strong>' + cedula
                c_email = '</p><br><p><strong>Email: </strong>' + from_email
                c_telefono ='</p><br><p><strong>Tel&eacute;fono: </strong>' + telefono
                c_direccion ='</p><br><p><strong>Direcci&oacute;n: </strong>' + direccion
                c_divServ= '<h3>Datos del Servicio</h3><br>'
                c_fecha = '</p><br><p><strong>Fecha: </strong>' + fecha
                c_tipo ='</p><br><p><strong>Tipo: </strong>' + tipo
                c_descripcion ='</p><br><p><strong>Descripci&oacute;n: </strong>' + descripcion
                html_content = titulo + c_divCli + c_nombre + c_apellido + c_cedula + c_email + c_telefono + c_direccion + c_divServ + c_fecha + c_tipo + c_descripcion

                msg = EmailMultiAlternatives(asunto, html_content, from_email, [to_email])
                msg.content_subtype = "html"
                msg.send()
                return HttpResponseRedirect('/servicio/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

# Save information device for Notification Push
@csrf_exempt
def register_device(request):
    response = {}
    device_id = request.POST.get('device_id',None)
    registration_id = request.POST.get('registration_id',None)

    if device_id and registration_id:
        gcm_device = GCMDevice.objects.filter(device_id=device_id)

        if gcm_device:
            gcm_device = gcm_device.firts()

        else:
            gcm_device = GCMDevice.objects.create(name="wilenco",device_id=device_id,registration_id=registration_id)
            gcm_device.save()

        response = {'id':gcm_device.id,}

    return JsonResponde(response)
