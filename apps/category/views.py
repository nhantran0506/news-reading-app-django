# views.py in your articles app
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.articles.models import Article
from .serializers import ArticleSerializer
from apps.category.enums import Category

@api_view(['GET'])
def articles_by_category(request):
    # Retrieve the category_name from the request's query parameters
    category_name = request.GET.get('category_name')
    
    # Check if category_name is provided
    if not category_name:
        return Response({'error': 'category_name parameter is required'}, status=400)
    
    # Initialize the category_value to None
    category_value = None
    
    # Loop through the Category enum to find the matching category value
    for category in Category:
        if category.name.lower() == category_name.lower():
            category_value = category.value
            break
    
    # If no matching category is found, return an error response
    if category_value is None:
        return Response({'error': 'Invalid category name'}, status=400)
    
    # Filter articles by the found category value
    articles = Article.objects.filter(category=category_value)
    
    # Serialize the filtered articles
    serializer = ArticleSerializer(articles, many=True)
    
    # Return the serialized articles in the response
    return Response(serializer.data)

