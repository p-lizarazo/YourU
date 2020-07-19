from django.db import models
from django.conf import settings
from university.models import Program, Period


class CostoDeVida(models.Model):
    PAIS = (
        ('Colombia', 'Colombia'), ('Ecuador', 'Ecuador'), ('Mexico', 'Mexico'),
        ('Rusia', 'Rusia'), ('Inglaterra', 'Inglaterra'), ('Perú', 'Perú'),
        ('Estados Unidos', 'Estados Unidos'), ('Chile', 'Chile'), ('Ecuador', 'Ecuador')
    )
    pais = models.CharField(max_length=15, choices=PAIS, unique=True)
    ciudad = models.CharField(max_length=15, blank=True)
    costo_habitacion = models.DecimalField(max_digits=20, decimal_places=0)
    costo_comida = models.DecimalField(max_digits=20, decimal_places=0)
    costo_transporte = models.DecimalField(max_digits=20, decimal_places=0)


# Create your models here.
class MyPlan(models.Model):
    name = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    costo_habitacion = models.BooleanField(default=True)
    costo_comida = models.BooleanField(default=True)
    costo_transporte = models.BooleanField(default=True)
    costo_matricula = models.BooleanField(default=True)
    application_deadline = models.DateField(null=True, blank=True)
    cost = models.ForeignKey( CostoDeVida, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



