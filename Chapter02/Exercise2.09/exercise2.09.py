#!/usr/bin/env python3

from reviews.models import Book, Publisher

books = Book.objects.filter(publisher__name='Packt Publishing')
print(books)

publisher = Publisher.objects.get(book__title='Advanced Deep Learning with Keras')
print(publisher)

book = Book.objects.get(title='The Talisman')
print(book.publisher)

publisher = Publisher.objects.get(name='Pocket Books')
publisher.book_set.all()