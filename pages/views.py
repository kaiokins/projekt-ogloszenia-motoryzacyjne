from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    teams = Team.objects.all()
    fCars = Car.objects.order_by('-added').filter(isFeatured=True)
    aCars = Car.objects.order_by('-added')
    # search = Car.objects.values('brand', 'model', 'city', 'year', 'body')
    brand = Car.objects.values('brand').distinct()
    model = Car.objects.values('model').distinct()
    city = Car.objects.values('city').distinct()
    year = Car.objects.values('year').distinct().order_by('year')
    body = Car.objects.values('body').distinct()
    data = {
        'teams': teams,
        'fCars': fCars,
        'aCars': aCars,
        # 'search': search,
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

        info = User.objects.get(is_superuser=True)
        emailInfo = info.email
        send_mail(
            '[OtoAuto] Masz nową wiadomość, temat: ' + subject,
            messageMail,
            'otoautocomp@gmail.com',
            [emailInfo],
            fail_silently=False,
        )
        messages.success(request, 'Dziękujemy za kontakt. Wkrótce odpowiemy Ci na wiadomość.')
        return redirect('contact')

    return render(request, 'pages/contact.html')