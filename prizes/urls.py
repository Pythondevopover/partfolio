from django.urls import path
from .views import prizes

urlpatterns = [
    path('', prizes, name='prizes'),  # Prizelar sahifasi
]
