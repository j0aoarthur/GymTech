# Generated by Django 4.2.3 on 2023-07-30 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treino', '0003_remove_current_workout_current_workout_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_exercises', to='treino.workout'),
        ),
    ]