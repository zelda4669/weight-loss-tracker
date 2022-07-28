from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignUpPageTests(TestCase):
    def test_signup_url_exists_and_is_correct(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_is_correct_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
