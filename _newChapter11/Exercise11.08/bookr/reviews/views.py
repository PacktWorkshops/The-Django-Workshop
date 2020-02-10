from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse


from .models import Book, Publisher, Review
from .forms import PublisherForm, SearchForm, ReviewForm
from .utils import average_rating


class WelcomeView(TemplateView):
    template_name = 'reviews/welcome_page.html'


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "reviews/search-results.html", {"search_text": search_text})


class BookList(ListView):
    model = Book
    template_name = 'reviews/book_list.html'
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
            book_list.append({'book': book, 'book_rating': book_rating,
                             'number_of_reviews': number_of_reviews})
        context['book_list'] = book_list

        return context


class BookDetail(DetailView):
    model = Book
    template_name = 'reviews/book_detail.html'

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


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher \"{}\" was created.".format(updated_publisher))
            else:
                messages.success(request, "Publisher \"{}\" was updated.".format(updated_publisher))

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, "reviews/instance-form.html",
                  {"form": form, "instance": publisher, "model_type": "Publisher"})


class ReviewEdit(View):

    def get(self, request, **kwargs):
        book_pk = kwargs.get('book_pk')
        review_pk = kwargs.get('review_pk')
        book = get_object_or_404(Book, pk=book_pk)

        if review_pk is not None:
            review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
        else:
            review = None

        form = ReviewForm(instance=review)
        return render(request, "reviews/instance-form.html",
                      {"form": form,
                       "instance": review,
                       "model_type": "Review",
                       "related_instance": book,
                       "related_model_type": "Book"
                       })

    def post(self, request, **kwargs):
        book_pk = kwargs.get('book_pk')
        review_pk = kwargs.get('review_pk')
        book = get_object_or_404(Book, pk=book_pk)
        if review_pk is not None:
            review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
        else:
            review = None
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, "Review for \"{}\" created.".format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Review for \"{}\" updated.".format(book))

            updated_review.save()
            return redirect("book_detail", book.pk)


class ReviewDelete(DeleteView):
    model = Review
    template_name = 'reviews/delete-review.html'

    def get_object(self):
        book_pk = self.kwargs.get('book_pk')
        review_pk = self.kwargs.get('review_pk')
        return get_object_or_404(Review, book_id=book_pk, pk=review_pk)

    def get_success_url(self):
        book_pk = self.kwargs.get('book_pk')
        return reverse('book_detail', args=(book_pk,))


