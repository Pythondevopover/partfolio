from django.urls import path
from .views import rank
from django.shortcuts import render

def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)

handler404 = custom_page_not_found
urlpatterns = [
    path('', rank, name='rank'),  # Rank sahifasi
]
