from django.db.models import Sum

from rest_framework import viewsets, permissions, views
from rest_framework.response import Response 

from base.models import Credit
from base.serializers import CreditSerializer, DashboardSerializer

from sponsors.models import Sponsor
from students.models import Student


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [permissions.IsAuthenticated]
    
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
    

class DashboardView(views.APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format=None):
        total_paid_qs = Credit.objects.aggregate(Sum('amount'))
        total_required_qs = Student.objects.aggregate(Sum('fee'))
        total_paid = total_paid_qs.get('amount__sum')
        total_required = total_required_qs.get('fee__sum')
        total_left = total_required - total_paid

        return Response(data={'total_paid': total_paid, 'total_required': total_required, 'total_left': total_left})