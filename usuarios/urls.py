from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('admin/', views.admin, name='admin'),
    path('excluirAdmin/', views.excluirAdmin, name='excluir-admin'),
    path('alterarAdmin/', views.alterarAdmin, name='alterar-admin'),
    path('alterarSenhaAdmin/', views.alterarSenhaAdmin, name='alterar-senha-admin'),
    path('verDados/<int:usuario_id>', views.verDados, name='ver-dados'),
    path('alterarDados/<int:usuario_id>', views.alterarDados, name='alterar-dados'),
    path('excluir/<int:usuario_id>', views.excluirUsuario, name="excluir-usuario"),
    path('renovarAssinatura/<int:usuario_id>', views.renovarAssinatura, name='renovar-assinatura'),
]