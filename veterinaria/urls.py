from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('catalogo/',include('catalogo.urls')),
    path('ventas/',include('ventas.urls')),
    path('citas/',include('citas.urls')),
    path('facturacion/',include('facturacion.urls')),
]
