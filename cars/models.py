from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Car(models.Model):
    yearChoise = []
    for r in range(1980, (datetime.now().year + 1)):
        yearChoise.append((r, r))

    provinceName = (
        ('Dolnośląskie', 'Dolnośląskie'),
        ('Kujawsko-Pomorskie', 'Kujawsko-Pomorskie'),
        ('Lubelskie', 'Lubelskie'),
        ('Lubuskie', 'Lubuskie'),
        ('Łódzkie', 'Łódzkie'),
        ('Małopolskie', 'Małopolskie'),
        ('Mazowieckie', 'Mazowieckie'),
        ('Opolskie', 'Opolskie'),
        ('Podkarpackie', 'Podkarpackie'),
        ('Podlaskie', 'Podlaskie'),
        ('Pomorskie', 'Pomorskie'),
        ('Śląskie', 'Śląskie'),
        ('Świętokrzyskie', 'Świętokrzyskie'),
        ('Warmińsko-mazurskie', 'Warmińsko-mazurskie'),
        ('Wielkopolskie', 'Wielkopolskie'),
        ('Zachodniopomorskie', 'Zachodniopomorskie'),
    )

    doorChoise = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    transmissionChoise = (
        ('Manualna', 'Manualna'),
        ('Automatyczna', 'Automatyczna'),
        ('Półautomatyczna', 'Półautomatyczna'),
    )

    conditionChoise = (
        ('Nowe', 'Nowe'),
        ('Używane', 'Używane'),
        ('Uszkodzone', 'Uszkodzone'),
    )

    featureChoise = (
        ('Interfejs Bluetooth', 'Interfejs Bluetooth'),
        ('Radio', 'Radio'),
        ('System nawigacji satelitarnej', 'System nawigacji satelitarnej'),
        ('Klimatyzacja automatyczna', 'Klimatyzacja automatyczna'),
        ('Klimatyzacja manualna', 'Klimatyzacja manualna'),
        ('Tapicerka skórzana', 'Tapicerka skórzana'),
        ('Elektrycznie ustawiany fotel kierowcy', 'Elektrycznie ustawiany fotel kierowcy'),
        ('Podgrzewany fotel pasażera', 'Podgrzewany fotel pasażera'),
        ('Podgrzewany fotel kierowcy', 'Podgrzewany fotel kierowcy'),
        ('Elektrycznie ustawiany fotel pasażera', 'Elektrycznie ustawiany fotel pasażera'),
        ('Podgrzewana przednia szyba', 'Podgrzewana przednia szyba'),
        ('Elektryczne szyby przednie', 'Elektryczne szyby przednie'),
        ('Elektryczne szyby tylne', 'Elektryczne szyby tylne'),
        ('Przyciemniane tylne szyby', 'Przyciemniane tylne szyby'),
        ('Tempomat', 'Tempomat'),
        ('Lampy ksenonowe', 'Lampy ksenonowe'),
        ('Kontrola odległości z tyłu (przy parkowaniu)', 'Kontrola odległości z tyłu (przy parkowaniu)'),
        ('Kamera parkowania tył', 'Kamera parkowania tył'),
        ('Lusterka boczne ustawiane elektrycznie', 'Lusterka boczne ustawiane elektrycznie'),
        ('Podgrzewane lusterka boczne', 'Podgrzewane lusterka boczne'),
        ('Kamera w lusterku bocznym', 'Kamera w lusterku bocznym'),
        ('Lampy przeciwmgielne', 'Lampy przeciwmgielne'),
        ('Wspomaganie kierownicy', 'Wspomaganie kierownicy'),
        ('ABS', 'ABS'),
        ('ESP', 'ESP'),
        ('Poduszki powietrzne', 'Poduszki powietrzne'),
        ('Isofix (punkty mocowania fotelika dziecięcego)', 'Isofix (punkty mocowania fotelika dziecięcego)'),
    )

    bodyChoise  = (
        ('Ciężarówka', 'Ciężarówka'),
        ('Suv', 'Suv'),
        ('Camper', 'Camper'),
        ('Mini ciężarówka', 'Mini ciężarówka'),
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('Kombi', 'Kombi'),
        ('Van', 'Van'),
        ('Minivan', 'Minivan'),
        ('Roadster', 'Roadster'),
        ('Kabriolet', 'Kabriolet'),
        ('Microcar', 'Microcar'),
        ('Coupe', 'Coupe'),
        ('Pickup', 'Pickup'),
        ('Supersamochód', 'Supersamochód'),
        ('Musclecar', 'Musclecar'),
    )

    fuelChoise = (
        ('Diesel', 'Diesel'),
        ('Benzyna', 'Benzyna'),
        ('LPG', 'LPG'),
        ('CNG', 'CNG'),
    )

    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100)
    year = models.IntegerField(choices=yearChoise, default=datetime.now().year)
    engine = models.CharField(max_length=100)
    power = models.SmallIntegerField(default=0)
    fuel = models.CharField(choices=fuelChoise, max_length=100)
    transmission = models.CharField(choices=transmissionChoise, max_length=15)
    condition = models.CharField(choices=conditionChoise, max_length=15)
    description = RichTextField()
    price = models.IntegerField()
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    color = models.CharField(max_length=100)
    features = MultiSelectField(choices=featureChoise, max_length=800)
    body = models.CharField(choices=bodyChoise, max_length=100)
    doors = models.CharField(choices=doorChoise, max_length=100)
    kilometeres = models.IntegerField()
    passengers = models.IntegerField()
    vin = models.CharField(max_length=100)
    isFeatured = models.BooleanField(default=False)
    province = models.CharField(choices=provinceName, max_length=100)
    city = models.CharField(max_length=100)
    added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title