from django.db import migrations, models
import taggit.managers
import utilities.json

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('extras', '0001_initial'),
        ('dcim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentSyncPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Synchronization Button',
                'verbose_name_plural': 'Synchronization Button',
                'permissions': [('can_use', 'Can use component sync tools')],
            },
        ),
    ]
