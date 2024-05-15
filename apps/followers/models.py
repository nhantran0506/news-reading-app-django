from django.db import models
from apps.users.models import User

class Follower(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

  class Meta:
    db_table = 'followers'
    unique_together = (('user', 'follower'),)
