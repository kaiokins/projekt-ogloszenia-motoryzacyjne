from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    carId = models.IntegerField()
    userId = models.IntegerField(blank=True)
    added = models.DateTimeField(default=datetime.now, blank=True)
    question = models.CharField(max_length=50)
    carTitle = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email