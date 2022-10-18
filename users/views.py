from dataclasses import field
from email import message
from django.shortcuts import render, redirect
from .models import Profile
from recipes.models import Blog
from blog.models import Blog as Blg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileForm
from django.db.models import Count
# Create your views here.



@login_required(login_url='signin')
def myprofile(request, slug):
    profile=request.user.profile
    page='profile'
    recipes=Blog.objects.filter(owner__username=profile.username).order_by("-created")
    blogs=Blg.objects.filter(owner__username=profile.username).order_by("-created")
    book=profile.recipebook_set.all() 
    review=profile.review_set.count()
    
    context={
        "profile":profile,
        "recipes":recipes,
        "blogs":blogs,
        "page":page,
        "book":book,
        "review":review,
   
    }
    return render(request, 'users/user_profile.html',context)


def signin(request):
    page='signin'
    if request.user.is_authenticated:
        return redirect('profile')


    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
            messages.success(request="Uğurla Giriş Etdiniz")
        except:
            pass
        
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET["next"] if "next" in request.GET else "index")
        else:
            messages.error(request, "İstifadəçi adı və ya şifrə yanlışdır.")


    return render(request, 'users/signin.html')




def signout(request):
  
    logout(request)
    return redirect('index')


def signup(request):
    page='signup'
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect("edit-account")

    context={
        "page":page,
        "form":form
    }
    return render(request, 'users/signin.html', context)

def userAccount(request, slug):
    page='Account'
    profile=Profile.objects.get(slug=slug)
    user_recipes=Blog.objects.filter(owner__slug=profile.slug).order_by("-created")
    user_blogs=Blg.objects.filter(owner__username=profile.username).order_by("-created")
    user_book=profile.recipebook_set.all() 
    user_review=profile.review_set.count()
    context={
        "profil":profile,
        "page": page,
        "user_recipes":user_recipes,
        "user_blogs":user_blogs,
        "user_book":user_book,
        "user_review":user_review
    }
    return render(request, "users/user_profile.html", context )
    

def users(request):
    profiles=Profile.objects.all()
    context={
        "profiles":profiles
    }
    return render(request, "contact.html",context)

@login_required(login_url='signin')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=="POST":
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/account/{profile.slug}')

    context={
        "form":form
    }
    print()
    return render(request, "users/profile_form.html",context)