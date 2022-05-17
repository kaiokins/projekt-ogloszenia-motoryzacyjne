from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import cars
from .models import Car

# Create your tests here.
class carTests(TestCase):

    # urls test
    def test_urlCars(self):
        url = reverse('cars')
        self.assertEquals(resolve(url).func, cars)

    # views test
    def test_viewCars(self):
        client = Client()
        response = client.get(reverse('cars'))
        self.assertEquals(response.status_code, 200)
