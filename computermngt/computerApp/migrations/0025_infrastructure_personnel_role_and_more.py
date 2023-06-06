# Generated by Django 4.2.1 on 2023-05-21 09:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0024_alter_machine_appartient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=16)),
                ('etat', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='role',
            field=models.CharField(choices=[('responsable', 'Responsable'), ('employe', 'Employé')], default='employe', max_length=100),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 11, 20, 35, 349237)),
        ),
        migrations.AddField(
            model_name='personnel',
            name='infrastructure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='computerApp.infrastructure'),
        ),
    ]
