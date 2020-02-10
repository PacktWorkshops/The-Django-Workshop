from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail')
]
