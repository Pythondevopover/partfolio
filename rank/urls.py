from django.urls import path
from .views import rank
from django.shortcuts import render

urlpatterns = [
    path('', rank, name='rank'),  # Rank sahifasi
]
