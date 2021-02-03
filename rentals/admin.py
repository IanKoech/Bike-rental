from django.contrib import admin
from .models import Renter, Customer, Comment
#Register your models here.

admin.site.register(Renter)
admin.site.register(Customer)
admin.site.register(Comment)