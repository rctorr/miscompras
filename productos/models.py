from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_compra = models.DateTimeField(blank=True, null=True)

    def comprar(self):
        self.fecha_compra = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
