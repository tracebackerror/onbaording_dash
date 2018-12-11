from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone



class ParentTicket(models.Model):
    parent_ticket = models.CharField(max_length=200)
    
    def __str__(self):
        return self.parent_ticket

STATUS_CHOICES = (
    ('inqueue','In Queue'),
    ('pending','Pending'),
    ('onhold', 'On Hold'),
    ('complete','Complete'),
)

class SubTicket(models.Model):
    onboarding_id = models.ForeignKey(ParentTicket, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=200)
    
    tracking_status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='inqueue')

    def __str__(self):
        return self.tracking_number
        
        
