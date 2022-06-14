from django.urls import path
from  .views import hinatazakaListView
urlpatterns = [
    path("",hinatazakaListView),
]