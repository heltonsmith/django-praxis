from django.contrib import admin
from django.urls import path
from .views import inicial, primera_vista, segunda_vista, tercera_vista

urlpatterns = [
    path("inicial/", inicial),
    path("primera/", primera_vista),
    path("segunda/", segunda_vista),
    path("tercera/", tercera_vista),
]