from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),  
    path('profiles/',views.users, name="contact"), 
    path('edit-account/', views.editAccount, name='edit-account'),path('user/<slug:slug>/',views.userAccount, name="Account"),  
    path('account/<slug:slug>/',views.myprofile, name="profile"),     
]
