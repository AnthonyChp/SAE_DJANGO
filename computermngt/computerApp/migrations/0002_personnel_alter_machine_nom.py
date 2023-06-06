# Generated by Django 4.1.7 on 2023-03-17 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personnel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "secu",
                    models.PositiveIntegerField(
                        editable=False,
                        validators=[django.core.validators.MaxValueValidator(13)],
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="machine",
            name="nom",
            field=models.CharField(max_length=16),
        ),
    ]
