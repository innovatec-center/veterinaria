from django.shortcuts import render
from django.utils import timezone
from .models import Facturacion
from .serializers import FacturacionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class FacturacionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        facturaciones = Facturacion.objects.filter(is_active=True)
        facturaciones_serializadas = FacturacionSerializer(facturaciones, many=True)
        return Response(facturaciones_serializadas.data)
    
    def post(self, request):
        facturacion_serializada = FacturacionSerializer(data=request.data)
        if facturacion_serializada.is_valid():
            facturacion_serializada.save()
            return Response(facturacion_serializada.data, status=status.HTTP_201_CREATED)
        return Response(facturacion_serializada.errors, status=400)

class facturacionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        facturacion = Facturacion.objects.get(pk=pk)
        facturacion_serializada = FacturacionSerializer(facturacion)
        return Response(facturacion_serializada.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        facturacion = Facturacion.objects.get(pk=pk)
        if facturacion is not None:
            facturacion_serializada = FacturacionSerializer(facturacion, data=request.data)
            if facturacion_serializada.is_valid():
                facturacion_serializada.save()
                return Response(facturacion_serializada.data, status=status.HTTP_200_OK)
            return Response(facturacion_serializada.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        facturacion = Facturacion.objects.get(pk=pk)
        if facturacion is not None:
            facturacion.is_active = False
            facturacion.deleted_at = timezone.now()
            if request.user.is_authenticated:
                facturacion.deleted_by = request.user.username
            else:
                facturacion.deleted_by = 'Sistema'
            facturacion.save()
        return Response(status=status.HTTP_404_NOT_FOUND)