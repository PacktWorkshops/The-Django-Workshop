from django import template

register = template.Library()

@register.inclusion_tag('book_list.html')
def book_list(books):
    book_list = [book_name for book_name, _ in books.items()]
    return {'book_list': book_list}
