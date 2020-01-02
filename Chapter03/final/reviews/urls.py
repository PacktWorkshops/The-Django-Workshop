from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.books_list, name='all_books'),
    path('book/<int:id>/', views.book_detail)

]
