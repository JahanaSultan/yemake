from django.urls import path
from . import views


urlpatterns=[
   path('blogs/', views.blog, name="blogs"),
   path('create-blog/',views.createBlog, name="createblog"),
   path('blog-details/<slug:slug>', views.details, name="blogdetail"),
   path('update-blog/<str:pk>/', views.updateBlog, name="updateblog"),
   path('delete-blog/<str:pk>/', views.deleteBlog, name="deleteBlog"),
]