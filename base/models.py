from django.db import models

from sponsors.models import Sponsor
from students.models import Student


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
class Credit(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='relations')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='relations')
    amount = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f'{self.sponsor.title} -> {self.student.title}' 