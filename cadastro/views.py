from django.shortcuts import render,redirect
from .models import Person
from .forms import CadastrarPerson, AddressFormSet, PlanFormSet, userForm
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cadastrar(request):
    if request.method == 'POST':

        if Person.objects.filter(cpf=request.POST.get("cpf")).exists():
            messages.error(request, 'Cadastro não foi realizado, esse CPF já conta na base de dados.')

            return redirect('cadastro') 

        person_form = CadastrarPerson(request.POST, request.FILES)
        plan_formset = PlanFormSet(request.POST)
        address_formset = AddressFormSet(request.POST)


        if person_form.is_valid() and plan_formset.is_valid() and address_formset.is_valid():
            person = person_form.save(commit=False)
            if person.profileImage: # save the profile picture
                person.profileImage.name = f"initialProfileImage.{person.profileImage.name.split('.')[-1]}"
            person.save()

            addresses = address_formset.save(commit=False)
            plans = plan_formset.save(commit=False)
            for address in addresses:
                address.address_person = person
                address.save()
            
            for plan in plans:
                plan.plan_person = person
                plan.save()
            
                
            messages.success(request, f'{request.POST.get("name")} está cadastrado, ele(a) já pode frequentar o local. O seu plano estará válido até {request.POST.get("plan-0-expiration_date")}')
        else:
            messages.warning(request, 'Formulário inválido! Tente preencher novamente corretamente.')

        return redirect('cadastro')

    elif request.method == 'GET':
        person_form = CadastrarPerson()
        address_formset = AddressFormSet()
        plan_formset = PlanFormSet()

        context = {
            'person_form':person_form,
            'address_formset':address_formset,
            'plan_formset':plan_formset,
        }

        return render(request, 'cadastrarCliente.html', context=context)

@login_required
def admin(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Trainer")
            user.groups.add(group)

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("menu-principal")
    else:
        form = userForm()

        context = {
                "form":form,
            }

    return render(request, 'register.html', context=context)

