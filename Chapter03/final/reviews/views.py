from django.shortcuts import render

from django.http import HttpResponse
import datetime

from django import views


def books_list(request):
    return render(request, 'reviews/books_list.html', {})
