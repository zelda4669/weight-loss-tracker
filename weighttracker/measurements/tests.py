from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_correctly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')