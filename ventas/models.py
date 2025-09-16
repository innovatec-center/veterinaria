from django.db import models
from clientes.models import Cliente, Mascota
from catalogo.models import Producto, Servicio

# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.cliente.fullnombre} - {self.fecha.strftime("%d-%m-%Y")}'

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.venta.cliente.fullnombre} - {self.venta.id} - {self.producto.nombre}'
    
    class Meta:
        ordering = ['venta']
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de ventas'