from django import forms
from django.forms import ModelForm
from .models import Exercise
from cadastro.forms import CustomSelect

class CadastrarExercise(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', 'required':''}),
            "type": CustomSelect()
        }