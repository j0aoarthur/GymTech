from django.shortcuts import render,redirect
from .models import Exercise
from .forms import CadastrarExercise
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def exercicios(request):

    exercicios = Exercise.objects.all()
    if request.method == 'POST':
        form = CadastrarExercise(request.POST)


        if exercicios.filter(name=request.POST.get("name")).exists():
            messages.error(request, 'Exercício não cadastrado! Esse nome já se encontra cadastrado na base de dados. Tente procurár-lo na lista de exercicios ou utilize um nome diferente.')

            return redirect('exercicios')

        if form.is_valid():
            form.save()
            
            messages.success(request, 'Exercício cadastrado com sucesso! O exercício já está disponível para ser selecionado e utilizado.')

            return redirect('exercicios')

    elif request.method == 'GET':
        form = CadastrarExercise()

        search = request.GET.get("q")

        if search:
            exercicios = Exercise.objects.filter(name__icontains=search)

        context = {
            'exercicios':exercicios,
            'form':form,
        }

        return render(request, 'exercicios.html' ,context=context)

@login_required
def editar(request, exercise_id):

    exercicios = Exercise.objects.all()
    exercicio = exercicios.get(pk=exercise_id)
    form = CadastrarExercise(request.POST or None, instance=exercicio)

    if form.is_valid():
        form.save()

        return redirect('exercicios')
    
    context = {
        'update_form':form,
        'exercicio':exercicio,
        'exercicios':exercicios,
    }

    return render(request, 'editar_modal.html' ,context=context)
        
@login_required
def removerExercicio(request, exercise_id):

    exercicio = Exercise.objects.get(id=exercise_id)
    exercicios = Exercise.objects.all()
    
    if request.method == 'POST':
        exercicio.delete()
        return redirect('exercicios')
    elif request.method == 'GET':

        context = {
            'excluir_exercicio':True,
            'exercicio':exercicio,
            'exercicios':exercicios
        }

        return render(request, 'confirmacao_delete.html', context=context)
