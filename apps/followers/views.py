from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import Follower
from .serializers import FollowerSerializer, UserSerializer, FollowerCreateSerializer

User = get_user_model()

@api_view(['GET'])
def followers_list(request):
    # Extract the user_id from the request's query parameters
    user_id = request.GET.get('user_id')
    
    # Check if user_id is provided
    if not user_id:
        # Return a response with error message if user_id is missing
        return Response({"error": "user_id parameter is required"}, status=400)
    
    try:
        # Attempt to retrieve the user object with the provided user_id
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        # If the user does not exist, return a response indicating the error
        return Response({"error": "User not found"}, status=404)
    
    # Retrieve followers of the user and prefetch related follower objects
    followers = Follower.objects.filter(user=user).select_related('follower')
    
    # Serialize the follower objects using FollowerSerializer
    serializer = FollowerSerializer(followers, many=True)
    
    # Return a response with the serialized data
    return Response(serializer.data)


@api_view(['GET'])
def following_list(request):
    # Extract the user_id from the request's query parameters
    user_id = request.GET.get('user_id')
    
    # Check if user_id is provided
    if not user_id:
        # Return a response with error message if user_id is missing
        return Response({"error": "user_id parameter is required"}, status=400)
    
    try:
        # Attempt to retrieve the user object with the provided user_id
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        # If the user does not exist, return a response indicating the error
        return Response({"error": "User not found"}, status=404)

    # Retrieve users whom the specified user is following
    following = Follower.objects.filter(follower=user).select_related('user')
    
    # Serialize the following users using UserSerializer
    serializer = UserSerializer([relation.user for relation in following], many=True)
    
    # Return a response with the serialized data
    return Response(serializer.data)




from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.followers.models import Follower
from apps.followers.serializers import FollowerSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return FollowerCreateSerializer
        return FollowerSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        follower_id = request.data.get('follower')
        
        if not user_id or not follower_id:
            return Response({'error': 'Both user and follower IDs are required.'}, status=400)
        
        if user_id == follower_id:
            return Response({'error': 'User cannot follow themselves.'}, status=400)
        
        return super().create(request, *args, **kwargs)