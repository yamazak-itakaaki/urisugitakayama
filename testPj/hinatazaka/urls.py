from django.urls import path
from  .views import hinatazakaListView
from .views import hinatazakaProfileView

from .views import hinatazakaCreateView

from .views import  hinatazakaDeleteView

urlpatterns = [
    path("",hinatazakaListView, name='hinatazaka-list'),
    path("profile/<int:id>/",hinatazakaProfileView,name="hinatazaka-profile"),
    path("form/",hinatazakaCreateView,name="hinatazaka-create"),
]

  


