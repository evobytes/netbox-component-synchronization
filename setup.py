from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netbox_component_synchronization',
    version='5.0.5',
    description='Syncing existing components with the components from a device type template in NetBox 4+',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Keith Knowles and Bastian Leicht and Dave Bevan',
    author_email='mkknowles@outlook.com',
    url='https://github.com/evobytes/netbox-component-synchronization/',
    license='GPL-3.0',
    packages=["netbox_component_synchronization"],
    package_data={
        "netbox_component_synchronization": [
            "templates/netbox_component_synchronization/*.html",
            "migrations/*.py",
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/evobytes/netbox-component-synchronization/issues",
        "Source Code": "https://github.com/evobytes/netbox-component-synchronization/",
    },
    zip_safe=False
)
