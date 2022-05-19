from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    fCars = Car.objects.order_by('-added').filter(isFeatured=True)
    aCars = Car.objects.order_by('-added')
    data = {
        'teams': teams,
        'fCars': fCars,
        'aCars': aCars,
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
    return render(request, 'pages/contact.html')
