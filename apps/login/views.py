from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import UserSerializer

class LoginView(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request=self.request, username=username, password=password)
    if user is not None:
      user_serializer = UserSerializer(user)
      return Response(user_serializer.data, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
