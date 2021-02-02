from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Renter(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    contact  = models.IntegerField()
    email = models.EmailField()
    charges = models.IntegerField()
    location = models.CharField(max_length=30)
    description = models.TextField()
    #image = models.ImageField(upload_to = 'images/')

    @classmethod
    def search_location(cls,search_term):
        bike = cls.objects.filter(location__icontains=search_term)
        return bike

class Customer(model.Models):
    name  = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name


