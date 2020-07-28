from django.urls import path

from .views import BookRecordCreateView, BookRecordDeleteView, BookRecordFormView, BookRecordDetailView, BookRecordUpdateView, DeleteSuccessView, FormSuccessView

urlpatterns = [
    path('new_book_record', BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('delete_success', DeleteSuccessView.as_view(), name='delete_success'),
    path('book_record_create', BookRecordCreateView.as_view(), name='book_create'),
    path('book_record_update/<int:pk>', BookRecordUpdateView.as_view(), name='book_update'),
    path('book_record_delete/<int:pk>', BookRecordDeleteView.as_view(), name='book_delete'),
    path('book_record_detail/<int:pk>', BookRecordDetailView.as_view(), name='book_detail')
]