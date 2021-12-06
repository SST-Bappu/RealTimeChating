from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('register/',registerUser,name='registration'),
    path('login/',Userlogin,name='login'),
    path('room',generateRoom,name='room'),
    path('chat',send,name='chat'),
    path('getChat<str:room_id>/',getMessage,name='getchat')
]