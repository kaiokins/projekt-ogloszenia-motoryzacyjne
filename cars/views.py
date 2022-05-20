from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-added')
    pagination = Paginator(cars, 6)
    page = request.GET.get('page')
    pagedCars = pagination.get_page(page)
    data = {'cars': pagedCars,}
    return render(request, 'cars/cars.html', data)

def car_info(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {'car': car,}
    return render(request, 'cars/car_info.html', data)

