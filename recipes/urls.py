from django.urls import path
from . import views


urlpatterns=[
    path('recipes/', views.Recipes, name="recipes"),
    path('recipe-details/<slug:slug>', views.details, name="blogdetails"),
    path('comment/',views.add_comment, name="recipecomment"),
    path('delete-comment/<str:pk>/',views.delete_comment, name="deletecomment"),
    path('create-recipe/', views.createRecipe, name="blogcreate"),
    path('update-recipe/<str:pk>/', views.updateRecipe, name="update"),
    path('delete-recipe/<str:pk>/', views.deleteRecipe, name='delete'),
    path('category-filter/<slug:slug>',views.category_filter, name="recipe-category"),
    path('time-filter/',views.time_filter, name="recipe-time"),
    path('video-filter/',views.video_filter, name="recipe-video"),
    path('add-recipe-book/', views.recipe_book_add,name="recipebook"),
    path('add-like/', views.recipe_like_add,name="like"),
]