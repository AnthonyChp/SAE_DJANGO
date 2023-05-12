from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),

    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=16)
    maintenanceDate = models.DateField(default=datetime.now()) 
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

class Personnel(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True,
        validators=[MaxValueValidator(9999999999999)],
        editable=True)

    nom = models.CharField(
        max_length=16,
        default=""
    )
    prenom = models.CharField(
        max_length=16,
        default=""
    )
    def __str__(self):
        return str(self.id) + " -> " + self.nom + " " + self.prenom