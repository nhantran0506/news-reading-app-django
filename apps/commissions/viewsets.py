from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.commissions.models import Commission
from apps.commissions.serializers import CommissionSerializer

class CommissionViewSet(viewsets.ModelViewSet):
  queryset = Commission.objects.all()
  serializer_class = CommissionSerializer
  permission_classes = [AllowAny]
