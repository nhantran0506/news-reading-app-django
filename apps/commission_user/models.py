from django.db import models
from apps.commissions.models import Commission
from apps.users.models import User

class CommissionUser(models.Model):
  commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commission_users')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commission_users')

  class Meta:
    db_table = 'commission_user'
    unique_together = (('commission', 'user'),)
