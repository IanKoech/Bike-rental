from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Renter(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    charges = models.IntegerField()
    location = models.CharField(max_length=15)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', null= True)
    is_rented = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name

    @classmethod
    def search_location(cls,search_term):
        lessor = cls.objects.filter(location__icontains=search_term)
        return lessor

    @classmethod
    def filter_price(cls, price):
        renters = cls.objects.filter(charges=price)
        return renters


class Comment(models.Model):
    # Foreign key below establishes a many to one relationship with Renter model
    renter = models.ForeignKey(Renter, on_delete= models.CASCADE, related_name='comments')
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField(max_length=160)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.author)