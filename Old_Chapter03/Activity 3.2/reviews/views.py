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


def detail_book(request, book_title):
    book = Book.objects.get(title=book_title)
    templates = loader.get_template('reviews/detail_books.html')
    context = {
        "book": book
    }
    return HttpResponse(templates.render(context, request))


def list_cont(request):
    list_contributors = Contributor.objects.all()
    context = {
        "list_contributors": list_contributors
    }
    return render(request, 'reviews/list_cont.html', context)


def detail_contributor(request, contributor_name):
    first_names = contributor_name.split()[0]
    last_names = contributor_name.split()[1]
    contributor = Contributor.objects.get(first_names=first_names, last_names=last_names)
    role = BookContributor.objects.filter(contributor = contributor.id).first()
    books= contributor.book_set.all().first()


    context = {
        "contributor": contributor,
         "role" : role,
        "book": books

    }
    return render(request, 'reviews/detail_contributor.html', context)