from rest_framework import serializers
from apps.articles.models import Article
from apps.roles.enums import Roles
from apps.comments.serializers import CommentSerializer
from apps.users.serializers import UserSerializer
import base64
from django.core.files.base import ContentFile

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user_id = serializers.ReadOnlyField(source='user.id') 
    username = serializers.ReadOnlyField(source='user.username')
    

    def create(self, validated_data):
        user = validated_data['user']
        allowed_roles = [role.value for role in Roles if role != Roles.Reader]

        if user.role not in allowed_roles:
            raise serializers.ValidationError("This user does not have the permission to create articles.")
        return super().create(validated_data)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'user_id', 'username']  
        extra_kwargs = {
            'user': {'required': True}
        }
