from notification.models import Notification
from users.models import Profile

def notification_count(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(username=request.user.username)
        notification=Notification.objects.filter(user=profile, is_seen=False)
        return {
          "push":notification
        }
    else:
        return {
            "push": {}
        }