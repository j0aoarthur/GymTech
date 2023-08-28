# Generated by Django 4.2.3 on 2023-07-29 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercicios', '0002_rename_tipo_exercise_type'),
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=1, verbose_name='Nome do treino')),
                ('quantity', models.IntegerField(verbose_name='Quantidade de vezes')),
                ('current_quantity', models.IntegerField(default=0, verbose_name='Atual quantidade')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.person')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(default=0, verbose_name='Series')),
                ('reps', models.IntegerField(default=0, verbose_name='Repetitions')),
                ('id_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercicios.exercise')),
                ('id_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treino.workout')),
            ],
        ),
        migrations.CreateModel(
            name='Current_workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.person')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treino.workout')),
            ],
        ),
    ]