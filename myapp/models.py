from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, blank=True)
