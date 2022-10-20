from django.shortcuts import render,  redirect
from .models import Blog, Review, Vote, RecipeBook
from blog.models import Blog as Blg
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchRecipe, Paginations
from django.db.models import Q
from django.contrib import messages
from users.models import Profile




# Create your views here.


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
    user=Profile.objects.get(username=request.user.username)
    blog = Blog.objects.get(slug=slug)
    blogs= Blog.objects.filter(category=blog.category).filter(~Q(id=blog.id))
    reviews=Review.objects.filter(recipe=blog)
    upvote=Vote.objects.filter(recipe=blog)
    book=RecipeBook.objects.filter(recipe__slug=slug).count()
    like=Vote.objects.filter(recipe=blog, owner=user )
    bookmark=RecipeBook.objects.filter(recipe=blog, owner=user)

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
        "form":form,
        "book":book,
        "like":like,
        "bookmark":bookmark
  
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
        "page":page,
    }
    return render(request, "recipes/recipes_form.html", context)


@login_required
def recipe_book_add(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog-id')
        blog_var = Blog.objects.get(id=blog_id)
        user=Profile.objects.get(username=request.user.username)
        try:
            recipe_book = RecipeBook.objects.get(owner=user, recipe=blog_var)
            if recipe_book:
                recipe_book.delete()
                messages.warning(request, "Resept Kitabından Silindi")

        except:
            RecipeBook.objects.create(owner=user, recipe=blog_var)
            messages.success(request, "Resept Kitabına Əlavə Edildi")
        finally:
            return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def recipe_like_add(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog-id')
        blog_var = Blog.objects.get(id=blog_id)
        user=Profile.objects.get(username=request.user.username)
        try:
            recipe_like = Vote.objects.get(owner=user, recipe=blog_var)
            if recipe_like:
                recipe_like.delete()
                
        except:
            Vote.objects.create(owner=user, recipe=blog_var)
            
        finally:
            return redirect(request.META.get("HTTP_REFERER", "/"))