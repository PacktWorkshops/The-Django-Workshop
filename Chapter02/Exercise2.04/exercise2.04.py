#!/usr/bin/env python3

from reviews.models import Book
from reviews.models import BookContributor
from reviews.models import Contributor

contributor = Contributor.objects.get(first_names=‘Rowel')
book = Book.objects.get(title="Advanced Deep Learning with Keras”)
book_contributor = BookContributor(book=book, contributor=contributor, role='AUTHOR')
book_contributor.save()