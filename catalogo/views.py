from django.shortcuts import render
from django.utils import timezone
from .models import CategoriaProducto, Producto, Servicio
from .serializers import CategoriaProductoSerializer, ProductoSerializer, ServicioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Create your views here.
class CategoriaProductoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        categorias_productos = CategoriaProducto.objects.filter(is_active=True)
        categorias_serializadas = CategoriaProductoSerializer(categorias_productos, many=True)
        return Response(categorias_serializadas.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        categoria_producto = CategoriaProductoSerializer(data=request.data)
        if categoria_producto.is_valid():
            categoria_producto.save()
            return Response(categoria_producto.data, status=status.HTTP_201_CREATED)
        return Response(categoria_producto.errors, status=400)
    
class CategoriaProductoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        categoria_producto = CategoriaProducto.objects.get(pk=pk)
        categoria_producto_serializado = CategoriaProductoSerializer(categoria_producto)
        return Response(categoria_producto_serializado.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        categoria_producto = CategoriaProducto.objects.get(pk=pk)
        if categoria_producto is not None:
            categoria_producto_serializado = CategoriaProductoSerializer(categoria_producto, data=request.data)
            if categoria_producto_serializado.is_valid():
                categoria_producto_serializado.save()
                return Response(categoria_producto_serializado.data, status=status.HTTP_200_OK)
            return Response(categoria_producto_serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        categoria_producto = CategoriaProducto.objects.get(pk=pk)
        if categoria_producto is not None:
            categoria_producto.is_active = False
            categoria_producto.deleted_at = timezone.now()
            if request.user.is_authenticated:
                categoria_producto.deleted_by = request.user.username
            else:
                categoria_producto.deleted_by = 'Sistema'
            categoria_producto.save()
        return Response(status=status.HTTP_404_NOT_FOUND)

class ProductoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        productos = Producto.objects.filter(is_active=True)
        productos_serializados = ProductoSerializer(productos, many=True)
        return Response(productos_serializados.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        producto_serializado = ProductoSerializer(data=request.data)
        if producto_serializado.is_valid():
            producto_serializado.save()
            return Response(producto_serializado.data, status=status.HTTP_201_CREATED)
        return Response(producto_serializado.errors, status=400)
    
class ProductoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        producto = Producto.objects.get(pk=pk)
        producto_serializado = ProductoSerializer(producto)
        return Response(producto_serializado.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        producto = Producto.objects.get(pk=pk)
        if producto is not None:
            producto_serializado = ProductoSerializer(producto, data=request.data)
            if producto_serializado.is_valid():
                producto_serializado.save()
                return Response(producto_serializado.data, status=status.HTTP_200_OK)
            return Response(producto_serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        producto = Producto.objects.get(pk=pk)
        if producto is not None:
            producto.is_active = False
            producto.deleted_at = timezone.now()
            if request.user.is_authenticated:
                producto.deleted_by = request.user.username
            else:
                producto.deleted_by = 'Sistema'
            producto.save()
        return Response(status=status.HTTP_404_NOT_FOUND)

class ServicioAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        servicios = Servicio.objects.filter(is_active=True)
        servicios_serializados = ServicioSerializer(servicios, many=True)
        return Response(servicios_serializados.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        servicio_serializado = ServicioSerializer(data=request.data)
        if servicio_serializado.is_valid():
            servicio_serializado.save()
            return Response(servicio_serializado.data, status=status.HTTP_201_CREATED)
        return Response(servicio_serializado.errors, status=400)
    
class ServicioDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        servicio = Servicio.objects.get(pk=pk)
        servicio_serializado = ServicioSerializer(servicio)
        return Response(servicio_serializado.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        servicio = Servicio.objects.get(pk=pk)
        if servicio is not None:
            servicio_serializado = ServicioSerializer(servicio, data=request.data)
            if servicio_serializado.is_valid():
                servicio_serializado.save()
                return Response(servicio_serializado.data, status=status.HTTP_200_OK)
            return Response(servicio_serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        servicio = Servicio.objects.get(pk=pk)
        if servicio is not None:
            servicio.is_active = False
            servicio.deleted_at = timezone.now()
            if request.user.is_authenticated:
                servicio.deleted_by = request.user.username
            else:
                servicio.deleted_by = 'Sistema'
            servicio.save()
        return Response(status=status.HTTP_404_NOT_FOUND)