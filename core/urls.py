from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('users/signin',login),
    path('users/signup/',registro),
    path('users/logout', puestoPersonas, name='puestoPersonas'),
]