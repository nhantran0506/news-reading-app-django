from rest_framework import serializers
from apps.commission_user.models import CommissionUser

class CommissionUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CommissionUser
    fields = '__all__'
