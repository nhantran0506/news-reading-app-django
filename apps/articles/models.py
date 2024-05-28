from django.db import models
from apps.users.models import User
from apps.category.enums import Category

class Article(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.TextField(null=True, blank=True)
    content = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.CharField(choices=Category.choices(), max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'
