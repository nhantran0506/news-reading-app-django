from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Follower
from .serializers import UserSerializer

User = get_user_model()

class FollowersListView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
        followers = user.followers.all().select_related('follower')
        serializer = UserSerializer([f.follower for f in followers], many=True)
        return Response(serializer.data)

class FollowingListView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        following = user.users.all().select_related('user')
        serializer = UserSerializer([f.user for f in following], many=True)
        return Response(serializer.data)
