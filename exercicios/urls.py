from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercicios, name='exercicios'),
    path('editar/<int:exercise_id>', views.editar, name='editar-exercicio'),
    path('excluir/<int:exercise_id>', views.removerExercicio, name='excluir-exercicio'),
]