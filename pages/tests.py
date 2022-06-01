from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import contact, about, services, home
from .models import Team
from django.core.mail import send_mail
from django.contrib.auth.models import User

class otoautoTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='abc@gmail.com', first_name='t', last_name='u', password="password")

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
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_viewAbout(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_viewServices(self):
        response = self.client.get(reverse('services'))
        self.assertEquals(response.status_code, 200)

    def test_viewContact(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)

    # models test
    def test_teamText(self):
        member = Team.objects.create(firstName="Jakub", lastName="Godfryd", qualification='Właściciel')
        self.assertEquals(str(member), "Jakub Godfryd | Właściciel")

    # email send test
    def test_send_email(self):
        messageMail = 'Imię: ' + 'Adrian' + '\nEmail: ' + 'Nowak' + '\nTelefon: ' + '123456789' + '\nWiadomość: ' + 'Test wiadomości'
        send_mail(
            '[OtoAuto] Masz nową wiadomość, temat: ' + 'Temat',
            messageMail,
            'otoautocomp@gmail.com',
            [self.user.email],
            fail_silently=False,
        )