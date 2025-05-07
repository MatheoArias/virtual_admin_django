import uuid
from django.db import models


class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField("Código", max_length=10, blank=True, null=False)
    name = models.CharField("Descripción", max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positiones"

    def __str__(self):
        return f"{self.code} {self.name}"
