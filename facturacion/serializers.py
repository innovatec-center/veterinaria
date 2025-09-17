from rest_framework import serializers
from .models import Facturacion

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = [
            'id', 'venta','tipo','serie', 'numero', 'fecha', 'created_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at']