from django.db import models
from apps.users.models import User

class Article(models.Model):
  title = models.CharField(max_length=255, blank=False)
  content = models.TextField(blank=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'articles'
