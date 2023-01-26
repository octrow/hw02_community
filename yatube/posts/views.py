from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:settings.NUM_POSTS]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:settings.NUM_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
