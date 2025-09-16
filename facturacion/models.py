from django.db import models
from ventas.models import Venta
# Create your models here.
class Facturacion(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    tipo_Comprobante_Options={1:'Boleta',2:'Factura', 3:'Ticket'}
    tipo = models.IntegerField(choices=tipo_Comprobante_Options)
    serie = models.CharField(max_length=10)
    numero = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.serie = self.serie.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha} - {self.venta.cliente.fullnombre} "

    class Meta:
        ordering = ['-fecha', 'venta__cliente__fullnombre']
        verbose_name = 'Comprobate'
        verbose_name_plural = 'Comprobates'