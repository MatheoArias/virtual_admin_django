import uuid
from django.db import models
from apps.position.models import Position


class Liable(models.Model):
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique= True)
    position=models.ForeignKey(Position, verbose_name='Cargo', on_delete=models.CASCADE)
    code=models.CharField('Código', max_length=10, blank=True, null=False, unique=True)
    name=models.CharField('Nombre', max_length=100,blank=True, null=False)
    lastName=models.CharField("Apellidos", max_length=100, blank=True, null=False)
    email=models.EmailField('Correo Electrónico', max_length=254, blank=True, null=False, unique=True)
    telephone=models.CharField('Teléfono', max_length=10, blank=False, null=False )
    workstation=models.CharField('Ubicación', max_length=50, blank=True, null=True)
    image=models.ImageField('Imagen', upload_to='liables/', null=True, blank=True)
    active=models.BooleanField('Estado', default=True)
    
    class Meta:
        
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        
        return f"{self.code} - {self.name} {self.lastName}"

    
