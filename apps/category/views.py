# views.py in your articles app
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.articles.models import Article
from .serializers import ArticleSerializer
from apps.category.enums import Category

@api_view(['GET'])
def articles_by_category(request):
    category_name = request.GET.get('category_name')
    if not category_name:
        return Response({'error': 'category_name parameter is required'}, status=400)
    
    category_value = None
    for category in Category:
        if category.name.lower() == category_name.lower():
            category_value = category.value
            break
    
    if category_value is None:
        return Response({'error': 'Invalid category name'}, status=400)
    
    articles = Article.objects.filter(category=category_value)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
