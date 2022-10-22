from random import choices
from django.db import models
from users.models import Profile
from recipes.models import Blog

# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES=((1, "Like"),(2, "Comment"), (3, "RecipeBook"), (4,  "isActive"))

    post=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="post_noti", blank=True, null=True)
    sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="send_noti")
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="get_noti")
    notification_type=models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview=models.CharField(max_length=90,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    is_seen=models.BooleanField(default=False)

    def __str__(self):
        return str(self.post)
    



