from django.urls import path
from reviews import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<str:book_title>', views.book_detail, name='book_detail'),
]
