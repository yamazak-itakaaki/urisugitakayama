"""testPj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test.test, name='test'),
    path('hinatazaka/', include('hinatazaka.urls'))
    path('hinatazaka1/', include('hinatazaka.urls'))
    path('hinatazaka2/', include('hinatazaka.urls'))
    path('hinatazaka3/', include('hinatazaka.urls'))
    path('hinatazaka4/', include('hinatazaka.urls'))
    path('hinatazaka5/', include('hinatazaka.urls'))
    path('hinatazaka6/', include('hinatazaka.urls'))
    path('hinatazaka7/', include('hinatazaka.urls'))
    path('hinatazaka8/', include('hinatazaka.urls'))
    path('hinatazaka9/', include('hinatazaka.urls'))
]
