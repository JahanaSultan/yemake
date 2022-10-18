from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    username=models.CharField(max_length=100, null=True, blank=True)
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True, unique=True)
    short_info=models.CharField(max_length=200, null=True, blank=True)
    profile_image=models.ImageField(upload_to='Users', null=True, blank=True,default='Users/user-default.jpg')
    cover_image=models.ImageField(upload_to='Users', blank=True, null=True, default='Users/cover.webp')
    slug=models.SlugField( verbose_name="Slug", null=True, unique=True)

    def __str__(self) -> str:
        return str(self.slug)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)



 
