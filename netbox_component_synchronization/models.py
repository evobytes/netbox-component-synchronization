from netbox.models import NetBoxModel

class ComponentSyncPermission(NetBoxModel):
    class Meta:
        verbose_name = "Synchronize Button"
        verbose_name_plural = "Synchronize Button"
        permissions = (
            ("can_use", "Can use component sync tools"),
        )
