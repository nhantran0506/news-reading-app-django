from rest_framework import serializers
from apps.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'user', 'category', 'created_at', 'updated_at']
