from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display= ("title","category","slug","owner", "isActive")
    list_filter=("isActive","category","owner" )
    search_fields=("title", "description")

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)