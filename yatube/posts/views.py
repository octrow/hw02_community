from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Welcome to YaTube!'
    posts = Post.objects.all()[:settings.NUM_POSTS]
    context = {
        'title': title,
        'text': text,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    posts = Post.objects.filter(group=group)[:settings.NUM_POSTS]
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, template, context)
