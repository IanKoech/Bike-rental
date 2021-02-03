from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Renter
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    renters = Renter.objects.all()
    return render(request, 'home.html', {"renters":renters}) 

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        renters = Renter.search_location(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"renters": renters})

    else:
        message = "You haven't entered a location"
        return render(request, 'search.html',{"message":message})

def post_comment(request):
    renter = get_object_or_404(Renter, slug=slug)
    comments = renter.comments.filter(active = True)
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