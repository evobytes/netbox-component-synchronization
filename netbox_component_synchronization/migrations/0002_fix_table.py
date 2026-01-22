from django.db import migrations, models
import taggit.managers
import utilities.json

def add_columns_if_missing(apps, schema_editor):
    # Use the schema_editor connection to check the actual database state
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name = 'netbox_component_synchronization_componentsyncpermission'"
        )
        existing_columns = [row[0] for row in cursor.fetchall()]

    # Add description if it's not already there
    if 'description' not in existing_columns:
        schema_editor.execute(
            "ALTER TABLE netbox_component_synchronization_componentsyncpermission "
            "ADD COLUMN description varchar(200) NOT NULL DEFAULT ''"
        )

    # Add custom_field_data if it's not already there
    if 'custom_field_data' not in existing_columns:
        schema_editor.execute(
            "ALTER TABLE netbox_component_synchronization_componentsyncpermission "
            "ADD COLUMN custom_field_data jsonb NOT NULL DEFAULT '{}'::jsonb"
        )

class Migration(migrations.Migration):
    dependencies = [
        ('extras', '0001_initial'),
        ('netbox_component_synchronization', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            # 1. Database Operations: Run our custom logic to add columns ONLY if missing
            database_operations=[
                migrations.RunPython(add_columns_if_missing),
            ],
            # 2. State Operations: Tell Django these fields exist so it stops nagging you.
            # No SQL is fired for these lines.
            state_operations=[
                migrations.AddField(
                    model_name='componentsyncpermission',
                    name='description',
                    field=models.CharField(blank=True, max_length=200),
                ),
                migrations.AddField(
                    model_name='componentsyncpermission',
                    name='custom_field_data',
                    field=models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                migrations.AddField(
                    model_name='componentsyncpermission',
                    name='tags',
                    field=taggit.managers.TaggableManager(
                        through='extras.TaggedItem',
                        to='extras.Tag'
                    ),
                ),
            ],
        ),
    ]
