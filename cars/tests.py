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


    # def test_carText(self):
    #     member = Car.objects.create(title="Volkswagen Golf 4, 1.9 TDI", brand="Volkswagen", model="Golf", year=2005, engine="1.6", fuel="Benzyna", transmission="Manualna", condition="Używane", description="ok", price=5000, photo1="/static/img/car/car-1.jpg", color="Czarny", features="Radio", body="Hatchback", doors="5", kilometeres=250000, vin="VWW1114444", province="Podkarpackie", city="Jasło")
    #     self.assertEquals(str(member), "Volkswagen Golf 4, 1.9 TDI")