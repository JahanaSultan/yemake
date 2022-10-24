from tabnanny import verbose
from django.db import models
from recipes.helper import seo
from django.utils.crypto import get_random_string
from users.models import Profile
from embed_video.fields  import  EmbedVideoField
from django_quill.fields import QuillField



# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(null=True,upload_to='Category')
    slug=models.SlugField(editable=False, verbose_name="Slug", null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kargs):
        if Category.objects.filter(title=self.title):
            self.slug=seo(self.title)+get_random_string(length=4)
        else:
            self.slug = seo(self.title)
        super().save(arg,kargs)
    
    class Meta:
        verbose_name="Kateqoriya"
        verbose_name_plural="Kateqoriyalar"


class Blog(models.Model):
    sn = 'saniyə'
    deq = 'dəqiqə'
    s = 'saat'
    g = 'gün'

    TIME_CHOICES = [
        (sn, "saniyə"),
        (deq, 'dəqiqə'),
        (s, 'saat'),
        (g, 'gün'),
       
    ]
    title = models.CharField(verbose_name="Başlıq",max_length=1500)
    description = QuillField(verbose_name="Açıqlama")
    image=models.ImageField(verbose_name="Şəkil",null=True, blank=True, default='Recipes/default.jpg', upload_to='Recipes')
    isActive=models.BooleanField(verbose_name="Aktivlik",default=False)
    category= models.ForeignKey(Category,verbose_name="Kateqoriya", on_delete=models.CASCADE)
    slug=models.SlugField(editable=False, verbose_name="Slug", null=True, unique=True)
    cook_time=models.IntegerField(verbose_name="Bişirilmə Vaxtı",null=True)
    time=models.CharField(verbose_name="Zaman Ölçüsü",max_length=10, choices=TIME_CHOICES, default=deq, null=True)
    created=models.DateTimeField("Yaradılma Vaxtı",auto_now_add=True, null=True)
    youtube_link=EmbedVideoField("Youtube Linki",null=True, blank=True)
    owner=models.ForeignKey(Profile,verbose_name="Postu Paylaşan", null=True, on_delete=models.SET_NULL)
    
    def save(self, *arg, **kargs):
        if Blog.objects.filter(title=self.title):
            self.slug=seo(self.title)+get_random_string(length=4)
        else:
            self.slug = seo(self.title)
        super().save(arg,kargs)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering= ["-created"]
        verbose_name="Resept"
        verbose_name_plural="Reseptlər"


class Review(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(Blog ,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    class Meta:
        ordering=["-created"]
        verbose_name="Şərh"
        verbose_name_plural="Şərhlər"

class Vote(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        unique_together=[["owner", "recipe"]]
        verbose_name="Bəyənmə"
        verbose_name_plural="Bəyənmələr"

    def __str__(self):
        return self.recipe.title



class RecipeBook(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    recipe=models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.recipe.owner)
    class Meta:
        unique_together=[["owner", "recipe"]]
        verbose_name="Resept Dəftəri"
        verbose_name_plural="Resept Dəftəri"
    