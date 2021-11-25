from django.views.generic import ListView, DetailView
from .models import Post


class BloglistView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog_list.html'


class BlogdetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog_detail.html'
