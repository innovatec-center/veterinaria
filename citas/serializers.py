from rest_framework import serializers
from .models import Atencion

class AtencionSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source="mascota.nombre",read_only=True)
    class Meta:
        model = Atencion
        fields = [
            'id', 'mascota','detalle_venta','mascota_nombre', 'fecha', 'hora','motivo', 'observaciones', 'created_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at','mascota_nombre']