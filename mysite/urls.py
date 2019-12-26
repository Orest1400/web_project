"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from egames import views as egames_views


urlpatterns = [
    path('', egames_views.home, name='home'),
    path('contact/', egames_views.contact, name='contact'),
    path('game_review/', egames_views.game_review, name='game_review'),
    path('single_game_review/', egames_views.single_game_review, name='single_game_review'),
    path('post/', egames_views.post, name='post'),
    path('single_post/', egames_views.single_post, name='single_post'),
    path('admin/', admin.site.urls),
]

