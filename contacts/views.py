from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def question(request):
    if request.method == 'POST':
        carId = request.POST['carId']
        carTitle = request.POST['carTitle']
        userId = request.POST['userId']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        question = request.POST['question']
        city = request.POST['city']
        province = request.POST['province']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']

        if request.user.is_authenticated:
            userId = request.user.id
            sended = Contact.objects.all().filter(carId=carId, userId=userId)
            if sended:
                messages.error(request, 'Wysłałeś zapytanie do tej oferty')
                return redirect('/cars'+carId)

        question = Contact(carId=carId, carTitle=carTitle, userId=userId, firstName=firstName, lastName=lastName, question=question, city=city, province=province, email=email, phoneNumber=phoneNumber, message=message)

        send_mail(
            'Zapytanie związane z samochodem',
            'Masz nowe zapytanie do ofert: ' + carTitle,
            email,
            ['otoautocomp2@gmail.com'],
            fail_silently=False,
        )

        question.save()
        messages.success(request, "Wkrótce otrzymasz odpowiedź na Twoją wiadomość")

        return redirect('/cars'+carId)