from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path('', contact_view, name='contact_us'),
]
