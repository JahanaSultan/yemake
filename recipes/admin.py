from django.contrib import admin
from .models import Blog, Category, Review, Vote, RecipeBook

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display= ("title","category","slug","owner", "isActive")
    list_filter=("isActive","category","owner","cook_time","time", )
    search_fields=("title", "description")
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Vote)
admin.site.register(RecipeBook)