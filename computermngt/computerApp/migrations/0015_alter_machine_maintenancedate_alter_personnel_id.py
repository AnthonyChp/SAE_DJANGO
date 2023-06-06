# Generated by Django 4.2.1 on 2023-05-20 13:41

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0014_personnel_email_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 27, 15, 41, 37, 390308)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='id',
            field=models.PositiveIntegerField(editable=False, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
    ]
