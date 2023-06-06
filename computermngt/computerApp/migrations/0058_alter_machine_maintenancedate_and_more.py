# Generated by Django 4.2.1 on 2023-06-06 16:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0057_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 18, 17, 52, 278536)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='infrastructure',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnel', to='computerApp.infrastructure'),
        ),
    ]
