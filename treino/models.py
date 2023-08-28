from django.db import models
from cadastro.models import Person
from exercicios.models import Exercise
from django.core.validators import MaxLengthValidator

# Create your models here.

class Workout(models.Model):
    workout_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='workouts')
    workout_name = models.CharField('Nome do treino', max_length=1, validators=[MaxLengthValidator(limit_value=1)])
    quantity = models.IntegerField('Quantidade de vezes')
    current_quantity = models.IntegerField('Atual quantidade',default=0, blank=True)

    def __str__(self):
        return self.workout_name + ' - ' + self.workout_person.name
    
    def save(self, *args, **kwargs):
        self.workout_name = self.workout_name.upper()
        super(Workout, self).save(*args, **kwargs)
    
class Workout_exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    series = models.IntegerField('Series', default=3)
    reps = models.IntegerField('Repetições', default=12)

    def __str__(self):
        return self.workout.workout_name + ' - ' + self.exercise.name + ' - ' + self.workout.workout_person.name

class Current_workout(models.Model):
    current_workout_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="current_workout")
    name = models.OneToOneField(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.workout_name + ' - ' + self.current_workout_person.name + "'s current workout"
    

    