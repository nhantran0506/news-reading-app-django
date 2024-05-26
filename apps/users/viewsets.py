from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.users.models import User
from apps.users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = serializer.validated_data.get('password')
            if password:
                user.set_password(password)
                user.save()
            return Response({'message': 'User successfully created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        # Only allow updates to first_name, last_name, and role
        allowed_updates = ['first_name', 'last_name', 'role']
        for field in list(data.keys()):
            if field not in allowed_updates:
                data.pop(field)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        if serializer.is_valid():
            user = serializer.save()
            
            # Handle password separately
            if 'password' in request.data and request.data['password']:
                user.set_password(request.data['password'])
                user.save()
            else:
                original_user = User.objects.get(pk=user.pk)
                user.password = original_user.password
                user.save(update_fields=['password'])

            return Response({'message': 'User updated successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



