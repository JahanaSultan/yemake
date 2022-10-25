from notification.models import Notification, ActiveRecipe, ActiveBlog
from users.models import Profile

def notification_count(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(username=request.user.username)
        notification=Notification.objects.filter(user=profile, is_seen=False)
        active_recipe=ActiveRecipe.objects.filter(user=profile, is_seen=False)
        active_blog=ActiveBlog.objects.filter(user=profile, is_seen=False)
        count=notification.count() + active_recipe.count() + active_blog.count()
        return {
          "push":notification,
          "active_recipe":active_recipe,
          "active_blog":active_blog,
          "not_count":count
        }
    else:
        return {
            "push": {},
            "active_recipe":{}
        }
