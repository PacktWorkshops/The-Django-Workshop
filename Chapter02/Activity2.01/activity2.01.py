#!/usr/bin/env python3

from reviews.models import Contributor

contributor = Contributor.objects.filter(book__title='The Tailsman')
print(contributor)