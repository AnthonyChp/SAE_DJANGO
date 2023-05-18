from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine
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
	machines_count = Machine.objects.count()
	#Que l'on passe en parametre de la page html via la syntaxe suivante
	context = {
		'machines' : machines,
		'machines_count': machines_count
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
		form_1 = AddMachineForm(request.POST or None)
		if form_1.is_valid():
			new_machine = Machine(nom=form_1.cleaned_data['nom'])
			new_machine.save()
			return redirect('machines')

	else :
		form_2 = AddMachineForm()
		context = {'form' : form_2}
		return render(request,'computerApp/machine_add.html', context)