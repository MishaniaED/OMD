from django.conf.global_settings import MEDIA_ROOT
from django.shortcuts import render
from .forms import ObjectRecognitionForm


# Прописать функцию для обработки запроса на отображения видео на главной странице и странице с настройками


def home(request):
    form = ObjectRecognitionForm()
    if request.method == 'POST':
        form = ObjectRecognitionForm(request.POST)
        if form.is_valid():
            frames = form.cleaned_data['frames']
            camera = form.cleaned_data['camera']
            # Здесь посылаем запрос на переключение камеры стриминнговому серверу
    return render(request, 'object_watch/home.html', {'title': 'Главная', 'camera_form': form, 'media': MEDIA_ROOT})


def about(request):
    return render(request, 'object_watch/about.html', {'title': 'Про нас'})


def settings(request):
    return render(request, 'object_watch/settings.html', {'title': 'Настройки'})
