from django.db import models
from apps.users.models import User

class Notification(models.Model):
  content = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'notifications'
