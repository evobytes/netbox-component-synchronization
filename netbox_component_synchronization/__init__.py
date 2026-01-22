from netbox.plugins import PluginConfig


class Config(PluginConfig):
    name = "netbox_component_synchronization"
    verbose_name = "Component Synchronization Plugin"
    description = "Easily synchronize device components with their device types through an accessible UI."
    version = "5.0.3"
    author = "Keith Knowles and Bastian Leicht and Dave Bevan"
    author_email = "mkknowles@outlook.com"
    default_settings = {
        "include_interfaces_panel": False,
        # Compare description during diff
        # If compare is true, description will also be synced to device
        # Otherwise not.
        "compare_description": True,
        "exclude_interface_type_list": [
            "lag",
            "bridge",
        ],
    }


config = Config
