from rest_framework import serializers
from apps.comments.models import Comment
from apps.users.models import User

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')  # Include user_id
    username = serializers.ReadOnlyField(source='user.username')  # Include username

    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user_id', 'username', 'created_at', 'updated_at']  # Make user_id and username read-only
        extra_kwargs = {
            'user': {'required': True},
            'article': {'required': True}
        }
