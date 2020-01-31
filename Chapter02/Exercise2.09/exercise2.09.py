#!/usr/bin/env python3

from reviews.models import Book, Publisher

books = Book.objects.filter(publisher__name='Packt Publishing')
print(books)

publisher = Publisher.objects.get(book__title='Advanced Deep Learning with Keras')
print(publisher)

