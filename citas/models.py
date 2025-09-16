from django.db import models
from clientes.models import Mascota
from ventas.models import DetalleVenta
# Create your models here.
class Atencion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    detalle_venta = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True)
    observaciones = models.TextField(blank=True, null=True)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.motivo = self.motivo.upper()
        if self.observaciones:
            self.observaciones = self.observaciones.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.mascota.cliente.fullnombre} - {self.mascota.nombre} - {self.fecha}'
    
    class Meta:
        ordering = ['mascota__cliente__fullnombre', 'fecha']
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'