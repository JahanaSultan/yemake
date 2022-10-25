from django.urls import path
from . import views


urlpatterns=[

path('isseen/',views.update_notification, name="updatenotification"),
path('isactiverecipeseen/', views.update_recipe_active, name="updaterecipeactiveseen"),
path('isactiveblogseen/', views.update_blog_active, name="updateblogactiveseen"),
]