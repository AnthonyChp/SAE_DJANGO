from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine,Personnel, Infrastructure
from .forms import AddMachineForm, DeleteMachineForm
from django.http import JsonResponse

# Create your views here.
def index(request) :
	#On récupère l'ensemble des machines de la database
	machines = Machine.objects.all()
	#Que l'on passe en parametre de la page html via la syntaxe suivante
	context = {
		'machines' : machines,
	}
	return render(request, 'index.html', context)

def menu(request):

	machines = Machine.objects.all()
	users = Personnel.objects.all()
	infras = Infrastructure.objects.all()
	count_user = Personnel.objects.count()
	count_rep = Personnel.objects.filter(role='Resp.').count()
	count_machi = Machine.objects.count()
	count_onMach = Machine.objects.filter(etat=True).count()

	#Que l'on passe en parametre de la page html via la syntaxe suivante
	context = {
		'machines' : machines,
		'users' : users,
		'infras' : infras,
		'count_user' : count_user,
		'count_rep' : count_rep,
		'count_machi' : count_machi,
		'count_onMach' : count_onMach,
	}

	return render(request, 'computerApp/menu.html', context)

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
    
        elif delete_form.is_valid():
            machine_id = delete_form.cleaned_data['machine']
            machine = get_object_or_404(Machine, nom = machine_id)
            machine.delete()
        
        return redirect('menu')
    
    else:
        form = AddMachineForm()
        delete_form = DeleteMachineForm()
    
    context = {
        'form': form,
        'delete_form': delete_form,
        'machines': machines
    }
    
    return render(request, 'computerApp/gerer/gestion_machines.html', context)


def infra_gestion_form(request):
     infras = Infrastructure.objects.all()
     context = {
		'infras': infras
	}
     return render(request, 'computerApp/gerer/gestion_infra.html',context)

def user_gestion_form(request):
     users = Personnel.objects.all()
     context = {
		'users': users
	}
     return render(request, 'computerApp/gerer/gestion_users.html',context)

def ajouter_machine(request):
	machines = Machine.objects.all()
	context = {
		'machines': machines
	}
	return render(request, 'computerApp/gerer/ajouter_machine.html',context)

def machine_list_view(request) :
	machines = Machine.objects.all()
	context = {
		'machines': machines
	}
	return render(request, 'computerApp/machine_list.html',context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request, 'computerApp/machine_detail.html')


def add_machine(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            # Traitement lorsque le formulaire est valide
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        # Création d'une instance du formulaire pour afficher la page initiale
        form = AddMachineForm()
    
    # Le formulaire n'est pas valide ou c'est la première visite à la page, afficher le formulaire
    return render(request, 'menu/test', {'form': form})