from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader


# Create your views here.

def index(request):
    list_book = Book.objects.all()
    context = {
        "list_book": list_book
    }
    return render(request, 'reviews/index.html', context)


def detail(request, book_title):
    book = book_title
    book = Book.objects.get(title=book)
    templates = loader.get_template('reviews/detail.html')
    context = {
        "book": book
    }
    return render(request, 'reviews/detail.html', context)
