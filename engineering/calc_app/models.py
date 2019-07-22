from django.db import models
import datetime
from django import forms

# Create your models here.

class Rectangle(models.Model):
    rec_width = models.DecimalField(max_digits=10, decimal_places=2)
    rec_height = models.DecimalField(max_digits=10, decimal_places=2)
    date_recorded = models.DateField(auto_now=True)
    
class FanUnbalance(models.Model):
    BALANCE_CHOICE =['1','2.5','6.3']
    balance_grade= models.CharField(max_length=10, choices= [(x,x) for x in BALANCE_CHOICE], default = '2.5')
    impeller_mass = models.DecimalField(max_digits=10, decimal_places=2)
    fan_speed = models.DecimalField(max_digits=10, decimal_places=2)
    backplate_dia = models.DecimalField(max_digits=10, decimal_places=2)
