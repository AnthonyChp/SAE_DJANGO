# Generated by Django 4.2.1 on 2023-05-20 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0015_alter_machine_maintenancedate_alter_personnel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 27, 15, 43, 25, 760890)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='email',
            field=models.EmailField(default='{prenom}.{nom}@RTdev.com', editable=False, max_length=254),
        ),
    ]
