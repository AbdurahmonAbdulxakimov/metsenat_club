from rest_framework import serializers

from base import models
from students.models import Student
from sponsors.models import Sponsor


class CreditSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        fee_left = Student.objects.get(id=data.get('student').id).fee_left()
        sponsor_left = Sponsor.objects.get(id=data.get('sponsor').id).amount_left()
        
        if data.get('amount') > fee_left or data.get('amount') > sponsor_left:
            raise serializers.ValidationError('Possible amount of sponsorship did not match!')
        return data
        
    
    class Meta:
        model = models.Credit
        fields = ['sponsor', 'student', 'amount', 'created_at', 'updated_at']