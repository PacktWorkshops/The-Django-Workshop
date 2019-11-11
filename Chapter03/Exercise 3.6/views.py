from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from django.template import loader

# Create your views here.
def index (request):
    list_book = Book.objects.all()
    templates = loader.get_template('reviews/index.html')
    context = {
        "list_book" : list_book
    }
    return HttpResponse(templates.render(context,request))
