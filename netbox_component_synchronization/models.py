from netbox.models import NetBoxModel


class ComponentSyncPermissionAnchor(NetBoxModel):
    """
    Permission anchor model.

    REQUIRED for NetBox 4.4.10 so that plugin permissions
    appear in the UI and can be assigned to groups.
    """

    class Meta:
        verbose_name = "Component Synchronization"
        verbose_name_plural = "Component Synchronization"
        permissions = (
            ("use_component_synchronization", "Can use component sync tools"),
        )
