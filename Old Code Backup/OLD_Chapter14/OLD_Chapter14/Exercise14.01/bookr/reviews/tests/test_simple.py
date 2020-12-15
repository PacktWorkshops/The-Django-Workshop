from django.test import SimpleTestCase


class TestSimple(SimpleTestCase):

    def test_simple(self):
        var = 2 + 2
        self.assertTrue(var == 4)
