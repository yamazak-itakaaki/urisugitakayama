from django.urls import path
from  .views import hinatazakaListView
from .views import hinatazakaProfileView
from .views import hinatazakaCreateView
from .views import hinatazakaDeleteView
from .views import hinatazakaUpdateFormView

urlpatterns = [
    path("",hinatazakaListView, name='hinatazaka-list'),
    path("profile/<int:id>/",hinatazakaProfileView,name="hinatazaka-profile"),
    path("delete/<int:pk>/", hinatazakaDeleteView, name="hinatazaka-delete"),
    path("form/",hinatazakaCreateView,name="hinatazaka-create"),
    path("update/<int:pk>/", hinatazakaUpdateFormView, name="hinatazaka-update"),
    path("delete/<int:id>/", hinatazakaDeleteView, name="hinatazaka-delete"),

]

  


