from django.db import models

# Create your models here.
class Employee(models.Model):
    #ID is autogenerated in Django so I am not taking this field here
    name = models.CharField(max_length=50, blank=True, null=True)
    roll_no = models.CharField(max_length=20, blank=True, null=True)
    class_name = models.CharField(max_length=30,blank=True, null=True)