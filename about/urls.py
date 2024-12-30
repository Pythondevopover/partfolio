from django.urls import path
from .views import about
from django.shortcuts import render

from django.http import HttpResponseNotFound
from django.shortcuts import render

urlpatterns = [
    path('', about, name='about'),  # Bosh sahifa yoki About sahifasi
]