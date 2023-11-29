from django import forms
from django.forms import ModelForm
from .models import Exercise

class CadastrarExercise(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', 'required':''}),
            "type": forms.Select(attrs={'class':'mt-2 form-select', 'id':'plan', 'required':''}),
        }