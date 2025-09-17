from django.shortcuts import render
from django.utils import timezone
from .models import Cliente, Mascota
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClienteSerializer, MascotaSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClienteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        clientes = Cliente.objects.filter(is_active=True)
        cliente_serializados = ClienteSerializer(clientes, many=True)
        return Response(cliente_serializados.data)
    
    def post(self, request):
        cliente_serializado = ClienteSerializer(data=request.data)
        if cliente_serializado.is_valid():
            cliente_serializado.save()
            return Response(cliente_serializado.data, status=status.HTTP_201_CREATED)
        return Response(cliente_serializado.errors, status=400)

class ClienteDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente_serializado = ClienteSerializer(cliente)
        return Response(cliente_serializado.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        cliente = Cliente.objects.get(pk=pk)
        if cliente is not None:
            cliente_serializado = ClienteSerializer(cliente, data=request.data)
            if cliente_serializado.is_valid():
                cliente_serializado.save()
                return Response(cliente_serializado.data, status=status.HTTP_200_OK)
            return Response(cliente_serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        cliente = Cliente.objects.get(pk=pk)
        if cliente is not None:
            cliente.is_active = False
            cliente.deleted_at = timezone.now()
            if request.user.is_authenticated:
                cliente.deleted_by = request.user.username
            else:
                cliente.deleted_by = 'Sistema'
            cliente.save()
        return Response(status=status.HTTP_404_NOT_FOUND)

class MascotaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mascotas = Mascota.objects.filter(is_active=True)
        mascotas_serializadas = MascotaSerializer(mascotas, many=True)
        return Response(mascotas_serializadas.data)
    
    def post(self, request):
        mascota_serializada = MascotaSerializer(data=request.data)
        if mascota_serializada.is_valid():
            mascota_serializada.save()
            return Response(mascota_serializada.data, status=status.HTTP_201_CREATED)
        return Response(mascota_serializada.errors, status=400)

class MascotaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mascota = Mascota.objects.get(pk=pk)
        mascota_serializada = MascotaSerializer(mascota)
        return Response(mascota_serializada.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        mascota = Mascota.objects.get(pk=pk)
        if mascota is not None:
            mascota_serializada = MascotaSerializer(mascota, data=request.data)
            if mascota_serializada.is_valid():
                mascota_serializada.save()
                return Response(mascota_serializada.data, status=status.HTTP_200_OK)
            return Response(mascota_serializada.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        mascota = Mascota.objects.get(pk=pk)
        if mascota is not None:
            mascota.is_active = False
            mascota.deleted_at = timezone.now()
            if request.user.is_authenticated:
                mascota.deleted_by = request.user.username
            else:
                mascota.deleted_by = 'Sistema'
            mascota.save()
        return Response(status=status.HTTP_404_NOT_FOUND)