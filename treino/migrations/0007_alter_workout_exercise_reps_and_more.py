# Generated by Django 4.2.3 on 2023-07-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treino', '0006_alter_workout_exercise_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_exercise',
            name='reps',
            field=models.IntegerField(default=12, verbose_name='Repetições'),
        ),
        migrations.AlterField(
            model_name='workout_exercise',
            name='series',
            field=models.IntegerField(default=3, verbose_name='Series'),
        ),
    ]
