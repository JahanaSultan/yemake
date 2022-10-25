from django.shortcuts import render,  redirect
from .models import Blog, Review, Vote, RecipeBook
from .forms import RecipeForm
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



def video_filter(request):
    video=Blog.objects.filter(youtube_link__isnull=False)
    if video:
        blogs, custom_range=Paginations(request, video)
    else:
        blogs=""
        custom_range=""
    context={
        "blog":blogs,
        "custom_range":custom_range
    }
    return render(request, "recipes/recipes.html",context)


def time_filter(request):
    time=Blog.objects.filter(Q(cook_time__lte=15) & Q(time="dəqiqə"))[0:15]
    if time:
        blogs, custom_range=Paginations(request, time)
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




def add_comment(request):
     user=Profile.objects.get(username=request.user.username)
     if request.method == "GET":
        blog_id = request.GET['post_id']
        comment_body=request.GET['comment_body']
        blog_var = Blog.objects.get(id=blog_id)
        try:
            Review.objects.create(owner=user, recipe=blog_var, body=comment_body)
        except:
            messages.error(request, "Xəta baş verdi!")
            
        finally:
            return redirect(request.META.get("HTTP_REFERER", "/"))





def delete_comment(request, pk):
    profile=request.user.profile
    comment=profile.review_set.get(id=pk)
    if request.method=='POST':
        comment.delete()
        messages.success(request,"Şərhiniz Silindi")
        return redirect(request.META.get("HTTP_REFERER", "/"))





def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogs= Blog.objects.filter(category=blog.category).filter(~Q(id=blog.id))
    reviews=Review.objects.filter(recipe=blog)
    upvote=Vote.objects.filter(recipe=blog)
    book=RecipeBook.objects.filter(recipe__slug=slug).count()
    if request.user.is_authenticated:
        user=Profile.objects.get(username=request.user.username)
        bookmark=RecipeBook.objects.filter(owner=user, recipe=blog)
        like=Vote.objects.filter(owner=user, recipe=blog)
    else:
        like=False
        bookmark=False
   

    context = {
        "blog" : blog,
        "blogs" : blogs,
        "review":reviews,
        "upvote":upvote,
        "book":book,
        "bookmark":bookmark,
        "like":like,
  
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
            messages.success(request, "Reseptiniz qeydə alındı, təsdiqləndikdə bildiriş alacaqsınız.")
            return redirect(f'/account/{profile.slug}')

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
            messages.success(request,"Dəyişiklik qeydə alındı!")
            return redirect(f'/account/{profile.slug}')

    context = {
        "form":form,
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
        messages.success(request,"Resept Silindi")
        return redirect(request.META.get("HTTP_REFERER", "/"))
    context={
        "page":page,
    }
    return render(request, "recipes/recipes_form.html", context)



def recipe_book_add(request):
    if request.method == 'GET':
        blog_id = request.GET['post_id']
        blog_var = Blog.objects.get(id=blog_id)
        user=Profile.objects.get(username=request.user.username)
        if user != blog_var.owner:
            try:
                recipe_book = RecipeBook.objects.get(owner=user, recipe=blog_var)
                if recipe_book:
                    recipe_book.delete()
            except:
                RecipeBook.objects.create(owner=user, recipe=blog_var)
            finally:
                return redirect(request.META.get("HTTP_REFERER", "/"))




def recipe_like_add(request):
    if request.method == 'GET':
        blog_id = request.GET['post_id']
        blog_var = Blog.objects.get(id=blog_id)
        user=Profile.objects.get(username=request.user.username)
        if user != blog_var.owner:
            try:
                recipe_like = Vote.objects.get(owner=user, recipe=blog_var)
                if recipe_like:
                    recipe_like.delete()
                    
            except:
                Vote.objects.create(owner=user, recipe=blog_var)
                
            finally:
                return redirect(request.META.get("HTTP_REFERER", "/"))
