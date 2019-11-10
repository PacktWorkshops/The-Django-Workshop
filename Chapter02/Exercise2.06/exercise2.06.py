#!/usr/bin/env python3

from reviews.models import Publisher

publisher = Publisher.objects.get(name='Pocket Books’)
print(publisher.name)
print(publisher.website)
print(publisher.email)