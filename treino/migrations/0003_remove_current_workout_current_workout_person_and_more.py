# Generated by Django 4.2.3 on 2023-07-30 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
        ('exercicios', '0004_alter_exercise_name_alter_exercise_type'),
        ('treino', '0002_remove_current_workout_matricula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_workout',
            name='current_workout_person',
        ),
        migrations.RemoveField(
            model_name='workout_exercise',
            name='id_exercise',
        ),
        migrations.RemoveField(
            model_name='workout_exercise',
            name='id_workout',
        ),
        migrations.AddField(
            model_name='current_workout',
            name='current_workout',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='cadastro.person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout_exercise',
            name='exercise',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='exercicios.exercise'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout_exercise',
            name='workout',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='treino.workout'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='current_workout',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='treino.workout'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='cadastro.person'),
        ),
        migrations.AlterField(
            model_name='workout_exercise',
            name='reps',
            field=models.IntegerField(default=3, verbose_name='Repetitions'),
        ),
        migrations.AlterField(
            model_name='workout_exercise',
            name='series',
            field=models.IntegerField(default=12, verbose_name='Series'),
        ),
    ]
