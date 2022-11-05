from django.db import models
from users.models import Profile
from recipes.models import Blog as Recipe
from blog.models import Blog 
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES=((1, "Like"),(2, "Comment"))

    post=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="post_noti", blank=True, null=True)
    sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="send_noti", blank=True)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="get_noti")
    notification_type=models.IntegerField(choices=NOTIFICATION_TYPES)
    date=models.DateTimeField(auto_now_add=True)
    is_seen=models.BooleanField(default=False)

    def __str__(self):
        return str(self.post)

class ActiveRecipe(models.Model):
    post=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.post)
    

class ActiveBlog(models.Model):
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.post)