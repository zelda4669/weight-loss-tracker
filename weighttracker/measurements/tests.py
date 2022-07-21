from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Measurements


class HomepageTests(SimpleTestCase):
    def test_url_exists_correctly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'create_account.html')


class AddMeasurementsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com', password='password'
        )

        cls.measurement = Measurements.objects.create(
            date='2022-07-01',
            weight=230,
            bust=45,
            chest=54,
            waist=45,
            hips=42,
            left_thigh=22,
            right_thigh=22,
            left_calf=41,
            right_calf=4,
            left_forearm=32,
            right_forearm=12,
            left_upper_arm=12,
            right_upper_arm=12
        )

    def test_measurement_model(self):
        self.assertEqual(self.measurement.date, '2022-07-01')
        self.assertEqual(self.measurement.weight, 230)
        self.assertEqual(self.measurement.bust, 45)
        self.assertEqual(self.measurement.chest, 54)
        self.assertEqual(self.measurement.waist, 45)
        self.assertEqual(self.measurement.hips, 42)
        self.assertEqual(self.measurement.left_thigh, 22)
        self.assertEqual(self.measurement.right_thigh, 22)
        self.assertEqual(self.measurement.left_calf, 41)
        self.assertEqual(self.measurement.right_calf, 4)
        self.assertEqual(self.measurement.left_forearm, 32)
        self.assertEqual(self.measurement.right_forearm, 12)
        self.assertEqual(self.measurement.left_upper_arm, 12)
        self.assertEqual(self.measurement.right_upper_arm, 12)
        self.assertEqual(str(self.measurement), 'Body Comp from 2022-07-01')

    def test_url_exists_correctly(self):
        response = self.client.get('/add_measurement')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse('add_measurement'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('add_measurement'))
        self.assertTemplateUsed(response, 'add_measurements.html')