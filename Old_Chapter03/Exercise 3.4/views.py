from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Book

# Create your views here.
def index (request):
    list_book = Book.objects.all()
    html = ''
    for books in list_book:
        publisher = str(books.publisher)
        html += '<a>' + str(books.title) + ' is published by ' + str(publisher) + '</a> <br>'
    return HttpResponse(html)
