from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import cars, car_info, search
from .models import Car

class carTests(TestCase):
    def setUp(self):
        self.client = Client()

    # urls test
    def test_urlCars(self):
        url = reverse('cars')
        self.assertEquals(resolve(url).func, cars)

    def test_urlCarInfo(self):
        url = reverse('car_info', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, car_info)

    def test_urlSearch(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    # views test
    def test_viewCars(self):
        response = self.client.get(reverse('cars'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/cars.html')

    # def test_viewCarInfo(self):
    #     response = self.client.get(reverse('cars', kwargs={'id': 1}))
    #     self.assertEquals(response.status_code, 200)

    def test_viewSearch(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/search.html')

    # models test
    def test_carsText(self):
        car = Car.objects.create(title="Volkswagen Golf 4, 1.9 TDI", brand="Volkswagen", model="Golf", year=2005, engine="1", fuel="Benzyna", transmission="Manualna", condition="Używane", description="ok", price=5000, photo1="/static/img/car/car-1.jpg", color="Czarny", features="Radio", body="Hatchback", doors="5", kilometeres=250000, vin="VWW1114444", province="Podkarpackie", city="Jasło", passengers=5)
        self.assertEquals(str(car), "Volkswagen Golf 4, 1.9 TDI")
