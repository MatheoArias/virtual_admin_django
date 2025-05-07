import uuid
from django.db import models
from apps.area.models import Area


class Category(models.TextChoices):
    measurement_instrument='IM',
    industrial_machine='MI'


class Equipment(models.Model):
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True)
    area=models.ForeignKey(Area, verbose_name='Area', on_delete=models.CASCADE)
    name=models.CharField('Equipo', max_length=80, null=False, blank=False)
    model=models.CharField('Modelo', max_length=50, null=False, blank=False)
    code= models.CharField('Código', max_length=50, null=True, blank=True, unique=True)
    serie=models.CharField('Serie', max_length=20, null=False, blank=False)
    mannufacturer=models.CharField('Fabricante', max_length=50, null=False, blank=False)
    installed=models.DateField('Instalación', auto_now=False, auto_now_add=False)
    purchased=models.DateField('Adquirido', auto_now=False, auto_now_add=False)
    description=models.TextField('Descripción')
    accesories=models.TextField('Accesorios')
    manteinance_interval=models.IntegerField('Mantenimiento | Meses')
    category=models.CharField('Categoría', max_length=20,choices=Category.choices, default=Category.industrial_machine)
    image=models.ImageField('Imágen', upload_to='equipments/', blank=True, null=True)
    
    class Meta:
        
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return f"{self.code} - {self.name} {self.model} {self.serie}"
    
    
    