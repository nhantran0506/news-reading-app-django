from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import Follower
from .serializers import FollowerSerializer, UserSerializer

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
