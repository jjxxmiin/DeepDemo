from django import forms
from demo.models import Demo


class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = ['subject', 'content', 'framework', 'task', 'url']
        labels = {
            'subject': 'Title',
            'content': 'Content',
            'framework': 'Framework',
            'task': 'Task',
            'url': 'URL',
        }