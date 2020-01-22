from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Profile,Project,User,Review
from .forms import ProfileForm,ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    current_profile = Profile.objects.filter(user=request.user) 
    posts=Project.objects.all()[::-1]
    if request.method == 'POST':
        form= ProjectForm(request.POST,request.FILES)
        rate = ReviewForm(request.POST)
        if form.is_valid() and rate.is_valid(): 
            project=form.save(commit=False)
            review=rate.save(commit=False)
            project.author=current_user
            review.author=current_user
            project.profile=current_profile
            project.save()
            review.save()
            
            return redirect('index')
    else:
        form=ProjectForm()
        rate=ReviewForm()
    return render(request,"index.html",{"posts":posts,"current_user": current_user, "form":form,"rate":rate})


def profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.filter(user = request.user) 
    posts = Project.objects.filter(author__id=id)[::-1]
    p_form= ProfileForm()
    return render(request, "profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "posts":posts,"p_form":p_form})
    


def review_form(request):
    current_user=request.user
    if request.method =="POST":
        rate = ReviewForm(request.POST)
        if rate.is_valid():
            review=rate.save(commit=False)
            review.author=current_user
            review.save()
            
            return redirect('index')
    else:
        rate = ReviewForm()
    return render(request,"index.html",{"rate":rate,"current_user":current_user})
    

def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})