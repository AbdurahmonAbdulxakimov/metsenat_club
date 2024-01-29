from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter

from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ['type', 'university'] 

    permission_classes = [permissions.IsAuthenticated]
   