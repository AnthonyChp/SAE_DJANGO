# Generated by Django 4.2.1 on 2023-05-21 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0031_infrastructure_crea_infrastructure_maintenancedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 11, 58, 32, 995399), editable=False),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 11, 58, 32, 995399)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 11, 58, 33, 22405)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 11, 58, 33, 22405), editable=False),
        ),
    ]
