from django.shortcuts import render
from django.shortcuts import render
from .models import UserRank

def rank(request):
    ranks = UserRank.objects.all()
    context = {
        'ranks': ranks
    }
    return render(request, 'rank.html', context)