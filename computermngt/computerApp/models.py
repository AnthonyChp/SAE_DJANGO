from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Infrastructure(models.Model):
    nom = models.CharField(max_length=16)
    etat = models.BooleanField(default=False)
    maintenanceDate = models.DateField(default=timezone.now)
    crea = models.DateField(default=timezone.now, editable=False)
    description = models.TextField(default="/")
    utilisateur_mise_a_jour_infra = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updates')
    date_mise_a_jour_infra = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='infrastructures')

    def __str__(self):
        return self.nom

class Personnel(models.Model):
    ROLES = (
        ('Resp.', 'Resp.Paris'),
        ('Resp.', 'Resp.Poitiers'),
        ('Resp.', 'Resp.Marseille'),
        ('Resp.', 'Resp.Lyon'),
        ('Employé', 'Employé'),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=16, default="")
    prenom = models.CharField(max_length=16, default="")
    email = models.EmailField(editable=False, blank=True)
    role = models.CharField(max_length=100, choices=ROLES, default='Employé')
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.SET_NULL, null=True, blank=True, related_name='personnel')
    crea = models.DateField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = f"{self.prenom.lower()}.{self.nom.lower()}@rtdev.com"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom + " " + self.prenom

class Update(models.Model):
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE, related_name='updates')
    utilisateur_mise_a_jour = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return f"Mise à jour de l'infrastructure {self.infrastructure.nom}"

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
    appartient = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=False)
    creation = models.DateField(auto_now_add=True)
    infra = models.ForeignKey(Infrastructure, on_delete=models.SET_NULL, null=True, blank=False)

    utilisateur_mise_a_jour = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    description = models.TextField(default="/")

    def save(self, *args, **kwargs):
        self.date_mise_a_jour = datetime.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nom

