from django.shortcuts import render


def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')

'''
from django contrib.auth.models import User
from facultyapp.models import Marks
from adminapp.models import StudentList

def view_marks(request):
    user=request.user
    try:
        student_user=User.objects.get(username=user.username)
        student=StudenntList.objects.get








'''