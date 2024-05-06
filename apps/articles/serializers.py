from rest_framework import serializers
from apps.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ['created_at', 'updated_at']
    extra_kwargs = {
      'user': {'required': True}
    }
