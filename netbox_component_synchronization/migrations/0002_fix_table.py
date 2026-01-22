from django.db import migrations, models
import taggit.managers
import utilities.json

def add_columns_if_missing(apps, schema_editor):
    column_names = [column.name for column in schema_editor.connection.introspection.get_table_description(schema_editor.connection.cursor(), "netbox_component_synchronization_componentsyncpermission")]

    # Add description if missing
    if 'description' not in column_names:
        schema_editor.execute('ALTER TABLE netbox_component_synchronization_componentsyncpermission ADD COLUMN description varchar(200) NOT NULL DEFAULT \'\'')

    # Add custom_field_data if missing
    if 'custom_field_data' not in column_names:
        schema_editor.execute('ALTER TABLE netbox_component_synchronization_componentsyncpermission ADD COLUMN custom_field_data jsonb NOT NULL DEFAULT \'{}\'::jsonb')

class Migration(migrations.Migration):
    dependencies = [
        ('extras', '0001_initial'),
        ('netbox_component_synchronization', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_columns_if_missing),
        # This tells Django's internal state that the fields now exist without running SQL
        migrations.AddField(
            model_name='componentsyncpermission',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='componentsyncpermission',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AddField(
            model_name='componentsyncpermission',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
    ]
