from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Workout_exercise,Workout
from cadastro.models import Person

class ExerciciosTreino(ModelForm):
    class Meta:
        model = Workout_exercise
        exclude = ("workout",)
        # fields = "__all__"

        widgets = {
            "exercise":forms.Select(attrs={'class':'form-select'}),
            "series": forms.NumberInput(attrs={'class':'form-control'}),
            "reps": forms.NumberInput(attrs={'class':'form-control'}),
        }

AddExerciciosTreino = inlineformset_factory(
    Workout,
    Workout_exercise,
    form=ExerciciosTreino,
    can_delete=False,
    extra=1,

)

class Treino(ModelForm):
    class Meta:
        model = Workout
        exclude = ("workout_person",)

        widgets = {
            "workout_name":forms.TextInput(attrs={'class':'form-control'}),
            "quantity": forms.NumberInput(attrs={'class':'form-control'}),
            "current_quantity": forms.NumberInput(attrs={'class':'form-control'}),
        }

CadastrarTreino = inlineformset_factory(
    Person,
    Workout,
    form=Treino,
    can_delete=False,
    extra=1,
)
