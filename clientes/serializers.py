from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id', 'nombre', 'apellidos', 'fullnombre', 'email', 'telefono', 'dni',
            'created_at', 'is_active'
        ]
        read_only_field = ['id', 'fullnombre', 'created_at']