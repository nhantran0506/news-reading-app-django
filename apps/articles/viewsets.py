from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.articles.models import Article
from apps.articles.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  permission_classes = [AllowAny]
