from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Sponsor(BaseModel):
    class Status(models.TextChoices):
        NEW = 'NW', 'New'
        IN_MODERATION = 'IM', 'In Moderation'
        PROVEN = 'PN', 'Proven'
    
    class Payment(models.TextChoices):
        CARD = 'CD', 'Card'
        BANK = 'BK', 'Bank'
        CASH = 'CH', 'Cash'
        
    
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    status = models.CharField(max_length=2, 
                              choices=Status.choices,
                              default=Status.NEW)
    
    amount = models.IntegerField()
    amount_paid = models.IntegerField(default=0)
    payment = models.CharField(max_length=2, 
                               choices=Payment.choices,
                               default=Payment.CARD)
    
    # If Individual then Save as "Individual". 
    # Otherwise as and organization name
    organization = models.CharField(max_length=255, blank=True)
    
    def amount_left(self):
        return self.amount - self.amount_paid
    
    def __str__(self) -> str:
        return self.title
    
    
