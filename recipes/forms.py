from cProfile import label
from dataclasses import fields
from turtle import title
from django.forms import ModelForm
from .models import Blog, Review


class RecipeForm(ModelForm):
    class Meta:
        model=Blog
        fields=['image','title', 'description',  'category', 'cook_time', 'time', 'youtube_link']
        labels = {
            "title": "Yeməyin adı",
            "description":"Resept",
            "image":"Şəkil Yüklə",
            "category":"Kateqoriyası",
            "cook_time":"Bişirilmə zamanı",
            "time":"Vaxt Ölçüsü",
            "youtube_link":"Youtube Linki"
        }

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['body']
        labels={
            "body":""
        }

