from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='object_watch-home'),
    path('about/', views.about, name='about-app'),
    path('settings/', views.settings, name='settings'),
    # path('update_camera_selection/', views.update_camera_selection, name='update_camera_selection')
]
