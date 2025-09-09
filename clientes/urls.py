from django.urls import path
from .views import ClienteAPIView

urlpatterns = [
    path('', ClienteAPIView.as_view(), name='cliente-list'),
    #path('/', admin.site.urls),
]