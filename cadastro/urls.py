from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.cadastrar, name='cadastro'),
    path('admin/', views.admin, name='cadastro-admin'),

]

