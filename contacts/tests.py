from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import question
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpRequest
from cars.views import cars
from django.test.client import RequestFactory
from django.core.mail import send_mail

class otoautoTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='abc@gmail.com', first_name='t', last_name='u',password="password")

    # urls test
    def test_urlQuestion(self):
        url = reverse('question')
        self.assertEquals(resolve(url).func, question)

    # views test
    def test_viewQuestion(self):
        response = self.client.get(reverse('cars'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/cars.html')

    # models test
    def test_contactText(self):
        message = Contact.objects.create(firstName='Jakub', lastName='Godfryd', carId=5, userId=5, question="Pytanko", carTitle="Volkswagen", city='Osobnica', province='Podkarpacie', email='kuba@godfryd.com', phoneNumber='123456789', message="Test wiadomości")
        self.assertEquals(str(message), "kuba@godfryd.com")

    # email send test
    def test_sendEmail(self):
        question = Contact(carId=1, carTitle='VW Golf', userId=2, firstName='Jakub', lastName='Godfryd', question='Jestem zainteresowany', city='Jasło', province='Podkarpackie', email='kuba@godfryd.com', phoneNumber='123456789', message="Test wiadomosci")
        send_mail(
            'Zapytanie związane z samochodem',
            'Masz nowe zapytanie do ofert: ' + question.carTitle,
            'otoautocomp2@gmail.com',
            [self.user.email],
            fail_silently=False,
        )