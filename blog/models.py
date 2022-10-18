from email.policy import default
from django.db import models
from blog.helper import seo
from django.utils.crypto import get_random_string
from users.models import Profile
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Category(models.Model):
    title=models.CharField(max_length=250)
    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    image= image=models.ImageField(default='Blog/default.png', upload_to='Blog', null=True)
    isActive=models.BooleanField(default=False)
    inSlide=models.BooleanField(default=False)
    slug=models.SlugField(editable=False, verbose_name="Slug", unique=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    owner=models.name = models.ForeignKey(Profile, related_name='blogown', on_delete=models.CASCADE, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def save(self, *arg, **kargs):  
        if Blog.objects.filter(title=self.title):
            self.slug=seo(self.title)+get_random_string(length=4)
        else:
            self.slug = seo(self.title)
        super().save(arg,kargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["-created"]