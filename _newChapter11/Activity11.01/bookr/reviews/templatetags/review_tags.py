from django import template

from reviews.models import Book
register = template.Library()


@register.simple_tag(name='books_count')
def number_of_books():
    return Book.objects.count()


@register.inclusion_tag('reviews/recent_books.html')
def recent_books():
    books = Book.objects.all().order_by('-publication_date')[:3]
    return {'books': books}


@register.filter(name='review_count_filter')
def review_count_converter(val):
    if val == 0:
        return 'No reviews yet.'
    else:
        return val
