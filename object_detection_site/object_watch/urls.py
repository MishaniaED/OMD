from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='object_watch-home'),
    path('about/', views.about, name='about-app'),
    path('settings/', views.settings, name='settings'),
]
