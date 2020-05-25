from django import template

from reviews.models import Book


register = template.Library()


@register.simple_tag(name='books_count')
def number_of_books():
    return Book.objects.count()
