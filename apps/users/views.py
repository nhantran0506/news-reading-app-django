from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import ForgotPasswordSerializer, ResetPasswordSerializer

class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            reset_code = serializer.save()
            return Response({'reset_code': reset_code}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password reset successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
