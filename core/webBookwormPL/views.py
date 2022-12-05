from django.shortcuts import render
from django.http import HttpResponse

def mainhall(request):
    return render(request, 'mainhall.html')
def bookshelf(request):
    return render(request, 'bookshelf.html')    



# Create your views here.
