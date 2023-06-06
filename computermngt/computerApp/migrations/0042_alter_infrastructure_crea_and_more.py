# Generated by Django 4.2.1 on 2023-06-06 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0041_remove_infrastructure_date_mise_a_jour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 16, 57, 10, 187951), editable=False),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 16, 57, 10, 186951)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 16, 57, 10, 188951)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='crea',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 16, 57, 10, 188951), editable=False),
        ),
    ]
