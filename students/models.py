from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Student(BaseModel):
    class University(models.TextChoices):
        PTU = 'PTU', 'Pharmaceutical Technical University'
        TEAM = 'TEAM', 'TEAM University'
        TSPU = 'TSPU', 'Tashkent State Pedagogical University'
        WIUT = 'WIUT', 'Westminster International University in Tashkent'
    
    class Type(models.TextChoices):
        BS = 'BS', 'Bachelors'
        PG = 'PG', 'Post Graduate'
        
    
    title = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    
    university = models.CharField(max_length=4, 
                              choices=University.choices,
                              default=University.WIUT)
    type = models.CharField(max_length=4, 
                               choices=Type.choices,
                               default=Type.BS)
    
    fee = models.IntegerField()
    fee_paid = models.IntegerField(default=0)
    
    
    def fee_left(self):
        return self.fee - self.fee_paid
    
    def __str__(self) -> str:
        return self.title
    
    
