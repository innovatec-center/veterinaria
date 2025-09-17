from django.urls import path
from .views import FacturacionAPIView, facturacionDetailAPIView

urlpatterns = [
    path('', FacturacionAPIView.as_view(), name='facturacion-list'),
    path('<int:pk>/', facturacionDetailAPIView.as_view(), name='facturacion-detail'),
]