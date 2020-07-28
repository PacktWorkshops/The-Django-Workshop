from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic import DetailView
from django.views import View

from .forms import BookForm
from .models import Book


class BookRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/book_management/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")

class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record deleted successfully")

class BookRecordCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['name', 'author']
    success_url = '/book_management/entry_success'

class BookRecordUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['name', 'author']
    success_url = '/book_management/entry_success'

class BookRecordDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/book_management/delete_success'

class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'