
from django.http import HttpResponse,JsonResponse
from . models import Book

def detail (request,book_title):
    book= book_title
    book = Book.objects.get(title = book)
    templates = loader.get_template('reviews/detail.html')
    context = {
        "book": book,
    }
    return HttpResponse(templates.render(context, request))





