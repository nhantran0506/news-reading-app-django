from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all articles from the database
    queryset = Article.objects.all()
    
    # Specify the serializer class to use for validating and deserializing input, and serializing output
    serializer_class = ArticleSerializer
    
    # Set the permission classes to allow any user to access the view
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Retrieve the userID from the request's query parameters
        user_id = self.request.query_params.get('userID')
        
        # If a userID is provided, filter the articles by the specified user ID
        if user_id:
            return Article.objects.filter(user__id=user_id)
        
        # If no userID is provided, return the default queryset
        return super().get_queryset()
