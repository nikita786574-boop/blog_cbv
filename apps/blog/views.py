from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Представление для вывода списка статей

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# Create your views here.
