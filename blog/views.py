from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.db.models import Q
from .utils import Paginations
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    blogs, custom_range=Paginations(request, blogs)
    context = {
        "blog": blogs,
        "custom_range":custom_range
    }
    return render(request, 'blog/blogs.html',context)

def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogs= Blog.objects.filter(category=blog.category).filter(~Q(id=blog.id))
    context = {
        "blog" : blog,
        "blogs" : blogs
    }
    return render(request, "blog/blog_details.html", context)


@login_required(login_url="signin")
def createBlog(request):
    page="createblog"
    profile=request.user.profile
    form = BlogForm
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.owner=profile
            blog.save()
            return redirect(f'/account/{profile.slug}')

    context = {
        "form": form,
        "page":page
    }
    return render(request, "recipes/recipes_form.html", context)





@login_required(login_url="signin")
def updateBlog(request, pk):
    page="updateblog"
    profile=request.user.profile
    blog=Blog.objects.filter(owner=profile).get(id=pk)
    form = BlogForm(instance=blog)
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect(f'/account/{profile.slug}')

    context = {
        "form": form,
        "page":page
    }
    return render(request, "recipes/recipes_form.html", context)



@login_required(login_url="signin")
def deleteBlog(request, pk):
    page="deleteBlog"
    profile=request.user.profile
    blog=Blog.objects.filter(owner=profile).get(id=pk)
    if request.method=='POST':
        blog.delete()
        return redirect(f'/account/{profile.slug}')
    context={
        "page":page
    }
    return render(request, "recipes/recipes_form.html", context)