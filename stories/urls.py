from django.urls import path
from .views import story_form
from stories import views

app_name = 'stories'

urlpatterns = [
    path('submit_story', views.story_form, name='story_form'),
    path('', views.stories_shared, name='stories_shared'),
    # path('<slug:slug>/', BlogdetailView.as_view(), name='blog_details'),
]
