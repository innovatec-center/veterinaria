from django.urls import path
from .views import CategoriaProductoAPIView, CategoriaProductoDetailAPIView
from .views import ProductoAPIView, ProductoDetailAPIView
from .views import ServicioAPIView, ServicioDetailAPIView

urlpatterns = [
    path('categorias/', CategoriaProductoAPIView.as_view(), name='categoria-producto-list'),
    path('categorias/<int:pk>/', CategoriaProductoDetailAPIView.as_view(), name='categoria-producto-detail'),
    path('productos/', ProductoAPIView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailAPIView.as_view(), name='producto-detail'),
    path('servicios/', ServicioAPIView.as_view(), name='servicio-list'),
    path('servicios/<int:pk>/', ServicioDetailAPIView.as_view(), name='servicio-detail'),
]