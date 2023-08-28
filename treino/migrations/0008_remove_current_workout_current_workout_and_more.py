# Generated by Django 4.2.3 on 2023-08-01 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
        ('treino', '0007_alter_workout_exercise_reps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_workout',
            name='current_workout',
        ),
        migrations.AddField(
            model_name='current_workout',
            name='current_workout_person',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='current_workout', to='cadastro.person'),
            preserve_default=False,
        ),
    ]
