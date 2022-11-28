from django.shortcuts import render
from django.http import HttpResponse

def mainhall(request):
    return render(request, 'mainhall.html')

# Create your views here.
