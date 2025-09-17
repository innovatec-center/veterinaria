from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fullnombre = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True) 
    dni = models.CharField(max_length=20, unique=True)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellidos = self.apellidos.upper()
        self.fullnombre = f"{self.apellidos.upper()} {self.nombre.upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.fullnombre
    
    class Meta:
        ordering = ['fullnombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
    peso = models.DecimalField(max_digits=4,decimal_places=2, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #campos de auditoria o trazabilidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_by = models.CharField(max_length=100, blank=True)
    deleted_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.especie = self.especie.upper()
        self.raza = self.raza.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.fullnombre} - {self.nombre}"
    
    class Meta:
        ordering = ['cliente__fullnombre', 'nombre']
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
    
