from django.urls import path
from reviews import views

urlpatterns = [
    path('books/', views.index, name='book_list'),
    path('books/<str:book_title>', views.detail, name='book_detail'),
]
