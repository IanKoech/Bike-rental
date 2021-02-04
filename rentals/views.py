from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Renter, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    renters = Renter.objects.all()
    return render(request, 'home.html', {"renters":renters}) 

def about(request):
    return render(request, 'about.html')

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        renters = Renter.search_location(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"renters": renters})

    else:
        message = "You haven't entered a location"
        return render(request, 'search.html',{"message":message})

def filter_price(request):
    if 'charges' in request.GET and request.GET['charges']:
        price  = request.GET.get('charges')
        renters =  Renter.filter_price(price)
        message  = f"{price}"

        return render(request,'filter.html', {"message":message, "renters":renters})
    
    else:
        message = "Enter the price to filter"
        return render(request, 'filter.html',{"message":message})

# def is_rented(request):
#     #Checks if the bike is rented out
#     renter = get_object_or_404(Renter, user=request.user)

@login_required(login_url='/accounts/login/')
def details(request, id):
    renter = Renter.objects.get(id = id)
    
    return render(request, 'details.html', {"renter":renter})

def regsiter(request):
    form = UserCreationForm()
    if form.is_valid():
        form.save()
        user = form.cleaned_data['username']
        return 

@login_required(login_url='/accounts/login/')
def post_comment(request, id):
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         print('valid')
    #     else:
    #         form = CommentForm()
    #     return render(request, 'comment.html',{"form": form})
    renter = Renter.objects.get(id=id)
    #Code below retrieves all approved comments from database
    comments = Comment.objects.filter(renter= renter)
    new_comment  = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment form without saving to database
            new_comment = comment_form.save(commit=False)
            #Assign current renter to the comment
            new_comment.renter = renter
            # saving comment  to database
            new_comment.save()

    else:
        comment_form = CommentForm()
    
    return render(request, 'comment.html',{'renter':renter, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})