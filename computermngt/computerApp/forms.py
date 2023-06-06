from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine,Personnel, Infrastructure
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User


class AddMachineForm(forms.Form):

   TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('Mac - Run MacOS')),
       ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )
   
   nom = forms.CharField(required=True, label='Nom de la machine')
   maintenanceDate = forms.DateField(initial=timezone.now() + timedelta(weeks=1), widget=forms.DateInput(attrs={'type': 'date'}))
   etat = forms.BooleanField(required=False, label='Etat de la machine')
   mach = forms.ChoiceField(choices=TYPE, required=False)
   appartient = forms.ModelChoiceField(queryset=Personnel.objects.all(), required=True, label='Appartient à')
   infra = forms.ModelChoiceField(queryset=Infrastructure.objects.all(), required=True, label='Dans quel infrastructure')


class DeleteMachineForm(forms.Form):
   machine = forms.ModelChoiceField(queryset=Machine.objects.all(), label='Machine à supprimer')

class AddUserForm(forms.Form):
   ROLES = (
      ('Resp.', 'Resp.'),
      ('Employé', 'Employé'),
     )
   
   nom = forms.CharField(required=True, label='Nom de l\'utilisateur')
   prenom = forms.CharField(required=True, label='Prénom de l\'utilisateur')
   role = forms.ChoiceField(choices=ROLES, required=False)
   infrastructure = forms.ModelChoiceField(queryset=Infrastructure.objects.all(), required=True, label='Dans quel infrastructure')

class DeleteUserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Personnel.objects.all(), label='Utilisateur à supprimer')

class MachineForm(forms.ModelForm):

    entretien_effectue = forms.BooleanField(required=False)

    class Meta:
        model = Machine
        fields = ['nom', 'infra', 'etat', 'mach', 'maintenanceDate']

    def save(self, commit=True):
        machine = super().save(commit=False)

        entretien_effectue = self.cleaned_data.get('entretien_effectue', False)
        if entretien_effectue:
            machine.maintenanceDate += timedelta(days=7)

        if commit:
            machine.save()

        return machine

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
