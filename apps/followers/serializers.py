from rest_framework import serializers
from apps.followers.models import Follower
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role']

class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Follower
        fields = ['user', 'follower']
