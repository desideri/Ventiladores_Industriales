# urls.py
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from web import views


"""
 Django Urls for wilenco project.
 Autor: Wilenco
 Nombre: urls.py
 Descripcion: Archivo que contiene las urls del sitio web
 Version: 2.1
 Fecha de Creacion: Mayo 30/2016
 Ultima modificacion: Junio 07/2016
 Ultimo modificador: Kattya Desiderio
"""

router = routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'web.views.index'), # URl para la pagina de index

    url(r'^contacto/', 'web.views.contacto'), #URL para la pagina de Contactenos

    url(r'^productos/', 'web.views.product'), #URL para la pagina de Productos

    url(r'^productos/filtrar', 'web.views.filtrar_productos'), #URL para la pagina de Productos

    url(r'^empresa/', 'web.views.empresa'), #URL para la pagina de Empresa: Mision, Vision, Obras

    url(r'^servicio/', 'web.views.servicio'), #URL para la pagina de Servicio: Mantenimiento, Instalacion

    #RestFramework
    url(r'^api/', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
