from django.shortcuts import render
from . import forms


def story_upload(request):
    # story_form = forms.StoryForm()
    if request.method == 'POST':
        story_form = forms.StoryForm(request.POST)
        if story_form.is_valid():
            story_form.save()
    return render(request, "story_detail.html")
