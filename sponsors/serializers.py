from rest_framework import serializers
from sponsors.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'title', 'phone', 'status', 'amount', 'payment', 
                  'organization', 'created_at', 'updated_at']
