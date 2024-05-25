from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def get(self, request):
        # Return an error message indicating that only POST requests are accepted
        return Response(
            {
                'error': 'This endpoint only accepts POST requests. Please send your credentials in a POST request with the following fields.',
                'example': {
                    'username': 'f0o',
                    'password': 'b4r'
                }
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def post(self, request):
        # Extract the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user with the provided credentials
        user = authenticate(request=self.request, username=username, password=password)
        
        if user is not None:
            # If authentication is successful, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            # If authentication fails, return an error message
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


