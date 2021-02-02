from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def home(request):
   return HttpResponse('Ollies bike rental')