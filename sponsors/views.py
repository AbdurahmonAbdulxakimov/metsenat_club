from rest_framework import viewsets
from  rest_framework import permissions
from rest_framework.filters import SearchFilter

from sponsors.models import Sponsor
from sponsors.serializers import SponsorSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ['status', 'amount', 'updated_at'] 
    
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]