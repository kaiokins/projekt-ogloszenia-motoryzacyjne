from django.db import models

# Create your models here.

class Team(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    qualification = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    youtube = models.URLField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + " " + self.lastName + " | " + self.qualification