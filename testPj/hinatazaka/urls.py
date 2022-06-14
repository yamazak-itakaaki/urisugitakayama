from django.urls import path
from  .views import hinatazakaListView
urlpatterns = [
    path("",hinatazakaProfileView),
    path("profile/<int:number>/",hinatazakaProfileView,name="hinatazaka-profile"),
]