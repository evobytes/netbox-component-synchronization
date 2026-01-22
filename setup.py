from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netbox_component_synchronization',
    version='5.0.3',
    description='Syncing existing components with the components from a device type template in NetBox 4+',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Keith Knowles and Bastian Leicht and Dave Bevan',
    author_email='mkknowles@outlook.com',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
