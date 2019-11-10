#!/usr/bin/env python3

from reviews.models import Contributor

contributor = Contributor.objects.create(first_names='Packt', last_names='Example Editor', email='PacktEditor@example.com')
book.contributors.add(contributor, through_defaults={'role': ‘EDITOR'})
