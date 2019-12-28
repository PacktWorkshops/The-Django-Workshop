#!/usr/bin/env python3

from reviews.models import Contributor

contributor = Contributor.objects.get(first_names='Rowel')
books = contributor.book_set.all()
print(books)