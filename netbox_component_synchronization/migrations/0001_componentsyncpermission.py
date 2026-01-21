from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # NetBox core dependency (safe baseline)
        ("dcim", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComponentSyncPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Synchronization Button",
                "verbose_name_plural": "Synchronization Button",
                "permissions": [
                    ("can_use", "Can use component sync tools"),
                ],
            },
        ),
    ]
