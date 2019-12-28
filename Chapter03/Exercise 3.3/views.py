from django.shortcuts import render
from django.http import HttpResponse
from . models import Book

# Create your views here.
def index (request):
    list_book = Book.objects.all()
    link= ''
    for books in list_book:
        url = '/bookr/' + str(books.title) + '/'
        html += '<a href = " ' + url + '" >' + str(books.title) + '</a> <br>'

    return HttpResponse(link)
