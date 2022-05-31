from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import login, logout, register, panel
from django.contrib.auth.models import User

class accountTest(TestCase):
    # urls test
    def test_urlLogin(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_urlLogout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_urlRegister(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_urlPanel(self):
        url = reverse('panel')
        self.assertEquals(resolve(url).func, panel)

    # views test
    def test_viewLogin(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    # def test_viewLogout(self):
    #     client = Client()
    #     response = client.get(reverse('logout'))
    #     self.assertEquals(response.status_code, 302)

    def test_viewRegister(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    # def test_viewPanel(self):
    #     object1 = User.objects.create(username='test', email='abc@gmail.com', first_name='t', last_name='u', password="password")
    #     client = Client()
    #     response = client.get(reverse('panel'))
    #     self.assertEqual(response.status_code, 200)