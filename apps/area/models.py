from django.db import models
import uuid

class Area (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField('Descripción',max_length=200, blank=False, null=False)
    
    class Meta:
        verbose_name='Area'
        verbose_name_plural='Areas'
        
    def __str__(self):
        return self.description
        
    