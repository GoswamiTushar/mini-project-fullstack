from django.urls import path
from .views import BloglistView, BlogdetailView

app_name = 'blog'

urlpatterns = [
    path('', BloglistView.as_view(), name='blog_list'),
    path('<slug:slug>/', BlogdetailView.as_view(), name='blog_detail'),
]
