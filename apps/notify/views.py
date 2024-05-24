from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
from apps.users.models import User




@api_view(['GET'])
def user_notifications(request):
    # Extract the user_id from the request's query parameters
    user_id = request.GET.get('user_id')
    
    # Check if user_id is provided
    if not user_id:
        # Return a response with error message if user_id is missing
        return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Attempt to retrieve the user object with the provided user_id
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        # If the user does not exist, return a response indicating the error
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Retrieve notifications for the specified user
    notifications = Notification.objects.filter(recipient=user)
    
    # Serialize the notifications using NotificationSerializer
    serializer = NotificationSerializer(notifications, many=True)
    
    # Return a response with the serialized data
    return Response(serializer.data)