from netbox.models import NetBoxModel


class ComponentSyncPermission(NetBoxModel):
    """
    Permission model.

    REQUIRED for NetBox 4.4.10 so that plugin permissions
    appear in the UI and can be assigned to groups.
    """

    class Meta:
        verbose_name = "Synchronize Button"
        verbose_name_plural = "Synchronize Button"
        permissions = (
            ("can_use", "Can use component sync tools"),
        )
