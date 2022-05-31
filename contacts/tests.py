from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import question
from .models import Contact

class otoautoTest(TestCase):
    # urls test
    def test_urlQuestion(self):
        url = reverse('question')
        self.assertEquals(resolve(url).func, question)

    # views test
    # def test_viewQuestion(self):
    #     client = Client()
    #     path = reverse('account:login')
    #     response = client.post(path=path, data={'username': 'test123', 'password': 'everything123'})
    #     self.assertRedirects(response, 'cars', status_code=302, target_status_code=200)

    # models test
    def test_contactText(self):
        message = Contact.objects.create(firstName='Jakub', lastName='Godfryd', carId=5, userId=5, question="Pytanko", carTitle="Volkswagen", city='Osobnica', province='Podkarpacie', email='kuba@godfryd.com', phoneNumber='123456789', message="Test wiadomości")
        self.assertEquals(str(message), "kuba@godfryd.com")