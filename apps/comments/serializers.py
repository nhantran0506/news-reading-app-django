from rest_framework import serializers
from apps.comments.models import Comment
from apps.users.serializers import UserSerializer  # Import the UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    # Include the user serializer to retrieve the username
    user = UserSerializer(read_only=True)
    username = serializers.ReadOnlyField(source='user.username')  # Add the username field

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'username']  # Make username read-only
        extra_kwargs = {
            'user': {'required': True},
            'article': {'required': True}
        }
