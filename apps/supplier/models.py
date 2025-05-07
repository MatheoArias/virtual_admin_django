from django.db import models
import uuid


class Supplier(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField('Nombre', max_length=80, blank=False, null=False)
    nit = models.CharField('Nit', max_length=20, blank=False, null=False, unique=True)
    telephone = models.CharField('Teléfono', max_length=10, blank=False, null=False)
    address = models.CharField( 'Dirección', max_length=150, blank=False, null=False)
    email = models.EmailField('Correo electrónico',max_length=254, blank=False, null=False)
    city = models.CharField('Ciudad', max_length=50, blank=False, null=False)

    class Meta:
        
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.name
