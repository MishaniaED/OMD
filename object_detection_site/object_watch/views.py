from django.http import JsonResponse
from django.shortcuts import render


# def update_camera_selection(request):
#     selected_value = request.POST.get('selected_value')
#     # Обратиться к стриминговому сервису за видео и в случае успешного обращения отдать его в качестве ответа
#     # return render(request, 'object_watch/home.html/camera-number', context)
#     return JsonResponse({'success': True})


def home(request):
    context = {
        'posts': 'some info'
    }
    return render(request, 'object_watch/home.html', context)


def about(request):
    return render(request, 'object_watch/about.html', {'title': 'Про нас'})


def settings(request):
    return render(request, 'object_watch/settings.html', {'title': 'Настройки'})
