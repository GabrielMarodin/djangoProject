from django.urls import path

from . import views


app_name = 'chat'
urlpatterns = [
    path('', views.join, name='join'),
    path('<str:room_name>/', views.room, name='room'),
]