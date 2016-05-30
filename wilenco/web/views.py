from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contacto(request):
    return render(request, 'contact.html', {})

def product(request):
    return render(request, 'product.html', {})

def empresa(request):
    return render(request, 'empresa.html', {})
