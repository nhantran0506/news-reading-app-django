from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
from apps.users.models import User
from apps.articles.models import Article

@api_view(['GET'])
def article_publish_notification(request):
    user_id = request.GET.get('user_id')
    articles_title = request.GET.get('articles_title')

    if not user_id or not articles_title:
        return Response({"error": "user_id and articles_title parameters are required"}, status=status.HTTP_400_BAD_REQUEST)

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
