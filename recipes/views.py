from django.shortcuts import render,  redirect
from .models import Blog, Category, Review, Vote, RecipeBook
from blog.models import Blog as Blg
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchRecipe, Paginations
from django.db.models import Q
from django.contrib import messages

from django.db.models import Count




# Create your views here.

def index(request):
    blogs=Blog.objects.filter(Q(isActive=True)).annotate(num=Count("recipebook")).order_by("-num")[0:15]
    wrts=Blg.objects.filter(Q(inSlide=True) & Q(isActive=True)).order_by("-created")[0:15]
    video=Blog.objects.filter(youtube_link__isnull=False)[0:15]
    diet=Blog.objects.filter(category__title='Diet')[0:15]
    time=Blog.objects.filter(Q(cook_time__lte=15) & Q(time="dəqiqə"))[0:15]
    categories= Category.objects.all().order_by('title').order_by("title")
    context = {
        "blog": blogs,
        "category":categories,
        "like":video,
        "diet":diet,
        "wrts":wrts,
        "time":time,
    }
    return render(request, "index.html", context)


def category_filter(request, slug):
    category=Blog.objects.filter(category__slug=slug)
    if category:
        blogs, custom_range=Paginations(request, category)
    else:
        blogs=""
        custom_range=""
    context={
        "blog":blogs,
        "custom_range":custom_range
    }
    return render(request, "recipes/recipes.html",context)



def Recipes(request):
   
    blogs, search_query=searchRecipe(request)
    if blogs:
        blogs, custom_range=Paginations(request, blogs)
    else:
        blogs=""
        custom_range=""
    context = {
        "blog": blogs,
        "search_query":search_query,
        "custom_range":custom_range
    }

    return render(request, "recipes/recipes.html", context)







def details(request, slug):
    form=ReviewForm
    blog = Blog.objects.get(slug=slug)
    blogs= Blog.objects.filter(category=blog.category).filter(~Q(id=blog.id))
    reviews=Review.objects.filter(recipe=blog)
    upvote=Vote.objects.filter(Q(recipe=blog) & Q(value="up"))
    downvote=Vote.objects.filter(Q(recipe=blog) & Q(value="down"))
    book=RecipeBook.objects.filter(recipe__slug=slug).count()

    if request.method == "POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.recipe=blog
            review.owner=request.user.profile
            review.save()
            messages.success(request, "Şərhiniz əlavə edildi")
            return redirect("blogdetails", slug=blog.slug)
        else:
            messages.error(request, "Boş Şərh Olmaz")
        


    context = {
        "blog" : blog,
        "blogs" : blogs,
        "review":reviews,
        "upvote":upvote,
        "downvote":downvote,
        "form":form,
        "book":book
  
    }
    return render(request, "recipes/recipe_details.html", context)






@login_required(login_url="signin")
def createRecipe(request):
    profile=request.user.profile
    form = RecipeForm
    if request.method=='POST':
        form=RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe=form.save(commit=False)
            recipe.owner=profile
            recipe.save()
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, "recipes/recipes_form.html", context)






@login_required(login_url="signin")
def updateRecipe(request, pk):
    page="update"
    profile=request.user.profile
    blog=Blog.objects.filter(owner=profile).get(id=pk)
    form = RecipeForm(instance=blog)
    if request.method=='POST':
        form=RecipeForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form,
        "page":page
    }
    return render(request, "recipes/recipes_form.html", context)






@login_required(login_url="signin")
def deleteRecipe(request, pk):
    page="delete"
    profile=request.user.profile
    blog=profile.blog_set.get(id=pk)
    if request.method=='POST':
        blog.delete()
        return redirect("index")
    context={
        "page":page
    }
    return render(request, "recipes/recipes_form.html", context)






def aboutus(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')