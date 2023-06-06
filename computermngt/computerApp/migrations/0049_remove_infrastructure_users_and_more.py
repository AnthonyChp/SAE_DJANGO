# Generated by Django 4.2.1 on 2023-06-06 15:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computerApp', '0048_infrastructure_users_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infrastructure',
            name='users',
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infrastructures', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 13, 17, 45, 35, 509136)),
        ),
    ]