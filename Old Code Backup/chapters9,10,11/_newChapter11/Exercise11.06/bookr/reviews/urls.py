from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='bookr_welcome'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail')
]
