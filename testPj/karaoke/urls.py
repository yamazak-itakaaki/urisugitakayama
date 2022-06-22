from django.urls import path
from . import views
from .views import karaokehomeView, karaokeinputView, karaokeroomView, karaokenetimeView

urlpatterns = [
    path("",karaokehomeView, name='karaoke-home'),
    path("input/", karaokeinputView, name='karaoke-input'),
    path("room/", karaokeroomView, name='karaoke-room'),
    path("time/<int:number>/",karaokenetimeView, name='karaoke-time'),
]