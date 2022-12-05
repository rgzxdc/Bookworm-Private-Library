from django.shortcuts import render
from django.http import HttpResponse
from .models import BookList

def mainhall(request):
    return render(request, 'mainhall.html')
def bookshelf(request):
    booklist = BookList.objects.all()
    data = {'BookList':booklist}
    return render(request, 'bookshelf.html', data)
def bookentry(request):
    if request.method == 'POST':
        title = request.POST.get('book_title')
        author = request.POST.get('author_name')
        isbn = request.POST.get('isbn')
        genre = request.POST.get('genre')
        added_date = request.POST.get('added_date')

        booklist = BookList()
        booklist.title = title
        booklist.author_name = author
        booklist.genre = genre
        booklist.added_date = added_date
        booklist.isbn = isbn
        booklist.save()


    return render(request, 'bookentry.html')


# Create your views here.
