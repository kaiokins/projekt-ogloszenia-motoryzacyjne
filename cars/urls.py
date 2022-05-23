from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_info, name='car_info'),
    path('search', views.search, name='search'),
]
