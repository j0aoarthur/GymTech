from django.contrib import admin
from .models import Workout, Workout_exercise,Current_workout

# Register your models here.

admin.site.register(Workout)
admin.site.register(Current_workout)

@admin.register(Workout_exercise)
class Workout_exerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout', 'exercise')