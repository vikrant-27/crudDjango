from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    email=models.EmailField(max_length=30)
    
