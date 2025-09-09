from django.shortcuts import render
from .models import Cliente
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClienteSerializer

# Create your views here.
class ClienteAPIView(APIView):
    def get(self, request):
        clientes = Cliente.objects.filter(is_active=True)
        cliente_serializados = ClienteSerializer(clientes, many=True)
        return Response(cliente_serializados.data)