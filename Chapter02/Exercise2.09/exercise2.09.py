#!/usr/bin/env python3

from reviews.models import Contributor

contributors = Contributor.objects.all()
print(contributors)
print(contributors[0])
print(contributors[0].first_names)
print(contributors[0].last_names)