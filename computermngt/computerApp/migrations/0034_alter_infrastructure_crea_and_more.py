# Generated by Django 4.2.1 on 2023-05-21 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0033_alter_infrastructure_crea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 12, 13, 12, 174966), editable=False),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 12, 13, 12, 174966)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 12, 13, 12, 201972)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 12, 13, 12, 201972), editable=False),
        ),
    ]