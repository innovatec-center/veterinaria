from django.urls import path
from .views import VentaAPIView, VentaDetailAPIView
from .views import DetalleVentaAPIView, DetalleVentaDetailAPIView

urlpatterns = [
    path('', VentaAPIView.as_view(), name='venta-list'),
    path('<int:pk>/', VentaDetailAPIView.as_view(), name='venta-detail'),
    path('detalle/', DetalleVentaAPIView.as_view(), name='detalle-venta-list'),
    path('detalle/<int:pk>/', DetalleVentaDetailAPIView.as_view(), name='detalle-venta-detail'),
]