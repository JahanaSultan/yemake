from django.urls import path
from . import views


urlpatterns=[

path('isseen/',views.update_notification, name="updatenotification"),
]