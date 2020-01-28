from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Publisher, Review
from .utils import average_rating


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class ReviewsSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Review
        fields = ['content', 'date_created', 'date_edited', 'rating', 'creator']


class BookDetailSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    rating = serializers.SerializerMethodField('book_rating')
    reviews = serializers.SerializerMethodField('book_reviews')

    def book_rating(self, book):
        reviews = book.review_set.all()
        if reviews:
            return average_rating([review.rating for review in reviews])
        else:
            None

    def book_reviews(self, book):
        reviews = book.review_set.all()
        if reviews:
            return ReviewsSerializer(reviews, many=True).data
        else:
            None

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher', 'rating', 'reviews']