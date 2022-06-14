from django.urls import path
from  .views import hinatazakaListView
from .views import hinatazakaProfileView
from .views import  hinatazakaDeleteView
urlpatterns = [
    path("",hinatazakaListView),
    path("profile/<int:id>/",hinatazakaProfileView,name="hinatazaka-profile"),
    path("delete/<int:pk>/", hinatazakaDeleteView, name="hinatazaka-delete"),
]
