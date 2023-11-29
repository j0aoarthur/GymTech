from django.urls import path
from . import views

urlpatterns = [
    path('', views.treino, name='treinos'),
    path('criarTreino/<int:usuario_id>', views.criarTreino, name='criar-treino'),
    path('verTreino/<int:usuario_id>/', views.verTreino, name='ver-treino'),
    path('verTreino/<int:usuario_id>/<str:workout>/', views.verTreino, name='ver-treino'),
    path('redirecionarTreino/<int:usuario_id>', views.redirecionarTreino, name='redirecionar-treino'),
    path('treinar/<int:usuario_id>/<str:workout_name>/', views.treinar, name='treinar'),
    path('alterarTreino/<int:usuario_id>/<str:workout>/', views.alterarTreino, name='alterar-treino'),
    path('apagarTreino/<int:usuario_id>/<str:workout>/', views.apagarTreino, name='apagar-treino'),
    path('alterarExercicio/<int:usuario_id>/<str:edit_workout>/<int:exercise_id>', views.alterarExercicio, name='alterar-exercicioTreino'),
    path('excluirExercicio/<int:usuario_id>/<str:edit_workout>/<int:exercise_id>', views.excluirExercicioTreino, name="excluir-exercicioTreino")
]