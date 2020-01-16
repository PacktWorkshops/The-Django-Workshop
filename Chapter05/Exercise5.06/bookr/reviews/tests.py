import json
import os
from shutil import rmtree

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


def read_content(path):
    with open(path) as f:
        return f.read()


class Exercise6Test(TestCase):
    def test_django_conf(self):
        """
        Check that `reviews` is in `settings.INSTALLED_APPS`, the static dir is set to <projectdir>/static,
        STATIC_DIR is set to the static_temp directory and STATICFILES_STORAGE is ManifestStaticFilesStorage.
        """
        self.assertIn('reviews', settings.INSTALLED_APPS)
        self.assertEquals([settings.BASE_DIR + '/static'], settings.STATICFILES_DIRS)
        self.assertEquals(settings.BASE_DIR + '/static_temp', settings.STATIC_ROOT)
        self.assertEquals(settings.STATICFILES_STORAGE, 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage')

    def test_collect_static(self):
        """Test the result of the collectstatic command."""
        static_output_dir = os.path.join(settings.BASE_DIR, 'static_temp')
        call_command('collectstatic', '--noinput')
        self.assertTrue(os.path.isdir(static_output_dir))
        self.assertTrue(os.path.isdir(os.path.join(static_output_dir, 'admin')))
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, 'reviews', 'logo.png')))
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, 'main.css')))

        # Also some tests for manifest generated files
        manifest_path = os.path.join(settings.BASE_DIR, 'static_temp', 'staticfiles.json')
        self.assertTrue(os.path.exists(manifest_path))

        with open(manifest_path) as f:
            manifest = json.load(f)

        self.assertIn('main.css', manifest['paths'])
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, manifest['paths']['main.css'])))

        self.assertIn('reviews/logo.png', manifest['paths'])
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, manifest['paths']['reviews/logo.png'])))

        rmtree(static_output_dir)
