from django.shortcuts import render
from . import forms
from datetime import datetime
from django.contrib import messages
from .models import Story


def story_form(request):
    # story_form = forms.StoryForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('story')
        name = request.POST.get('name')
        story_form = Story(title=title, body=body,
                           name=name)
        story_form.save()
        messages.success(request, "Thank you for submitting your story")
    return render(request, "story_form.html")


def stories_list(request):
    stories = Story.objects.all()
    return render(request, "story_list.html", {'stories': stories})
