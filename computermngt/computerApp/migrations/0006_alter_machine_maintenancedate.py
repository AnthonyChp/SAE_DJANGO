# Generated by Django 4.2.1 on 2023-06-07 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0005_machine_adresse_ip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 14, 18, 4, 9, 705867)),
        ),
    ]
