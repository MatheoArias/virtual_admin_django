import uuid
from django.db import models

class Position(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    code=models.CharField('Código', max_length=10, blank=True, null=False)
    name=models.CharField('Nombre', max_length=100,blank=True, null=False)
    lastName=models.CharField("Apellidos", max_length=100, blank=True, null=False)
    email=models.EmailField('Correo Electrónico', max_length=254, blank=True, null=False)
    telephone=models.CharField('Teléfono', max_length=10, blank=False, null=False )
    workstation=models.CharField("Ubicación", max_length=50, blank=True, null=True)
    
       
