from django.test import TestCase

from reviews.forms import PublisherForm
from reviews.models import Publisher


class TestForms(TestCase):

    def test_publisher_form(self):
        form = PublisherForm(data={
            'name': 'Test Publisher',
            'website': 'https://testsampleurl.com',
            'email': 'example@example.com'
        })
        self.assertTrue(form.is_valid())
        form.save()
        publisher = Publisher.objects.get(id=1)
        self.assertDictEqual(
            {'name': publisher.name,
             'website': publisher.website,
             'email': publisher.email},
            {'name': 'Test Publisher',
             'website': 'https://testsampleurl.com',
             'email': 'example@example.com'})


