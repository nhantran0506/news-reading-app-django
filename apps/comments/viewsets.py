from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [AllowAny]
