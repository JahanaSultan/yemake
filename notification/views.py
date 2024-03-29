from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from users.models import Profile
from .models import ActiveBlog, ActiveRecipe, Notification
from django.db.models import Q
# Create your views here.



def update_notification(request):
    profile=Profile.objects.get(username=request.user.username)
    if request.method=="GET":
        not_seen=Notification.objects.filter(Q(user=profile) & Q(is_seen=False))
        seen=Notification.objects.filter(Q(user=profile) & Q(is_seen=True))
        for notification in not_seen:
            notification.is_seen=True
            notification.save()
        for notification in seen:
            notification.delete()
        
        return redirect(request.META.get("HTTP_REFERER", "/"))

def update_recipe_active(request):
    profile=Profile.objects.get(username=request.user.username)
    if request.method=="GET":
        not_seen=ActiveRecipe.objects.filter(Q(user=profile) & Q(is_seen=False))
        seen=ActiveRecipe.objects.filter(Q(user=profile) & Q(is_seen=True))
        for notification in not_seen:
            notification.is_seen=True
            notification.save()
        for notification in seen:
            notification.delete()
        
        return redirect(request.META.get("HTTP_REFERER", "/"))


def update_blog_active(request):
    profile=Profile.objects.get(username=request.user.username)
    if request.method=="GET":
        not_seen=ActiveBlog.objects.filter(Q(user=profile) & Q(is_seen=False))
        seen=ActiveBlog.objects.filter(Q(user=profile) & Q(is_seen=True))
        for notification in not_seen:
            notification.is_seen=True
            notification.save()
        for notification in seen:
            notification.delete()
        
        return redirect(request.META.get("HTTP_REFERER", "/"))
