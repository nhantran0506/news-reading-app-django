from django.db import models
from apps.users.models import User
from apps.articles.models import Article

class Rating(models.Model):
  rating = models.FloatField(default=0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'ratings'
    unique_together = (('user', 'article'),)
