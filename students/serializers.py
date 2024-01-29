from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'title', 'phone', 'university', 'type', 'fee', 
                  'created_at', 'updated_at']
