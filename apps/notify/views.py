# apps/notify/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer, UserSerializer
from apps.users.models import User
from apps.articles.models import Article
from apps.followers.models import Follower

class ArticlePublishNotificationView(APIView):
    def get(self, request, user_id, articles_title):
        try:
            editor = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "Editor not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            article = Article.objects.get(title=articles_title)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

       
        followers = User.objects.filter(followers__user=editor)

        
        notifications = []
        for follower in followers:
            notification = Notification.objects.create(
                recipient=follower,
                message=f"New article '{articles_title}' published by {editor.username}",
                article=article
            )
            notifications.append(notification)

        
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
