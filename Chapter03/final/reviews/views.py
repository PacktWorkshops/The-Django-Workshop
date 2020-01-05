from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Review
from .utils import average_rating


class BooksList(ListView):
    model = Book
    template_name = 'reviews/books_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = []
        books = context['object_list']

        for book in books:
            reviews = book.review_set.all()
            if reviews:
                book_rating = average_rating([review.rating for review in reviews])
                number_of_reviews = len(reviews)
            else:
                book_rating = None
                number_of_reviews = 0
            book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
        context['book_list'] = book_list

        return context


class BookDetail(DetailView):
    model = Book
    template_name = 'reviews/books_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['object']
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            context = {
                'book': book,
                'book_rating': book_rating,
                'reviews': reviews
            }
        else:
            context = {
                'book': book,
                'book_rating': None,
                'reviews': None
            }

        return context
