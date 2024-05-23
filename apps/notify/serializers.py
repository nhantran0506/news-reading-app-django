from rest_framework import serializers
from apps.users.models import User
from apps.articles.models import Article
from .models import Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'user', 'created_at', 'updated_at']

class NotificationSerializer(serializers.ModelSerializer):
    follower = UserSerializer(source='recipient', read_only=True)
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['message', 'follower', 'article', 'timestamp']
