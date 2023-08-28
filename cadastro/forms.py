from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Person, addressPerson, Plan
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CadastrarPerson(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'class':'input-material', 'id':"name"}),
            "email": forms.EmailInput(attrs={'class':'input-material', 'id':"email"}),
            "cpf": forms.TextInput(attrs={'class':'input-material', 'id':"cpf"}),
            "birthDate": forms.DateInput(attrs={'class':'input-material', 'id':"birthDate"}),
            "phone": forms.TextInput(attrs={'class':'input-material', 'id':"phone"}),
            "whatsapp": forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': "wpp"}),
        }


class CustomSelect(forms.Select):
    def __init__(self, attrs=None, choices=(), *args, **kwargs):
        attrs = attrs or {}
        attrs['class'] = 'mt-2 form-select'  # Add your desired class here
        attrs['id'] = 'plan'
        attrs['required'] = ''
        super().__init__(attrs, choices, *args, **kwargs)

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)

        # Add class to the 'Other' option
        if option['value'] == '':
            option['attrs']['readonly'] = ''
            option['attrs']['disabled'] = ''
            
        return option

class CadastrarPlan(ModelForm):
    class Meta:
        model = Plan
        exclude = ['signature_date']

        widgets = {
            "plan_name": CustomSelect(),
            "expiration_date": forms.TextInput(attrs={'class':'input-material' , 'id':'dueDateLabel', 'readonly':'', 'value':' '}),
        }


class CadastrarAddressPerson(ModelForm):
    class Meta:
        model = addressPerson
        fields = "__all__"

        widgets = {
            "cep": forms.TextInput( attrs={'class':'input-material' , 'id':'cep'}),
            "street": forms.TextInput(attrs={'class':'input-material' , 'id':'street', 'value':' ', 'readonly':''}),
            "neighborhood": forms.TextInput(attrs={'class':'input-material' , 'id':'neighborhood', 'value':' ', 'readonly':''}),
            "city": forms.TextInput(attrs={'class':'input-material' , 'id':'city', 'value':' ', 'readonly':''}),
            "state": forms.TextInput(attrs={'class':'input-material' , 'id':'state', 'value':' ', 'readonly':''}),
            "number": forms.NumberInput(attrs={'class':'input-material' , 'id':'num'}),
            "complement": forms.TextInput(attrs={'class':'input-material' , 'id':'complement'}),
        }

AddressFormSet = inlineformset_factory(
        Person,  # Parent model (Person)
        addressPerson,  # Child model (addressPerson)
        form=CadastrarAddressPerson,
        can_delete=False,
        extra=1,
    )


PlanFormSet = inlineformset_factory(
    Person,
    Plan,
    form = CadastrarPlan,
    can_delete=False,
    extra=1,
)

class userForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=False, help_text="Optional..")
    last_name = forms.CharField(max_length=40, required=False, help_text="Optional..")


    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name")

        widgets = {
            "username": forms.TextInput(attrs={'class':'input-material'}),
            "first_name": forms.TextInput(attrs={'class':'input-material'}),
            "last_name": forms.TextInput(attrs={'class':'input-material'}),
            "password1": forms.TextInput(attrs={'class':'input-material'}),
            "password2": forms.TextInput(attrs={'class':'input-material'}),
        }
    
class AlterarAdmin(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

        widgets = {
            "username": forms.TextInput(attrs={'class':'input-material'}),
            "first_name": forms.TextInput(attrs={'class':'input-material'}),
            "last_name": forms.TextInput(attrs={'class':'input-material'}),
        }

class AlterarSenhaAdmin(PasswordChangeForm):
    class Meta:
        model = User
        fields= "__all__"

        widgets = {
            "old_password": forms.PasswordInput(attrs={'class':'form-control'}),
            "new_password1": forms.PasswordInput(attrs={'class':'form-control'}),
            "new_password2": forms.PasswordInput(attrs={'class':'form-control'}),
        }

# AddressFormSet = inlineformset_factory(
#         Person,  # Parent model (Person)
#         addressPerson,  # Child model (addressPerson)
#         fields = "__all__",

#         widgets = {
#             "cep": forms.TextInput( attrs={'class':'input-material' , 'id':'cep'}),
#             "street": forms.TextInput(attrs={'class':'input-material' , 'id':'street', 'value':' '}),
#             "neighborhood": forms.TextInput(attrs={'class':'input-material' , 'id':'neighborhood', 'value':' '}),
#             "city": forms.TextInput(attrs={'class':'input-material' , 'id':'city', 'value':' '}),
#             "state": forms.TextInput(attrs={'class':'input-material' , 'id':'state', 'value':' '}),
#             "number": forms.NumberInput(attrs={'class':'input-material' , 'id':'num'}),
#             "complement": forms.TextInput(attrs={'class':'input-material' , 'id':'complement'}),
#         },
#         can_delete=False,  # Set to True if you want to allow deleting addresses
#         extra=1,  # Number of extra address forms to display
#     )
# name = models.CharField('Nome', max_length=100)
# email = models.EmailField('E-mail')
# cpf = models.CharField('CPF', max_length=14, unique=True)
# birthDate = models.CharField('Data de nascimento', max_length=10)
# phone = models.CharField('Telefone', max_length=15)
# whatsapp = models.BooleanField('Possui whatsapp?',default=True)
# signature_date = models.DateField('Data de criação', auto_now=True)
# expiration_date = models.DateField('Data de expiração')


# cep = onlyNum(request.POST.get('cep'))
# street = request.POST.get('street')
# neighborhood = request.POST.get('neighborhood')
# city = request.POST.get('city')
# state = request.POST.get('state')
# number = request.POST.get('num')
# complement = request.POST.get('complement')

# name = request.POST.get('name')
# email = request.POST.get('email')
# cpf = onlyNum(request.POST.get('cpf'))

# birthday = request.POST.get('birthday')
# phone = onlyNum(request.POST.get('phone'))

# if request.POST.get('wpp'):
#     whatsapp = True
# else:
#     whatsapp = False

# plan = request.POST.get('plan')
# dueDate = getDueDate(plan)
