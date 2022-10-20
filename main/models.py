from django.db import models
from django.utils import timezone
# Create your models here.

class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering= ["-created_date"]
        verbose_name="Email İzləyici"
        verbose_name_plural="Email İzləyicilər"
