import uuid
from django.db import models
from ..supplier.models import Supplier



class Calibration(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier= models.ForeignKey(Supplier, verbose_name=("Proveedor"), on_delete=models.CASCADE)
    number=models.CharField("Número", max_length=10, blank=False, null=False)
    date=models.DateField("Fecha", auto_now=False, auto_now_add=False)
    calibration_range_max=models.DecimalField("punto máximo", max_digits=6, decimal_places=3)
    calibration_range_min=models.DecimalField("punto mínimo",max_digits=6, decimal_places=3)
    uncertainty=models.DecimalField("Incertidumbre",max_digits=6, decimal_places=3)
    error=models.DecimalField("Error",max_digits=6, decimal_places=3)
    link=models.CharField("Link")
    
    class Meta:
        verbose_name='Calibración'
        verbose_name_plural='Calibraciones'
        
    def __str__(self):
        return self.supplier.name + self.number

