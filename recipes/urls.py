from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name="index"),
    path('recipes/', views.Recipes, name="recipes"),
    path('recipe-details/<slug:slug>', views.details, name="blogdetails"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('create-recipe/', views.createRecipe, name="blogcreate"),
    path('update-recipe/<str:pk>/', views.updateRecipe, name="update"),
    path('delete-recipe/<str:pk>/', views.deleteRecipe, name='delete'),
    path('category-filter/<slug:slug>',views.category_filter, name="recipe-category")
]