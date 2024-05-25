from rest_framework import serializers
from apps.followers.models import Follower
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role']

class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()

    class Meta:
        model = Follower
        fields = ['id', 'follower']


class FollowerCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    follower = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follower
        fields = ['user', 'follower']