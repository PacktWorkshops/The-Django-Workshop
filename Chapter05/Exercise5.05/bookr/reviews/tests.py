import subprocess

from django.conf import settings
from django.test import TestCase


def read_content(path):
    with open(path) as f:
        return f.read()


class Exercise5Test(TestCase):
    def test_django_conf(self):
        """
        Check that `reviews` is in `settings.INSTALLED_APPS`, the static dir is set to <projectdir>/static, and
        STATIC_DIR is set to the static_production_test directory.
        """
        self.assertIn('reviews', settings.INSTALLED_APPS)
        self.assertEquals([settings.BASE_DIR + '/static'], settings.STATICFILES_DIRS)
        self.assertEquals(settings.BASE_DIR + '/static_production_test', settings.STATIC_ROOT)

    def test_find_static(self):
        """Test the result of the findstatic command (i.e. it finds what we expect, and not what we don't)."""
        res = subprocess.run(['python3', settings.BASE_DIR + '/manage.py', 'findstatic', 'main.css'],
                             stdout=subprocess.PIPE)
        self.assertEquals(0, res.returncode)
        self.assertIn(b'Found \'main.css\' here:', res.stdout)

        res = subprocess.run(['python3', settings.BASE_DIR + '/manage.py', 'findstatic', 'logo.png'],
                             stderr=subprocess.PIPE)
        self.assertIn(b'No matching file found for \'logo.png\'.', res.stderr)
        self.assertEquals(0, res.returncode)

        res = subprocess.run(['python3', settings.BASE_DIR + '/manage.py', 'findstatic', 'reviews/logo.png'],
                             stdout=subprocess.PIPE)
        self.assertIn(b'Found \'reviews/logo.png\' here:', res.stdout)
        self.assertEquals(0, res.returncode)

        res = subprocess.run(
            ['python3', settings.BASE_DIR + '/manage.py', 'findstatic', 'reviews/logo.png', 'missing-file.js',
             'main.css'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn(b'Found \'reviews/logo.png\' here:', res.stdout)
        self.assertIn(b'Found \'main.css\' here:', res.stdout)
        self.assertIn(b'No matching file found for \'missing-file.js\'.', res.stderr)
        self.assertEquals(0, res.returncode)

        res = subprocess.run(
            ['python3', settings.BASE_DIR + '/manage.py', 'findstatic', '-v0', 'reviews/logo.png', 'missing-file.js',
             'main.css'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertNotIn(b'Found \'reviews/logo.png\' here:', res.stdout)
        self.assertNotIn(b'Found \'main.css\' here:', res.stdout)
        self.assertNotIn(b'No matching file found for \'missing-file.js\'.', res.stderr)
        self.assertIn(b'bookr/reviews/static/reviews/logo.png', res.stdout)
        self.assertIn(b'bookr/static/main.css', res.stdout)
        self.assertEquals(b'', res.stderr)
        self.assertEquals(0, res.returncode)

        res = subprocess.run(
            ['python3', settings.BASE_DIR + '/manage.py', 'findstatic', '-v2', 'reviews/logo.png', 'missing-file.js',
             'main.css'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn(b'Found \'reviews/logo.png\' here:', res.stdout)
        self.assertIn(b'Found \'main.css\' here:', res.stdout)
        self.assertIn(b'No matching file found for \'missing-file.js\'.', res.stderr)
        self.assertIn(b'Looking in the following locations:', res.stdout)
        self.assertEquals(0, res.returncode)
