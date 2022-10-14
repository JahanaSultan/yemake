from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def Paginations(request, blogs):
    page=request.GET.get("page")
    results=18
    paginator=Paginator(blogs, results)
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        page=1
        blogs=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        blogs=paginator.page(page)

    leftIndex=(int(page)-4)

    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+5)
    
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1

    custom_range=range(leftIndex, rightIndex)
    
    return blogs, custom_range