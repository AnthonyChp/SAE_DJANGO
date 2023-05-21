# Generated by Django 4.2.1 on 2023-05-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0010_machine_appartient_nom_machine_appartient_prenom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='appartient_nom',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='appartient_prenom',
        ),
        migrations.AddField(
            model_name='machine',
            name='appartient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='computerApp.personnel'),
        ),
    ]