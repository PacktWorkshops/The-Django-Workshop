from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='bookr_welcome'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
    path('books/<int:book_pk>/reviews/new/', views.ReviewEdit.as_view(), name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.ReviewEdit.as_view(), name='review_edit'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/delete', views.ReviewDelete.as_view(), name='review_delete'),
]
