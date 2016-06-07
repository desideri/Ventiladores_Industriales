# views.py

from django.shortcuts import render
"""
 Django Views for wilenco project.
 Autor: Wilenco
 Nombre: views.py
 Descripcion: Archivo que contiene las vistas del sitio web.
 Version: 2.1
 Fecha de Creacion: Mayo 30/2016
 Ultima modificacion: junio 06/2016
 Ultimo modificador: Kattya Desiderio
"""

# Funcion  "index"
# Descripcion: Funcion que hace render el index.
# Fecha de Creacion: Junio 03/2016
# Fecha de Modificacion: Junio 06/2016
def index(request):
    return render(request, 'index.html', {})

# Funcion  "contacto"
# Descripcion: Funcion que hace render la pagina de Contactenos.
# Fecha de Creacion: Junio 03/2016
# Fecha de Modificacion: Junio 06/2016
def contacto(request):
    return render(request, 'contact.html', {})

# Funcion  "product"
# Descripcion: Funcion que hace render la pagina de Productos.
# Fecha de Creacion: Junio 03/2016
# Fecha de Modificacion: Junio 06/2016
def product(request):
    return render(request, 'product.html', {})

# Funcion  "empresa"
# Descripcion: Funcion que hace render la pagina de Empresa.
# Fecha de Creacion: Junio 03/2016
# Fecha de Modificacion: Junio 06/2016
def empresa(request):
    return render(request, 'empresa.html', {})
