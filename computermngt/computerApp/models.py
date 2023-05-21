from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime, timedelta


class Personnel(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    nom = models.CharField(max_length=16,default="")
    prenom = models.CharField(max_length=16,default="")
    email = models.EmailField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = f"{self.prenom.lower()}.{self.nom.lower()}@rtdev.com"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom + " " + self.prenom


class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),

    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=16)
    maintenanceDate = models.DateField(default=datetime.now() + timedelta(weeks=1)) 
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    etat = models.BooleanField(default=False)
    appartient = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    creation = models.DateField(auto_now_add=True)

