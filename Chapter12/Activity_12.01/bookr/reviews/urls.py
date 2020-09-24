from django.urls import path
from . import views, api_views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('api/all_books/', api_views.AllBooks.as_view(), name='all_books'),
    path('api/contributors/', api_views.ContributorView.as_view(), name='contributors')
]
