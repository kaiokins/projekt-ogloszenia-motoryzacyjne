from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
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

        question = Contact(carId=carId, carTitle=carTitle, userId=userId, firstName=firstName, lastName=lastName, question=question, city=city, province=province, email=email, phoneNumber=phoneNumber, message=message)
        question.save()
        messages.success(request, "Wkrótce otrzymasz odpowiedź na Twoją wiadomość")

        return redirect('/cars'+carId)