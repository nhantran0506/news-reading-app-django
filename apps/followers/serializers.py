from rest_framework import serializers
from apps.followers.models import Follower

class FollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follower
    fields = '__all__'


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role']
