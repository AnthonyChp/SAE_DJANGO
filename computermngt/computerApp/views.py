from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine,Personnel, Infrastructure
from .forms import AddMachineForm, DeleteMachineForm, AddUserForm, DeleteUserForm, MachineForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

    return render(request, 'computerApp/menu.html', context)
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
                infra=infra
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
     
     return render(request, 'computerApp/gerer/gestion_users.html',context)
@login_required
def infra_gestion_form(request):
     infras = Infrastructure.objects.all()
     context = {
		'infras': infras
	}
     return render(request, 'computerApp/gerer/gestion_infra.html',context)
@login_required
def machines(request):

    form = MachineForm()  # Créez une instance du formulaire en dehors du bloc if
    
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
    
    machines = Machine.objects.all()
    
    context = {
        'machines': machines,
        'form': form,
    }
    
    return render(request, 'computerApp/gerer/machines.html', context)
@login_required
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
                return redirect('menu')  # Redirigez l'utilisateur vers la page menu après la connexion
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

