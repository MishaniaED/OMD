from django.shortcuts import render


def home(request):
    context = {
        'posts': 'some info'
    }
    return render(request, 'object_watch/home.html', context)


def about(request):
    return render(request, 'object_watch/about.html', {'title': 'Про нас'})