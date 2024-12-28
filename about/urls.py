from django.urls import path
from .views import about

urlpatterns = [
    path('', about, name='about'),  # Bosh sahifa yoki About sahifasi
]
