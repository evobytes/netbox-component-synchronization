from netbox.models import ChangeLoggedModel


class ComponentSyncPermission(ChangeLoggedModel):
    class Meta:
        verbose_name = "Synchronize Button"
        verbose_name_plural = "Synchronize Button"
        permissions = (
            ("can_use", "Can use component sync tools"),
        )
