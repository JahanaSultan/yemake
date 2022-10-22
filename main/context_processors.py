from notification.models import Notification
from users.models import Profile

def notification_count(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(username=request.user.username)
        count=Notification.objects.filter(user=profile).count()
        return {
          "notification_count":count
        }
    else:
        return {
            "notification_count": 0
        }