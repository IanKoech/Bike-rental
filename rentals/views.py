from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Renter

# Create your views here.

def home(request):
    renters = Renter.objects.all()
    return render(request, 'home.html', {"renters":renters}) 

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_bikes = Renter.search_location(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"bikes": searched_bikes})

    else:
        message = "You haven't entered a location"
        return render(request, 'search.html',{"message":message})