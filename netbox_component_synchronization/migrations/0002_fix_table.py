from django.db import migrations

def add_columns_if_missing(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name = 'netbox_component_synchronization_componentsyncpermission'"
        )
        existing_columns = [row[0] for row in cursor.fetchall()]

    if 'description' not in existing_columns:
        schema_editor.execute("ALTER TABLE netbox_component_synchronization_componentsyncpermission ADD COLUMN description varchar(200) NOT NULL DEFAULT ''")

    if 'custom_field_data' not in existing_columns:
        schema_editor.execute("ALTER TABLE netbox_component_synchronization_componentsyncpermission ADD COLUMN custom_field_data jsonb NOT NULL DEFAULT '{}'::jsonb")

class Migration(migrations.Migration):
    dependencies = [
        ('netbox_component_synchronization', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(add_columns_if_missing),
            ],
            state_operations=[], # Empty! 0001 already defines the state perfectly.
        ),
    ]
