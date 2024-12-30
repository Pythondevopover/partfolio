from django.urls import path
from .views import prizes
from django.shortcuts import render

urlpatterns = [
    path('', prizes, name='prizes'),  # Prizelar sahifasi
]
