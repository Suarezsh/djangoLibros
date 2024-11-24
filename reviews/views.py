from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

def book_reviews(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'reviews/book_reviews.html', {'book': book})
