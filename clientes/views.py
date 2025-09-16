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
    
    def post(self, request):
        cliente_serializado = ClienteSerializer(data=request.data)
        if cliente_serializado.is_valid():
            cliente_serializado.save()
            return Response(cliente_serializado.data, status=201)
        return Response(cliente_serializado.errors, status=400)

class ClienteDetailAPIView(APIView):
    def get(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente_serializado = ClienteSerializer(cliente)
        return Response(cliente_serializado.data)