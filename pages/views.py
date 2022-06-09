from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    teams = Team.objects.all()
    fCars = Car.objects.order_by('-added').filter(isFeatured=True)
    aCars = Car.objects.order_by('-added')
    brand = Car.objects.values('brand').distinct().order_by('brand')
    model = Car.objects.values('model').distinct().order_by('model')
    city = Car.objects.values('city').distinct().distinct('city')
    year = Car.objects.values('year').distinct().order_by('year')
    body = Car.objects.values('body')
    data = {
        'teams': teams,
        'fCars': fCars,
        'aCars': aCars,
        'brand': brand,
        'model': model,
        'city': city,
        'year': year,
        'body': body,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        messageMail = 'Imię: ' + name + '\nEmail: ' + email + '\nTelefon: ' + phone + '\nWiadomość: ' + message

        send_mail(
            '[OtoAuto] Masz nową wiadomość, temat: ' + subject,
            messageMail,
            email,
            ['otoautocomp2@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Dziękujemy za kontakt. Wkrótce odpowiemy Ci na wiadomość.')
        return redirect('contact')

    return render(request, 'pages/contact.html')