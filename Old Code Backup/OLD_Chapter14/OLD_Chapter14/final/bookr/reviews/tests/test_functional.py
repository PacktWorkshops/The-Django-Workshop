import os
import time
from datetime import date

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver

from reviews.models import Book, Contributor, Publisher, Review


class TestFunctionality(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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

        cls.driver_path = os.path.dirname(os.path.abspath(__file__)) + '/geckodriver'
        cls.browser = webdriver.Firefox(executable_path=cls.driver_path)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_book_list(self):
        self.browser.get(self.live_server_url + '/books/')
        time.sleep(5)

        self.assertTrue(self.browser.find_element_by_class_name('navbar-brand').text, 'Bookr')
        self.books = self.browser.find_element_by_xpath('html/body/ul/li').text.split('\n')
        self.assertTrue('Number of reviews: 2' in self.books)
        self.browser.find_element_by_link_text('Reviews').click()
        time.sleep(5)

        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Book Details')
        self.book_detail = self.browser.find_element_by_xpath('html/body/ul').text.split("\n")
        self.assertTrue('Review comment: Nice read for a weekend' in self.book_detail)

