# Generated by Django 3.0.7 on 2020-09-30 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('log_incident_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('impact', models.TextField(blank=True, null=True)),
                ('cause', models.TextField(blank=True, null=True)),
                ('remedy', models.TextField(blank=True, null=True)),
                ('action_items', models.TextField(blank=True, null=True)),
                ('incident_start', models.DateTimeField(default=datetime.datetime.now)),
                ('incident_end', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'log_incident',
            },
        ),
    ]
