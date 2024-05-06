from django.db import models
from apps.users.models import User
from apps.articles.models import Article

class Comment(models.Model):
  content = models.TextField(blank=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'comments'
