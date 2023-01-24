from django.shortcuts import get_object_or_404, render
from posts.settings import num_posts

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Лев Николаевич Толстой'
    posts = Post.objects.all()[:num_posts]
    context = {
        'title': title,
        'text': text,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = "Записи сообщества " + group.title
    posts = Post.objects.filter(group=group)[:num_posts]
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, template, context)
