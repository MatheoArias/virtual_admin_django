import uuid
from django.db import models
from apps.equipment.models import Equipment
from apps.liable.models import Liable


class Category(models.TextChoices):
    preventive='P',
    corrective='C'
    

class Maintenance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment = models.ForeignKey(Equipment, verbose_name='Equipo', on_delete=models.CASCADE)
    liable = models.ForeignKey(Liable, verbose_name='Responsable', on_delete=models.CASCADE)
    number = models.CharField('Número', max_length=10, unique=True)
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    category=models.CharField('Categoría', max_length=10,choices=Category.choices, default=Category.preventive)
    diagnostic = models.TextField('Diagnóstico')
    activities = models.TextField('Actividades')

    class Meta:

        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return f"{self.number} - {self.equipment}"
