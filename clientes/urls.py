from django.urls import path
from .views import ClienteAPIView, ClienteDetailAPIView
from .views import MascotaAPIView, MascotaDetailAPIView

urlpatterns = [
    path('', ClienteAPIView.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetailAPIView.as_view(), name='cliente-detail'),
    path('mascotas/', MascotaAPIView.as_view(), name='mascota-list'),
    path('mascotas/<int:pk>/', MascotaDetailAPIView.as_view(), name='mascota-detail'),
]