# urls.py
from django.conf.urls import include, url
from django.contrib import admin

"""
 Django Urls for wilenco project.
 Autor: Wilenco
 Nombre: urls.py
 Descripcion: Archivo que contiene las urls del sitio web.
 Version: 2.1
 Fecha de Creacion: Mayo 30/2016
 Ultima modificación: junio 06/2016
 Ultimo modificador: Kattya Desiderio
"""
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'web.views.index'), # URl para la pagina de index

    url(r'^contacto/', 'web.views.contacto'), #URL para la pagina de Contactenos

    url(r'^productos/', 'web.views.product'), #URL para la pagina de Productos

    url(r'^empresa/', 'web.views.empresa'), #URL para la pagina de Empresa: Mision, Vision, Obras

]
