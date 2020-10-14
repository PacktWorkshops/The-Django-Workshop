from datetime import date
from django.contrib.auth.models import User
from django.test import Client, TestCase

from reviews.models import Book, Contributor, Publisher, Review


class TestAPIs(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='testemail@email.com',
            username='Test User')
        cls.user.set_password('testpassword')
        cls.user.save()

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

    def setup(self):
        self.client = Client()

    def test_book_detail(self):
        response = self.client.get('/api/books/1/')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            {'title': response.data['title'],
             'isbn': response.data['isbn'],
             'publisher': response.data['publisher']['name']},
            {'title': 'Test Book',
             'isbn': '9754451697216',
             'publisher': 'Test Publisher'})

    def test_create_review(self):
        self.client.login(username="Test User", password="testpassword")
        response = self.client.post(
            '/api/reviews/',
            {'content': 'An amazing read',
             'rating': 5,
             'book_id': 1})
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(
            {'content': response.data['content'],
             'rating': response.data['rating'],
             'creator': response.data['creator']['username']},
            {'content': 'An amazing read',
             'rating': 5,
             'creator': 'Test User'})
