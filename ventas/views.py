from django.shortcuts import render
from django.utils import timezone
from .models import Venta, DetalleVenta
from .serializers import VentaSerializer, DetalleVentaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class VentaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ventas = Venta.objects.filter(is_active=True)
        ventas_serializadas = VentaSerializer(ventas, many=True)
        return Response(ventas_serializadas.data)
    
    def post(self, request):
        venta_serializada = VentaSerializer(data=request.data)
        if venta_serializada.is_valid():
            venta_serializada.save()
            return Response(venta_serializada.data, status=status.HTTP_201_CREATED)
        return Response(venta_serializada.errors, status=400)

class VentaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        venta = Venta.objects.get(pk=pk)
        venta_serializada = VentaSerializer(venta)
        return Response(venta_serializada.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        venta = Venta.objects.get(pk=pk)
        if venta is not None:
            venta_serializada = VentaSerializer(venta, data=request.data)
            if venta_serializada.is_valid():
                venta_serializada.save()
                return Response(venta_serializada.data, status=status.HTTP_200_OK)
            return Response(venta_serializada.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        venta = Venta.objects.get(pk=pk)
        if venta is not None:
            venta.is_active = False
            venta.deleted_at = timezone.now()
            if request.user.is_authenticated:
                venta.deleted_by = request.user.username
            else:
                venta.deleted_by = 'Sistema'
            venta.save()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class DetalleVentaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        detalle_ventas = DetalleVenta.objects.filter(is_active=True)
        detalle_ventas_serializadas = DetalleVentaSerializer(detalle_ventas, many=True)
        return Response(detalle_ventas_serializadas.data)
    
    def post(self, request):
        detalle_venta_serializada = DetalleVentaSerializer(data=request.data)
        if detalle_venta_serializada.is_valid():
            detalle_venta_serializada.save()
            return Response(detalle_venta_serializada.data, status=status.HTTP_201_CREATED)
        return Response(detalle_venta_serializada.errors, status=400)

class DetalleVentaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        detalle_venta = DetalleVenta.objects.get(pk=pk)
        detalle_venta_serializada = DetalleVentaSerializer(detalle_venta)
        return Response(detalle_venta_serializada.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        detalle_venta = DetalleVenta.objects.get(pk=pk)
        if detalle_venta is not None:
            detalle_venta_serializada = DetalleVentaSerializer(detalle_venta, data=request.data)
            if detalle_venta_serializada.is_valid():
                detalle_venta_serializada.save()
                return Response(detalle_venta_serializada.data, status=status.HTTP_200_OK)
            return Response(detalle_venta_serializada.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        detalle_venta = DetalleVenta.objects.get(pk=pk)
        if detalle_venta is not None:
            detalle_venta.is_active = False
            detalle_venta.deleted_at = timezone.now()
            if request.user.is_authenticated:
                detalle_venta.deleted_by = request.user.username
            else:
                detalle_venta.deleted_by = 'Sistema'
            detalle_venta.save()
        return Response(status=status.HTTP_404_NOT_FOUND)