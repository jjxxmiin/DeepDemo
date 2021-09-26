from django import forms
from demo.models import Demo


class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = ['photo', 'subject', 'content', 'framework', 'task']
        labels = {
            'photo': 'Photo',
            'subject': 'Title',
            'content': 'Content',
            'framework': 'Framework',
            'task': 'Task',
        }