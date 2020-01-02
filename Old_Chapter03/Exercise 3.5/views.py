from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book


def detail(request, book_title):
    book_detail = Book.objects.filter(title=book_title).values_list("publication_date", "isbn", "publisher")

    return JsonResponse({'results': list(book_detail)})
