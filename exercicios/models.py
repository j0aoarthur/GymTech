from django.db import models

# Create your models here.

class Exercise(models.Model):
    type_choices = (
        ('', 'Tipos'),
        ('Máquina', 'Máquina'),
        ('Corporal', 'Corporal'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome', max_length=50)
    type = models.CharField('Tipo', max_length=8, choices=type_choices)

    def __str__(self):
        return self.name

