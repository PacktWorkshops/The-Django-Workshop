from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Contributor
from django.template import loader


# Create your views here.
def index(request):
    context = {
        "booklist": "booklist",
        "contributorlist": "contributorlist"
    }
    return render(request, 'reviews/index.html', context)


def list_book(request):
    list_book = Book.objects.all()
    context = {
        "list_book": list_book
    }
    return render(request, 'reviews/list_book.html', context)


def list_cont(request):
    list_contributors = Contributor.objects.all()
    context = {
        "list_contributors": list_contributors
    }
    return render(request, 'reviews/list_cont.html', context)


