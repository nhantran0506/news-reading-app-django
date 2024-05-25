from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all comments from the database
    queryset = Comment.objects.all()
    
    # Specify the serializer class to use for validating and deserializing input, and serializing output
    serializer_class = CommentSerializer
    
    # Set the permission classes to allow any user to access the view
    permission_classes = [AllowAny]

