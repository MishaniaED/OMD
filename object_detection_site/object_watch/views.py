from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'object_watch/home.html', context)


def about(request):
    return render(request, 'object_watch/about.html', {'title': 'О клубе Python Bytes'})