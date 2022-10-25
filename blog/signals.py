from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from notification.models import ActiveBlog
from blog.models import Blog


def is_active_blog(sender, instance, *args, **kwargs):
        blog=instance
        admin=User.objects.get(is_superuser=True)
        if blog.isActive:
                notify=ActiveBlog(post=blog, sender=admin, user=blog.owner)
                notify.save()

post_save.connect(is_active_blog, sender=Blog)