import uuid
from django.db import models
from apps.equipment.models import Equipment


class Magnitude(models.TextChoices):

    lenght = 'LNG'
    time = 'CRN'
    mass = 'BAS'
    speed = 'FOT'
    temperature = 'TEMP'
    electric = 'MULT'


class MeasuringEquipment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment = models.OneToOneField(Equipment, verbose_name='Equipo', on_delete=models.CASCADE)
    meassurment_range_max = models.DecimalField('rango máximo', max_digits=6, decimal_places=3)
    meassurment_range_min = models.DecimalField('rango mínimo', max_digits=6, decimal_places=3)
    resolution = models.DecimalField('resolution', max_digits=6, decimal_places=3)
    emp = models.DecimalField('EMP', max_digits=6, decimal_places=3)
    magnitude = models.CharField("Magnitud", max_length=50, choices=Magnitude.choices, default=Magnitude.speed)

    class Meta:

        verbose_name = 'Instrumento de medición'
        verbose_name_plural = 'Instrumentos de medición'

    def __str__(self):
        return f"{self.magnitude} - {self.equipment} "
