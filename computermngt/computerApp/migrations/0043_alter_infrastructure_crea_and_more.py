# Generated by Django 4.2.1 on 2023-06-06 14:58

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0042_alter_infrastructure_crea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='crea',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 16, 58, 7, 184473)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 16, 58, 7, 185473)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 16, 58, 7, 185473), editable=False),
        ),
    ]
