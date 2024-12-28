from django.shortcuts import render
from .models import Prize
def prizes(request):
    prizess = Prize.objects.all()
    return render(request, 'prizes.html', {'prizess': prizess})