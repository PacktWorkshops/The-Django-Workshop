#!/usr/bin/env python3

from reviews.models import Contributor, Publisher

Contributor.objects.filter(book__title='The Talisman')

Publisher.objects.get(book__title='Advanced Deep Learning with Keras')

book = Book.objects.get(title='The Talisman')

print(book.publisher)

publisher = Publisher.objects.get(name='Pocket Books')

publisher.book_set.all()