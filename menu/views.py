from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from cadastro.models import Person
from datetime import datetime, date
from django.utils import timezone


# Create your views here.

@login_required
def main(request):

    people = Person.objects.all().order_by("-plan__signature_date","-matricula")

    expired_count = 0
    for person in people:
        if person.plan.expiration_date < timezone.now().date():
            expired_count += 1

    context = {
        "people":people[:3],
        "people_count":people.count(),
        "expired_count":expired_count,


    }
    return render(request, 'index.html', context=context)

def login_func(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("menu-principal")
            else:
                messages.error(request, "Usuário ou senha estão incorretos")

        else:
            messages.error(request, "Usuário ou senha não inserido corretamente")

    return render(request, "login.html", {"form":form})

@login_required
def logout_func(request):
    logout(request)
    return redirect("login")
