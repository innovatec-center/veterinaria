from django.shortcuts import render
from django.utils import timezone
from .models import Atencion
from .serializers import AtencionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AtencionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        atenciones = Atencion.objects.filter(is_active=True)
        atenciones_serializadas = AtencionSerializer(atenciones, many=True)
        return Response(atenciones_serializadas.data)
    
    def post(self, request):
        atencion_serializada = AtencionSerializer(data=request.data)
        if atencion_serializada.is_valid():
            atencion_serializada.save()
            return Response(atencion_serializada.data, status=status.HTTP_201_CREATED)
        return Response(atencion_serializada.errors, status=400)

class AtencionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        atencion = Atencion.objects.get(pk=pk)
        atencion_serializada = AtencionSerializer(atencion)
        return Response(atencion_serializada.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        atencion = Atencion.objects.get(pk=pk)
        if atencion is not None:
            atencion_serializada = AtencionSerializer(atencion, data=request.data)
            if atencion_serializada.is_valid():
                atencion_serializada.save()
                return Response(atencion_serializada.data, status=status.HTTP_200_OK)
            return Response(atencion_serializada.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        atencion = Atencion.objects.get(pk=pk)
        if atencion is not None:
            atencion.is_active = False
            atencion.deleted_at = timezone.now()
            if request.user.is_authenticated:
                atencion.deleted_by = request.user.username
            else:
                atencion.deleted_by = 'Sistema'
            atencion.save()
        return Response(status=status.HTTP_404_NOT_FOUND)