#!/usr/bin/env python3

from reviews.models import Publisher

publisher = Publisher.objects.get(book__title='Advanced Deep Learning with Keras')
print(publisher)

