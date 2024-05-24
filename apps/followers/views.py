from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import Follower
from .serializers import UserSerializer

User = get_user_model()

@api_view(['GET'])
def followers_list(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return Response({"error": "user_id parameter is required"}, status=400)
    
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    
 
    followers = user.followers.all().select_related('follower')

    serializer = UserSerializer([f.follower for f in followers], many=True)
    return Response(serializer.data)

@api_view(['GET'])
def following_list(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return Response({"error": "user_id parameter is required"}, status=400)
    
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    following = Follower.objects.filter(follower=user).select_related('user')
    serializer = UserSerializer([f.user for f in following], many=True)
    return Response(serializer.data)
