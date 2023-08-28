from django.shortcuts import render,redirect
from cadastro.models import Person
from cadastro.forms import CadastrarPerson, AddressFormSet, PlanFormSet, AlterarAdmin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def usuarios(request):

    people = Person.objects.all()
    search = request.GET.get("q")

    if search:
        people = Person.objects.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(cpf__icontains=search))

    return render(request, 'usuarios.html', context={'people':people})

@login_required
def verDados(request, usuario_id):
    person = Person.objects.get(matricula=usuario_id)
    return render(request, "verDados.html", {'person':person})

@login_required
def alterarDados(request, usuario_id):
    person = Person.objects.get(pk=usuario_id)
    person_form = CadastrarPerson(instance=person)
    address_formset = AddressFormSet(request.POST or None, instance=person)

    if request.method == 'POST':
        person_form = CadastrarPerson(request.POST, request.FILES, instance=person)

        if person_form.is_valid() and address_formset.is_valid():
            
            person_instance = person_form.save(commit=False)  # Save the Person model instance
            if person.profileImage is None:
                person_instance.profileImage.name = f"{person.matricula}.{person.profileImage.name.split('.')[-1]}"
      
            person_instance.save()

            # Link the person to the addresses and save them
            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.address_person = person_instance
                address.save()

            messages.success(request, 'Cadastro atualizado com sucesso! Alterações já realizadas no cadastro do usuário.')
            return redirect('usuarios')

        else:
            if Person.objects.filter(cpf=request.POST.get('cpf')).exists():

                messages.warning(request, 'CPF já cadastrado! Atualização não foi realizada, esse CPF já conta na base de dados.')
                return redirect('usuarios')
        

    return render(request, "alterarDados.html", {'person_form':person_form,'address_formset':address_formset, 'person':person})

@login_required
def excluirUsuario(request, usuario_id):

    person = Person.objects.get(pk=usuario_id)
    
    if request.method == 'POST':
        person.delete()
        messages.success(request, 'Usuário deletado! Todas as informações deste usuário foram deletadas permanentemente.')

        return redirect('usuarios')

@login_required
def renovarAssinatura(request, usuario_id):
    
    person = Person.objects.get(pk=usuario_id)
    plan_formset = PlanFormSet(instance=person)

    if request.method == 'POST':
        plan_formset = PlanFormSet(request.POST, instance=person)

        if plan_formset.is_valid():

            plans = plan_formset.save(commit=False)
            for plan in plans:
                plan.plan_person = person
                plan.save()

            messages.success(request, f"Plano renovado com sucesso, sua nova data de expiração é {request.POST.get('plan-0-expiration_date')}")

            return redirect('usuarios')
        else:
            print(plan_formset.errors, "estou aquiiiii")

    context = {
        "person":person,
        "plan_formset":plan_formset
    }

    return render(request, 'renovarAssinatura.html', context=context)


@login_required
def admin(request):
    return render(request, 'verAdmin.html')

@login_required
def excluirAdmin(request):
    user = request.user
    user.delete()
    return redirect("login")

@login_required
def alterarAdmin(request):
    form = AlterarAdmin(request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Administrador alterado com sucesso!")
            return redirect("admin")
        else:
            messages.error(request, "Erro ao alterar informações do admin! Tente Novamente!")

    context = {
        "form":form,
    }

    return render(request, 'alterarAdmin.html', context=context)

@login_required
def alterarSenhaAdmin(request):
    form = AlterarAdmin(instance=request.user)
    passwordForm = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        passwordForm = PasswordChangeForm(user=request.user, data=request.POST)
        if passwordForm.is_valid():
            passwordForm.save()
            update_session_auth_hash(request, passwordForm.user)

            messages.success(request, "Senha alterada com sucesso!")

            return redirect("alterar-admin")

    context = {
        "form":form,
        "passwordForm":passwordForm,
    }

    return render(request, "alterarSenhaAdmin.html", context=context)