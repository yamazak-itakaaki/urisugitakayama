from django.urls import path
from  .views import hinatazakaListView
from .views import hinatazakaProfileView
urlpatterns = [
    path("",hinatazakaListView),
    path("profile/<int:id>/",hinatazakaProfileView,name="hinatazaka-profile"),
]