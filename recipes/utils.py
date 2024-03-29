from .models import Blog, Category
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchRecipe(request):
    search_query=""
    if request.GET.get("search_query"):
        search_query=request.GET.get("search_query")
    categories=Category.objects.filter(title__icontains=search_query)
    blogs = Blog.objects.distinct().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(category__in=categories))

    return blogs, search_query


def Paginations(request, blogs):
    page=request.GET.get("page")
    results=30
    paginator=Paginator(blogs, results)
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        page=1
        blogs=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        blogs=paginator.page(page)

    leftIndex=(int(page)-2)

    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+3)

    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1

    custom_range=range(leftIndex, rightIndex)
 
    return blogs, custom_range