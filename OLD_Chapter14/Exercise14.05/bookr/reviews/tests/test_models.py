from datetime import date
from django.test import TestCase

from reviews.models import Book, Contributor, Publisher


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
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

    def test_get_book(self):
        book = Book.objects.get(id=1)
        assert book.title == 'Test Book'
        self.assertEqual(book.publisher.name, 'Test Publisher')
        self.assertListEqual(list(book.contributors.all().values('first_names')), [{'first_names': 'Anna'}, {'first_names': 'Peter'}])

    def test_create_publisher(self):
        self.publisher = Publisher.objects.create(
            name='New Publisher',
            website='https://testnewpublisher.com',
            email='newpublisher@example.com')
        self.assertDictEqual({'name': self.publisher.name, 'website': self.publisher.website, 'email': self.publisher.email},
                             {'name': 'New Publisher', 'website': 'https://testnewpublisher.com', 'email': 'newpublisher@example.com'})
