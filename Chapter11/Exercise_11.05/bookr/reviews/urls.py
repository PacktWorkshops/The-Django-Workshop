from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'book', api_views.BookViewSet)

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('api/', include(router.urls), name='book'),
    path('api/login', api_views.Login.as_view(), name='login'),
]
