from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.order_by('title')
    return render(request, 'reading/index.html', {'books': books})

def info(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'reading/info.html', {'book': book})