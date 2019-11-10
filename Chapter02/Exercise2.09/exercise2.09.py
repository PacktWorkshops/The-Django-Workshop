#!/usr/bin/env python3

from reviews.models import Book

books = Book.objects.filter(publisher__name='Packt Publishing')
print(books)