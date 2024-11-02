from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title



class StudentList(models.Model):
        Register_Number = models.CharField(max_length=10,unique=True)
        Name = models.CharField(max_length=100)
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
        def __str__(self):
            return self.Register_Number


