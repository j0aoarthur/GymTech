from django.shortcuts import render,redirect
from cadastro.models import Person
from .models import Workout, Current_workout, Workout_exercise
from exercicios.models import Exercise
from .forms import AddExerciciosTreino,ExerciciosTreino, CadastrarTreino, Treino
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required
def treino(request):

    people = Person.objects.all()
    search = request.GET.get("q")

    if search:
        people = Person.objects.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(cpf__icontains=search))

    context = {
        'people':people
    }
    return render(request, 'treino.html', context=context)

@login_required
def current_workout(person_id):
    person = Person.objects.get(pk=person_id)
    workout = Current_workout.objects.get(current_workout=person)
    return workout.name.workout_name

@login_required
def verTreino(request,usuario_id, workout=None):
        
    person = Person.objects.get(pk=usuario_id)

    if workout == None:
        default_workout = Current_workout.objects.get(current_workout_person=person)
        workout = default_workout.name.workout_name
    
    formset = AddExerciciosTreino()
    workouts = Workout.objects.filter(workout_person=person)
    curr_workout = workouts.get(workout_name=workout)
    workout_exercises = curr_workout.exercises.all()
    treino_formset = CadastrarTreino()

    workouts_name = list(workouts.values_list('workout_name', flat=True))


    if request.method == 'POST':
        formset = AddExerciciosTreino(request.POST)

        if formset.is_valid():

            exercises = formset.save(commit=False)
            for exercise in exercises:
                exercise.workout = curr_workout
                exercise.save()
            
            return redirect('ver-treino', usuario_id, workout)

    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":workout_exercises,
        "treino_formset":treino_formset,
        "workouts_name":workouts_name,

    }
    return render(request, 'perfilTreino.html', context=context)

@login_required
def alterarExercicio(request, usuario_id, edit_workout, exercise_id):

    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name__iexact=edit_workout)
    edit_exercise = Workout_exercise.objects.get(workout=curr_workout, id=exercise_id)
    all_exercises = curr_workout.exercises.all()

    formset = ExerciciosTreino(request.POST or None, instance=edit_exercise)

    if formset.is_valid():
        formset.save()
        return redirect('ver-treino', usuario_id, edit_workout)

    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":all_exercises,
        "exercise":edit_exercise
    }

    return render(request, 'editar_modal_exercicio.html', context=context)

@login_required
def excluirExercicioTreino(request, usuario_id, edit_workout, exercise_id):

    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name__iexact=edit_workout)
    exercise = Workout_exercise.objects.get(workout=curr_workout, id=exercise_id)
    
    exercise.delete()

    return redirect('ver-treino', usuario_id, edit_workout)

@login_required
def criarTreino(request, usuario_id):

    person = Person.objects.get(pk=usuario_id)
    workouts = Workout.objects.filter(workout_person=person)

    if request.method == 'POST':

        if workouts.filter(workout_name__iexact=request.POST.get("workouts-0-workout_name"), workout_person=person).exists():
            messages.warning(request, 'Nome de treino não disponível! Já existe um treino com esse mesmo nome, tente criar um treino com um nome diferente.')

            return redirect('ver-treino', usuario_id)

        formset = CadastrarTreino(request.POST)

        if formset.is_valid():
            treinos = formset.save(commit=False)
            for treino in treinos:
                treino.workout_person = person
                treino.save()

                if workouts.count() == 1:
                    current_workout = Current_workout(current_workout_person=person, name=treino)
                    current_workout.save()

            return redirect('ver-treino', usuario_id)
        else:
            print(formset.errors)
        
    elif request.method == 'GET':
        if workouts.count() == 0:
            treino_formset = CadastrarTreino()

            context = {
                'person':person,
                "treino_formset":treino_formset,
            }

            return render(request, 'criarTreino.html', context=context)

def testando(request, usuario_id):

    person = Person.objects.get(pk=usuario_id)
    workouts = Workout.objects.filter(workout_person=person)

    for x,workout in enumerate(workouts):
        print(workout, x)

    return render(request, 'teste2.html')


@login_required
def alterarTreino(request, usuario_id, workout):
    formset = AddExerciciosTreino()
    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name__iexact=workout)
    workout_exercises = curr_workout.exercises.all()

    treino = Treino(request.POST or None, instance=curr_workout)

    if request.method == "POST":

        if Workout.objects.filter(workout_name__iexact=request.POST.get("workouts-0-workout_name"), workout_person=person).exists():
            messages.warning(request, 'Nome de treino não disponível! Já existe um treino com esse mesmo nome, tente criar um treino com um nome diferente.')

            return redirect('ver-treino', usuario_id)

        if treino.is_valid():
            treino.save()
            return redirect("ver-treino", usuario_id=usuario_id, workout=curr_workout.workout_name)
    
    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":workout_exercises,
        "treino_formset":treino,
    }

    return render(request, "alterarTreino.html", context=context)

@login_required
def apagarTreino(request, usuario_id, workout):
    person = Person.objects.get(pk=usuario_id)
    workouts_person = Workout.objects.filter(workout_person=person)
    workout_del = Workout.objects.get(workout_person=person, workout_name=workout)
    person_current_workout = Current_workout.objects.get(current_workout_person=person)


    if workout_del.workout_name == person_current_workout.name.workout_name and workouts_person.count() > 1:
        workout_del.delete()
        current_workout = Current_workout(current_workout_person=person, name=workouts_person.first())
        current_workout.save()
    else:
        workout_del.delete()


    return redirect('treinos')

@login_required
def current_workout(person_id):
    person = Person.objects.get(pk=person_id)
    workout = Current_workout.objects.get(current_workout=person)
    return workout.name.workout_name

@login_required
def verTreino(request,usuario_id, workout=None):
        
    person = Person.objects.get(pk=usuario_id)

    if workout == None:
        default_workout = Current_workout.objects.get(current_workout_person=person)
        workout = default_workout.name.workout_name
    
    formset = AddExerciciosTreino()
    workouts = Workout.objects.filter(workout_person=person).order_by("workout_name")
    curr_workout = workouts.get(workout_name=workout)
    workout_exercises = curr_workout.exercises.all()
    treino_formset = CadastrarTreino()

    workouts_name = list(workouts.values_list('workout_name', flat=True))


    if request.method == 'POST':
        formset = AddExerciciosTreino(request.POST)

        if formset.is_valid():

            exercises = formset.save(commit=False)
            for exercise in exercises:
                exercise.workout = curr_workout
                exercise.save()
            
            return redirect('ver-treino', usuario_id, workout)

    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":workout_exercises,
        "treino_formset":treino_formset,
        "workouts_name":workouts_name,

    }
    return render(request, 'perfilTreino.html', context=context)

@login_required
def alterarExercicio(request, usuario_id, edit_workout, exercise_id):

    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name=edit_workout)
    edit_exercise = Workout_exercise.objects.get(workout=curr_workout, id=exercise_id)
    all_exercises = curr_workout.exercises.all()

    formset = ExerciciosTreino(request.POST or None, instance=edit_exercise)

    if formset.is_valid():
        formset.save()
        return redirect('ver-treino', usuario_id, edit_workout)

    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":all_exercises,
        "exercise":edit_exercise
    }

    return render(request, 'editar_modal_exercicio.html', context=context)

@login_required
def excluirExercicioTreino(request, usuario_id, edit_workout, exercise_id):

    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name=edit_workout)
    exercise = Workout_exercise.objects.get(workout=curr_workout, id=exercise_id)
    
    exercise.delete()

    return redirect('ver-treino', usuario_id, edit_workout)

@login_required
def criarTreino(request, usuario_id):

    person = Person.objects.get(pk=usuario_id)
    workouts = Workout.objects.filter(workout_person=person)

    if request.method == 'POST':

        if workouts.filter(workout_name=request.POST.get("workouts-0-workout_name"), workout_person=person).exists():
            messages.warning(request, 'Nome de treino não disponível! Já existe um treino com esse mesmo nome, tente criar um treino com um nome diferente.')

            return redirect('ver-treino', usuario_id)

        formset = CadastrarTreino(request.POST)

        if formset.is_valid():
            treinos = formset.save(commit=False)
            for treino in treinos:
                treino.workout_person = person
                treino.save()

                if workouts.count() == 1:
                    current_workout = Current_workout(current_workout_person=person, name=treino)
                    current_workout.save()

            return redirect('ver-treino', usuario_id)
        else:
            print(formset.errors)
        
    elif request.method == 'GET':
        if workouts.count() == 0:
            treino_formset = CadastrarTreino()

            context = {
                'person':person,
                "treino_formset":treino_formset,
            }

            return render(request, 'criarTreino.html', context=context)

def testando(request, usuario_id):

    person = Person.objects.get(pk=usuario_id)
    workouts = Workout.objects.filter(workout_person=person)

    for x,workout in enumerate(workouts):
        print(workout, x)



    return render(request, 'teste2.html')

@login_required
def alterarTreino(request, usuario_id, workout):
    formset = AddExerciciosTreino()
    person = Person.objects.get(pk=usuario_id)
    curr_workout = Workout.objects.get(workout_person=person, workout_name=workout)
    workout_exercises = curr_workout.exercises.all()
    treino_formset = CadastrarTreino()

    treino = Treino(request.POST or None, instance=curr_workout)

    if request.method == "POST":

        if Workout.objects.filter(workout_name=request.POST.get("workouts-0-workout_name"), workout_person=person).exists():
            messages.warning(request, 'Nome de treino não disponível! Já existe um treino com esse mesmo nome, tente criar um treino com um nome diferente.')

            return redirect('ver-treino', usuario_id)

        if treino.is_valid():
            treino.save()
            return redirect("ver-treino", usuario_id=usuario_id, workout=curr_workout.workout_name)
    
    context = {
        "exercise_formset":formset,
        'person':person,
        'workout':curr_workout,
        "workout_exercises":workout_exercises,
        "treino_formset":treino,
    }

    return render(request, "alterarTreino.html", context=context)

@login_required
def redirecionarTreino(request, usuario_id):
    return redirect("ver-treino", usuario_id=usuario_id, workout=request.GET.get("workout_name"))

@login_required
def treinar(request,usuario_id, workout_name):

    person = Person.objects.get(pk=usuario_id)
    workouts = Workout.objects.filter(workout_person=person).order_by("workout_name")

    workout_selected = Workout.objects.get(workout_person=person, workout_name=workout_name)
    workout_selected.current_quantity += 1
    workout_selected.save()

    current_workout = Current_workout.objects.get(current_workout_person=person)

    current_workout_index = list(workouts).index(workout_selected)

    new_index = (current_workout_index + 1) % workouts.count()

    new_workout = workouts[new_index]

    current_workout.name = new_workout
    current_workout.save()

    return redirect("ver-treino", usuario_id)

    

    



            


    




