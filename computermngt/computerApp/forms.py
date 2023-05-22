from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine,Personnel, Infrastructure
from datetime import datetime, timedelta
from django.utils import timezone


class AddMachineForm(forms.Form):


   TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('Mac - Run MacOS')),
       ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )
   
   nom = forms.CharField(required=True, label='Nom de la machine')
   maintenanceDate = forms.DateField(initial=timezone.now() + timedelta(weeks=1), widget=forms.DateInput(attrs={'type': 'date'}))
   etat = forms.BooleanField(required=False,label='Etat de la machine')
   mach = forms.ChoiceField(choices=TYPE, required=False)
   appartient = forms.ModelChoiceField(queryset=Personnel.objects.all(), required=True, label='Appartient à')
   infra = forms.ModelChoiceField(queryset=Infrastructure.objects.all(), required=True, label='Dans quel infrastructure')

class DeleteMachineForm(forms.Form):
   machine = forms.ModelChoiceField(queryset=Machine.objects.all(), label='Machine à supprimer')