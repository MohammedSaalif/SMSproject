from django.contrib.auth.models import User
from django.db import models

from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP','ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD','PYTHON FULL STACK DEVELOPMENT'),
    ]
    SECTION_CHOICES=[
        ('S1','SECTION 1'),
        ('S2','SECTION 2'),
        ('S3','SECTION 3'),
        ('S4','SECTION 4'),
        ('S5','SECTION 5'),
    ]
    student=models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course=models.CharField(max_length=50, choices=COURSE_CHOICES)
    section=models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICE = [
        ('AOOP', 'Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Developments'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICE)
    marks = models.IntegerField()
    def str(self):
        return f"{self.student.name} - {self.course}"








