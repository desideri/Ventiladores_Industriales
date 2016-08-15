from web.models import *
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('noSerie', 'nombre','stock','marca','categoria','potencia','capacidad','motor','presion','descripcion','imagen')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('categoria',)
