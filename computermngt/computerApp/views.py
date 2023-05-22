from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine,Personnel
from .forms import AddMachineForm

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
	nb_mach = Machine.objects.count()
	users = Personnel.objects.all()
	#Que l'on passe en parametre de la page html via la syntaxe suivante
	context = {
		'machines' : machines,
		'users' : users
	}

	return render(request, 'computerApp/menu.html', context)

def test(request):
	machines = Machine.objects.all()
	context = {
		'machines': machines
	}
	return render(request, 'computerApp/gerer/test.html',context)

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

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            maintenance_date = form.cleaned_data['maintenanceDate']
            etat = form.cleaned_data['etat']
            mach = form.cleaned_data['mach']
            appartient = form.cleaned_data['appartient']
            
            new_machine = Machine(
                nom=nom,
                maintenanceDate=maintenance_date,
                etat=etat,
                mach=mach,
                appartient=appartient
            )
            new_machine.save()
            form = AddMachineForm()
            return redirect('menu')
    else:
        form = AddMachineForm()
    
    return render(request, 'computerApp/machine_add.html', {'form': form})
