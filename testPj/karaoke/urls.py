from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AccountRegistration.as_view(), name="karaoke-login"),#ログインページへのパス
    path("time/<int:number>/",)


]