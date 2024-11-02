from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model=AddCourse
        fields=['student','course', 'section']

from django import forms
from .models import *



class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']

