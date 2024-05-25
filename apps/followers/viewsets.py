from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.followers.models import Follower
from apps.followers.serializers import FollowerSerializer, FollowerCreateSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all followers from the database
    queryset = Follower.objects.all()
    
    # Specify the serializer class to use for validating and deserializing input, and serializing output
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return FollowerCreateSerializer
        return FollowerSerializer
    
    # Set the permission classes to allow any user to access the view
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Retrieve the user ID and follower ID from the request data
        user_id = request.data.get('user')
        follower_id = request.data.get('follower')
        
        # Check if both user ID and follower ID are provided
        if not user_id or not follower_id:
            return Response({'error': 'Both user and follower IDs are required.'}, status=400)
        
        # Check if the user is trying to follow themselves
        if user_id == follower_id:
            return Response({'error': 'User cannot follow themselves.'}, status=400)
        
        # Check if the follower relationship already exists
        if Follower.objects.filter(user_id=user_id, follower_id=follower_id).exists():
            return Response({'error': 'This follower relationship already exists.'}, status=400)
        
        # Proceed with the default create behavior
        return super().create(request, *args, **kwargs)