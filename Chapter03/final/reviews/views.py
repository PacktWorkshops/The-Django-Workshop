from django.shortcuts import render

from .models import Book

from django.http import HttpResponse
import datetime

from django import views


def books_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'reviews/books_list.html', context)


def book_detail(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'reviews/books_detail.html', context)
