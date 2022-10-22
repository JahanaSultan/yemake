from venv import create
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from notification.models import Notification
from recipes.models import Vote


def user_liked_post(sender, instance, *args, **kwargs):
        like=instance
        notify=Notification(post=like.recipe, sender=like.owner, user=like.recipe.owner, notification_type=1)
        notify.save()

def user_unlike_post(sender, instance, *args, **kwargs):
        like=instance
        notify=Notification.objects.filter(post=like.recipe, sender=like.owner, notification_type=1)
        notify.delete()




post_save.connect(user_liked_post, sender=Vote)
post_delete.connect(user_unlike_post, sender=Vote)