from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("<h1> List of books </h1>")

def detail (request,book_id):
    return HttpResponse("<h2> You are checking book number: " + str(book_id) + "</h2>")

def titleDisplay (request,book_title):
    return HttpResponse("<h3> You are checking book named: " + book_title + "</h3>")
