from django.urls import path
from . import views
from .views import karaokehomeView, karaokenetimeView

urlpatterns = [
    path("time/<int:number>/",karaokenetimeView, name='karaoke-time'),
    path("",karaokehomeView, name='karaoke-home'),
    


]