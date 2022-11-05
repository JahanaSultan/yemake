
from django.forms import ModelForm
from .models import Blog, Review
from django import forms

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
    
    body=forms.CharField(widget=forms.Textarea, max_length=1000,)

