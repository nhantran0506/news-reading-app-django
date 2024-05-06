from django.db import models
from apps.users.models import User

class Commission(models.Model):
  amount = models.FloatField(default=0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissions')

  class Meta:
    db_table = 'commissions'
