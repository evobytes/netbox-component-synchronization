from django.db import models
from netbox.models import NetBoxModel

class ComponentSyncPermission(NetBoxModel):
    description = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name = "Synchronize Button"
        verbose_name_plural = "Synchronize Button"
        permissions = (
            ("can_use", "Can use component sync tools"),
        )
