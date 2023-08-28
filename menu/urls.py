from django.urls import path
from . import views


urlpatterns = [
    path("/", views.main ,name='menu-principal'),
    path("login/", views.login_func, name="login"),
    path("logout/", views.logout_func, name="logout")
]