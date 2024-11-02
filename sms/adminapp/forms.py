from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
      class Meta:
         model=Task
         fields=['title']


from django import forms
from .models import StudentList
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


