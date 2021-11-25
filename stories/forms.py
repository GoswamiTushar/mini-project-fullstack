from django import forms
from .models import Story


class StoryForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100)
