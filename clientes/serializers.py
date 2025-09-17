from rest_framework import serializers
from .models import Cliente, Mascota

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id', 'nombre', 'apellidos', 'fullnombre', 'email', 'telefono', 'dni',
            'created_at', 'is_active'
        ]
        read_only_field = ['id', 'fullnombre', 'created_at']

class MascotaSerializer(serializers.ModelSerializer):
    cliente_fullnombre = serializers.CharField(source="cliente.fullnombre", read_only=True)
    class Meta:
        model = Mascota
        fields=['id','nombre','especie','raza','edad','peso','created_at','is_active','cliente','cliente_fullnombre']
        read_only_fields = ['created_at']