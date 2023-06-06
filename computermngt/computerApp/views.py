from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine,Personnel, Infrastructure
from .forms import AddMachineForm, DeleteMachineForm, AddUserForm, DeleteUserForm, MachineForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date

# Create your views here.
def index(request) :
	#On récupère l'ensemble des machines de la database
	machines = Machine.objects.all()
	#Que l'on passe en parametre de la page html via la syntaxe suivante
	context = {
		'machines' : machines,
	}
	return render(request, 'index.html', context)

machine_crea = False 
machine_del = False 
user_crea = False 
user_del = False 
co_wrong = False

@login_required
def menu(request):
    machines = Machine.objects.all()
    users = Personnel.objects.all()
    infras = Infrastructure.objects.all()
    count_user = Personnel.objects.count()
    count_rep = Personnel.objects.filter(role='Resp.').count()
    count_machi = Machine.objects.count()
    count_onMach = Machine.objects.filter(etat=True).count()

    # Récupérer la valeur des variables depuis la session
    machine_crea = request.session.get('machine_crea', False)
    machine_del = request.session.get('machine_del', False)
    user_crea = request.session.get('user_crea', False)
    user_del = request.session.get('user_del', False)

    # Réinitialiser les variable à False dans la session
    request.session['machine_crea'] = False
    request.session['machine_del'] = False
    request.session['user_crea'] = False
    request.session['user_del'] = False


    context = {
        'machines': machines,
        'users': users,
        'infras': infras,
        'count_user': count_user,
        'count_rep': count_rep,
        'count_machi': count_machi,
        'count_onMach': count_onMach,
        'machine_crea': machine_crea,
        'machine_del' : machine_del,
        'user_crea': user_crea,
        'user_del' : user_del,
    }

    if request.user.groups.filter(name='full_access').exists():
        return render(request, 'computerApp/menu.html', context)
    else :
        return render(request, 'computerApp/gerer/error.html', context)

@login_required
def machine_gestion_form(request):
    machines = Machine.objects.all()

    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        delete_form = DeleteMachineForm(request.POST)
        
        if form.is_valid():
            nom = form.cleaned_data['nom']
            maintenance_date = form.cleaned_data['maintenanceDate']
            etat = form.cleaned_data['etat']
            mach = form.cleaned_data['mach']
            appartient = form.cleaned_data['appartient']
            infra = form.cleaned_data['infra']
            
            new_machine = Machine(
                nom=nom,
                maintenanceDate=maintenance_date,
                etat=etat,
                mach=mach,
                appartient=appartient,
                infra=infra,
            )

            new_machine.save()
            form = AddMachineForm()
            request.session['machine_crea'] = True
    
        elif delete_form.is_valid():
            machine_id = delete_form.cleaned_data['machine']
            machine = get_object_or_404(Machine, nom=machine_id)
            machine.delete()
            request.session['machine_del'] = True
        
        return redirect('menu')
    
    else:
        form = AddMachineForm()
        delete_form = DeleteMachineForm()
    
    context = {
        'form': form,
        'delete_form': delete_form,
        'machines': machines,
        'machine_crea': request.session.get('machine_crea', False),
        'machine_del': request.session.get('machine_del', False),
    }
    
    return render(request, 'computerApp/gerer/gestion_machines.html', context)

@login_required
def user_gestion_form(request):
     users = Personnel.objects.all()

     if request.method == 'POST':
        form = AddUserForm(request.POST)
        delete_form = DeleteUserForm(request.POST)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            role = form.cleaned_data['role']
            infrastructure = form.cleaned_data['infrastructure']
           
            new_user = Personnel(
                nom=nom,
                prenom=prenom,
                role=role,
                infrastructure=infrastructure,
            )

            new_user.save()
            form = AddUserForm()
            request.session['user_crea'] = True

        elif delete_form.is_valid():
            user = delete_form.cleaned_data['user']
            user.delete()
            request.session['user_del'] = True
        
        return redirect('menu')
    
     else:
        form = AddUserForm()
        delete_form = DeleteUserForm()
    
     context = {
		'users': users,
        'form' : form,
        'delete_form': delete_form,
        'user_crea': request.session.get('user_crea', False),
        'user_del': request.session.get('user_del', False),
	}
     if request.user.groups.filter(name='full_access').exists():
        return render(request, 'computerApp/gerer/gestion_users.html',context)
     else:
        return render(request, 'computerApp/gerer/error.html', context)

out_check = False

@login_required
def infra_gestion_form(request):
     out_check = request.session.get('out_check', False)

     request.session['out_check'] = False

     infras = Infrastructure.objects.all()
     context = {
		'infras': infras,
        'out_check' : out_check,
	}
     if request.user.groups.filter(name='full_access').exists():
        return render(request, 'computerApp/gerer/gestion_infra.html',context)
     else:
        return render(request, 'computerApp/gerer/error.html', context)

entretien_check = False
date_check = False

@login_required
def machines(request):

    # Récupérer la valeur des variables depuis la session
    entretien_check = request.session.get('entretien_check', False)
    date_check = request.session.get('date_check', False)

    machines = Machine.objects.all().order_by('maintenanceDate')

    request.session['date_check'] = False
    request.session['entretien_check'] = False

    form = MachineForm()  # Créez une instance du formulaire en dehors du bloc if
    
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'machines': machines,
        'form': form,
        'date_check': date_check,
        'entretien_check' : entretien_check,
    }
    
    return render(request, 'computerApp/gerer/machines.html', context)

def login_view(request):

    co_wrong = request.session.get('co_wrong', False)

    request.session['co_wrong'] = False

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../menu/profils')  # Redirigez l'utilisateur vers la page menu après la connexion
            else:
                form.add_error(None, 'Identifiant ou mot de passe incorrect.')
                request.session['co_wrong'] = True
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'co_wrong' : co_wrong,
        'co_wrong': request.session.get('co_wrong', False),
    }
    
    return render(request, 'computerApp/login.html', context)

@login_required
def profils(request):
    user = request.user
    user_attributes = user.__dict__

    context = {
        'user_attributes': user_attributes,
    }

    return render(request, 'computerApp/gerer/profils.html', context)

@login_required
def changement_statut(request, machine_id):
    # Récupérer la machine correspondant à l'ID
    try:
        machine = Machine.objects.get(id=machine_id)
    except Machine.DoesNotExist:
        # Gérer le cas où la machine n'existe pas
        return render(request, 'computerApp/machine_not_found.html')

    # Inverser le statut de la machine
    machine.etat = not machine.etat
    machine.save()
    request.session['date_check'] = True

    context = {
        'machines': machines,
        'date_check': request.session.get('date_check', False),
    }

    # Rediriger vers la page des machines
    return redirect('machines')
    

@login_required
def changement_entretient(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)

    if request.method == 'POST':
        description = request.POST.get('description', '') # Récupérer la valeur de la description depuis la requête POST
        machine.description = description

        machine.maintenanceDate = timezone.now() + timezone.timedelta(weeks=1)
        machine.utilisateur_mise_a_jour = request.user
        machine.date_mise_a_jour = timezone.now()
        machine.save()
        request.session['entretien_check'] = True
    machines = Machine.objects.all()
    context = {
        'machines': machines,
        'entretien_check': request.session.get('entretien_check', False),
    }

    return redirect('machines')

@login_required
def changement_statut_infra(request, infra_id):
    # Récupérer la machine correspondant à l'ID
    try:
        infras = Infrastructure.objects.get(id=infra_id)
    except Machine.DoesNotExist:
        # Gérer le cas où la machine n'existe pas
        return render(request, 'computerApp/machine_not_found.html')

    # Inverser le statut de la machine
    infras.etat = not infras.etat
    infras.save()

    request.session['out_check'] = True

    context = {
        'infras': infras,
        'out_check': request.session.get('out_check', False),
    }

    # Rediriger vers la page des machines
    return redirect('gestion-infra')


