#!/usr/bin/env python3

from reviews.models import Book

book = Book.objects.get(title='The Tailsman')
contributors = book.contributors.all()
print(contributors)