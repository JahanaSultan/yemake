from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from users.models import Profile
from .models import Notification
# Create your views here.

def show_notifications(request):
    user=Profile.objects.get(username=request.user.username)

    notifications=Notification.objects.filter(user=user).order_by('-date')
    template=loader.get_template("notifications.html")

    context={
        "notifications":notifications
    }
    return HttpResponse(template.render(context, request))
