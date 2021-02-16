from django.shortcuts import render

# blog/views.py
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    paginate_by = 18
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
