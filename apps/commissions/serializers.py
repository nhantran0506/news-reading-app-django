from rest_framework import serializers
from apps.commissions.models import Commission

class CommissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Commission
    fields = '__all__'
