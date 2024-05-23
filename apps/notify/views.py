from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
from apps.users.models import User




@api_view(['GET'])
def user_notifications(request):
    user_id = request.GET.get('user_id')

    if not user_id:
        return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    notifications = Notification.objects.filter(recipient=user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)