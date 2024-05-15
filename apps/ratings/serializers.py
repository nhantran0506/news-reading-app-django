from rest_framework import serializers
from apps.ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = '__all__'
    read_only_fields = ['created_at', 'updated_at']
    extra_kwargs = {
      'user': {'required': True},
      'article': {'required': True}
    }
