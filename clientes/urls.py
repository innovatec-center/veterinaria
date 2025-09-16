from django.urls import path
from .views import ClienteAPIView, ClienteDetailAPIView

urlpatterns = [
    path('', ClienteAPIView.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetailAPIView.as_view(), name='cliente-detail'),
]