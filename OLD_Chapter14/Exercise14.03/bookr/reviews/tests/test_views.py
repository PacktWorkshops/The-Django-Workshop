from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from reviews.models import Book, Contributor, Publisher, Review


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(
            email='testemail@email.com',
            username='Test User1')

        cls.user2 = User.objects.create(
            email='testemail@email.com',
            username='Test User2')

        cls.publisher = Publisher.objects.create(
            name='Test Publisher',
            website='https://testsampleurl.com',
            email='example@example.com')

        cls.book = Book.objects.create(
            title='Test Book',
            publication_date=date(2019, 10, 21),
            isbn='9754451697216',
            publisher=cls.publisher)

        cls.contributor1 = Contributor.objects.create(
            first_names='Anna',
            last_names='Smith',
            email='annasmith@example.com')

        cls.contributor2 = Contributor.objects.create(
            first_names='Peter', last_names='Parker',
            email='peterparker@example.com')

        cls.book.contributors.set(
            [cls.contributor1, cls.contributor2],
            through_defaults={'role': 'CO_AUTHOR'})

        cls.review1 = Review.objects.create(
            content="Nice read for a weekend",
            book=cls.book,
            creator=cls.user1,
            rating=5)

        cls.review1 = Review.objects.create(
            content="An average read",
            book=cls.book,
            creator=cls.user2,
            rating=3)

    def setUp(self):
        self.client = Client()

    def test_get_reviews_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/book_list.html')
        self.assertIn(b'Test Book', response.content)
        self.assertNotIn(b'Nice read for a weekend', response.content)
        self.assertNotIn(b'An average read', response.content)

    def test_get_reviews_detail(self):
        response = self.client.get(reverse('book_detail', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/book_detail.html')
        self.assertIn(b'Test Book', response.content)
        self.assertIn(b'Nice read for a weekend', response.content)
        self.assertIn(b'An average read', response.content)
