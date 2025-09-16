from django.contrib import admin
from .models import CategoriaProducto, Producto, Servicio
# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Servicio)