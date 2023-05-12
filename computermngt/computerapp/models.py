from datetime import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Machine(models.Model):

    TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('MAc - Run MacOS')),
       ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = timezone.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')