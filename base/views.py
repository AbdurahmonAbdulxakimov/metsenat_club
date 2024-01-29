from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from base.models import Credit
from base.serializers import CreditSerializer

from sponsors.models import Sponsor
from students.models import Student


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    
    def perform_create(self, serializer):
        sponsor_id = serializer.validated_data.get('sponsor').id
        student_id = serializer.validated_data.get('student').id
        amount_sponsored = serializer.validated_data.get('amount')
        
        student = Student.objects.get(id=student_id)
        sponsor = Sponsor.objects.get(id=sponsor_id)
        
        student.fee_paid += amount_sponsored
        sponsor.amount_paid += amount_sponsored
        
        student.save()
        sponsor.save()
        
        return super().perform_create(serializer)