import uuid
from django.db import models


class Liable(models.Model):
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique= True)
    code=models.CharField('Código', max_length=10, blank=True, null=False, unique=True)
    name=models.CharField('Nombre', max_length=100,blank=True, null=False)
    lastName=models.CharField("Apellidos", max_length=100, blank=True, null=False)
    email=models.EmailField('Correo Electrónico', max_length=254, blank=True, null=False, unique=True)
    telephone=models.CharField('Teléfono', max_length=10, blank=False, null=False )
    workstation=models.CharField("Ubicación", max_length=50, blank=True, null=True)
    image=models.ImageField("Imagen", upload_to='liables/', null=True, blank=True)
    
    class Meta:
        
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'

    def __str__(self):
        
        return f"{self.code} - {self.name} {self.lastName}"

    
       
