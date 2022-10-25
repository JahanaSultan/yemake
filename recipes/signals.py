
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from notification.models import ActiveRecipe, Notification
from recipes.models import Vote,Review, Blog


def user_liked_post(sender, instance, *args, **kwargs):
        like=instance
        notify=Notification(post=like.recipe, sender=like.owner, user=like.recipe.owner, notification_type=1)
        notify.save()

def user_unlike_post(sender, instance, *args, **kwargs):
        like=instance
        notify=Notification.objects.filter(post=like.recipe, sender=like.owner, notification_type=1)
        if notify:
           notify.delete()

def user_comment_post(sender, instance, *args, **kwargs):
        comment=instance
        if comment.owner != comment.recipe.owner:
                notify=Notification(post=comment.recipe, sender=comment.owner, user=comment.recipe.owner, notification_type=2)
                notify.save()

def user_delete_comment_post(sender, instance, *args, **kwargs):
        comment=instance
        notify=Notification.objects.filter(post=comment.recipe, sender=comment.owner, notification_type=2)
        if notify:
           notify.delete()

def is_active_recipe(sender, instance, *args, **kwargs):
        recipe=instance
        admin=User.objects.get(is_superuser=True)
        if recipe.isActive:
                notify=ActiveRecipe(post=recipe, sender=admin, user=recipe.owner)
                notify.save()


post_save.connect(user_liked_post, sender=Vote)
post_save.connect(user_comment_post, sender=Review)
post_save.connect(is_active_recipe, sender=Blog)
post_delete.connect(user_unlike_post, sender=Vote)
post_delete.connect(user_delete_comment_post, sender=Review)