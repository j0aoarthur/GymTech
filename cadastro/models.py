from django.db import models

# Create your models here.
class Person(models.Model):
    matricula = models.AutoField('Matrícula', primary_key=True)
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    cpf = models.CharField('CPF', max_length=14, unique=True)
    birthDate = models.DateField('Data de nascimento')
    phone = models.CharField('Telefone', max_length=15)
    whatsapp = models.BooleanField('Possui whatsapp?', default=True)
    profileImage = models.ImageField('Imagem de perfil', upload_to ="profileImages/", blank=True)
    
    def __str__(self):
        return str(self.matricula) + ' - ' + self.name

class addressPerson(models.Model):
    address_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='address')
    cep = models.CharField('CEP', max_length=9)
    street = models.CharField('Rua', max_length=30)
    neighborhood = models.CharField('Bairro', max_length=30)
    city = models.CharField('Cidade', max_length=30)
    state = models.CharField('Estado', max_length=2)
    number = models.IntegerField('Número')
    complement = models.CharField('Complemento', max_length=30)


    def __str__(self):
        return self.address_person.name + "'s address"
    
class Plan(models.Model):
    plan_choices = (
    ('', 'Planos'),
    ('Mensal', 'Mensal'),
    ('Trimestral', 'Trimestral'),
    ('Semestral', 'Semestral'),
    ('Anual', 'Anual'),
)
    plan_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="plan")
    plan_name = models.CharField('Nome do plano',choices=plan_choices, max_length=10)
    signature_date = models.DateField('Data de assinatura', auto_now=True)
    expiration_date = models.DateField('Data de expiração')

    def __str__(self):
        return self.plan_person.name + "'s plan"




