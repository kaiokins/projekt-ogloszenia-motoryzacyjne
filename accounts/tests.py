from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from .views import login, logout, register, panel
from django.contrib.auth.models import User, AnonymousUser

class accountTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='abc@gmail.com', first_name='t', last_name='u', password="password")

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
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_viewLogout(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_viewRegister(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_viewPanel(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('panel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/panel.html')

    # csrf test
    def test_csrfLogin(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_csrfRegister(self):
        response = self.client.get(reverse('register'))
        self.assertContains(response, 'csrfmiddlewaretoken')
