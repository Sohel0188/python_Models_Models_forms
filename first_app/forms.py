from django import forms
from first_app.models import Teachers

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'
        labels = {
            'name' : 'Teacher Name',
            'subject' : 'Subject Name',
            'id' : "Teacher Id"        
            }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : 'Write your full name'
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }
    