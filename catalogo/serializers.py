from rest_framework import serializers
from .models import CategoriaProducto, Producto,Servicio

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = [
            'id', 'cliente', 'descripcion', 'created_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at']

class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source="categoriaproducto.nombre", read_only=True)
    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'precio','stock','categoria','categoria_nombre','is_active'
        ]
        read_only_fields = ['id', 'created_at']

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = [
            'id', 'nombre', 'descripcion', 'precio','is_active'
        ]
        read_only_fields = ['id', 'created_at']