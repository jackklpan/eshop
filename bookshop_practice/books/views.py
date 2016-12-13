from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    book_list = Book.objects.all()
    return render(request, 'books/home.html', {
        'book_list': book_list
    })
