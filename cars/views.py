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
    brand = Car.objects.values('brand').distinct()
    model = Car.objects.values('model').distinct()
    city = Car.objects.values('city').distinct()
    year = Car.objects.values('year').distinct().order_by('year')
    body = Car.objects.values('body').distinct()

    data = {'cars': pagedCars,
            'brand': brand,
            'model': model,
            'city': city,
            'year': year,
            'body': body,
            }
    return render(request, 'cars/cars.html', data)

def car_info(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {'car': car,}
    return render(request, 'cars/car_info.html', data)

def search(request):
    cars = Car.objects.order_by('-added')
    searchBrand = Car.objects.values('brand').distinct()
    searchModel = Car.objects.values('model').distinct()
    searchCity = Car.objects.values('city').distinct()
    searchYear = Car.objects.values('year').distinct().order_by('year')
    searchBody = Car.objects.values('body').distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(title__icontains=keyword)

    # if 'brand' in request.GET:
    #     brand = request.GET['brand']
    #     if brand:
    #         cars = cars.filter(brand__iexact=brand)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body' in request.GET:
        body = request.GET['body']
        if body:
            cars = cars.filter(body__iexact=body)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {'cars': cars,
            'searchBrand': searchBrand,
            'searchModel': searchModel,
            'searchCity': searchCity,
            'searchYear': searchYear,
            'searchBody': searchBody,
            }
    return render(request, 'cars/search.html', data)