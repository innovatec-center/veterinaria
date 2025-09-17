from rest_framework import serializers
from .models import Venta, DetalleVenta

class VentaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source="cliente.fullnombre",read_only=True)
    class Meta:
        model = Venta
        fields = [
            'id', 'cliente','cliente_nombre', 'fecha', 'total', 'created_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at']

class DetalleVentaSerializer(serializers.ModelSerializer):
    servicio_nombre = serializers.CharField(source="servicio.nombre",read_only=True)
    producto_nombre = serializers.CharField(source="producto.nombre",read_only=True)
    class Meta:
        model = DetalleVenta
        fields = [
            'id', 'venta', 'producto','producto_nombre','servicio','servicio_nombre','cantidad','precio_unitario', 'subtotal', 'created_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at']