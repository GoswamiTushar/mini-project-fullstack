from django.urls import path
from .views import story_upload
from stories import views

app_name = 'stories'

urlpatterns = [
    path('story/', views.story_upload, name='story_form'),
    # path('<slug:slug>/', BlogdetailView.as_view(), name='blog_details'),
]
