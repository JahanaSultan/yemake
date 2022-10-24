from django.contrib import admin
from .models import Blog, Category, Review, Vote, RecipeBook

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display= ("title","category","slug","owner", "isActive")
    list_filter=("isActive","category","owner","cook_time","time", )
    search_fields=("title", "description")
class CategoryAdmin(admin.ModelAdmin):
    list_display= ("title","slug","id")
    list_filter=("slug", "title")
    search_fields=("title", "slug")

class modelAdmin(admin.ModelAdmin):
    list_display= ("recipe", "owner")
    search_fields=("recipe", "owner")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review,modelAdmin)
admin.site.register(Vote,modelAdmin)
admin.site.register(RecipeBook, modelAdmin)