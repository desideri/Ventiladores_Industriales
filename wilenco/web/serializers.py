from web.models import *
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    # formularios = serializers.StringRelatedField(many=True)
    class Meta:
        model = Producto
        fields = ('noSerie', 'nombre','stock','marca','modelo','potencia','capacidad','descripcion','imagen')
