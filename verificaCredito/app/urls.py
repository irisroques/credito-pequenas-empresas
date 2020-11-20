from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('buscar_empresas/', buscar_empresas, name='buscar_empresas'),
]
