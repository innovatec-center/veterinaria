from django.urls import path
from .views import AtencionAPIView, AtencionDetailAPIView

urlpatterns = [
    path('', AtencionAPIView.as_view(), name='atencion-list'),
    path('<int:pk>/', AtencionDetailAPIView.as_view(), name='atencion-detail'),
]