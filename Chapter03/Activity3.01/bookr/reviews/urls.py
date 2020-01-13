from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list),
    path('book/<int:id>/', views.book_detail)
]
