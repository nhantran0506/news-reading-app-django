from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.followers.models import Follower
from apps.followers.serializers import FollowerSerializer

class FollowerViewSet(viewsets.ModelViewSet):
  queryset = Follower.objects.all()
  serializer_class = FollowerSerializer
  permission_classes = [AllowAny]
