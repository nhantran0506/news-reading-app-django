from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer

class NotificationViewSets(viewsets.ModelViewSet):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer
  permission_classes = [AllowAny]