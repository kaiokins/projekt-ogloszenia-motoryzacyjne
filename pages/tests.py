from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import contact, about, services, home
from .models import Team

# Create your tests here.
class otoautoTests(TestCase):

    # urls test
    def test_urlContact(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_urlAbout(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_urlServices(self):
        url = reverse('services')
        self.assertEquals(resolve(url).func, services)

    def test_urlHome(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    # views test
    def test_viewHome(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_viewAbout(self):
        client = Client()
        response = client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_viewServices(self):
        client = Client()
        response = client.get(reverse('services'))
        self.assertEquals(response.status_code, 200)

    def test_viewContact(self):
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)

    # models test
    def test_teamText(self):
        member = Team.objects.create(firstName="Jakub", lastName="Godfryd", qualification='Właściciel')
        self.assertEquals(str(member), "Jakub Godfryd | Właściciel")
