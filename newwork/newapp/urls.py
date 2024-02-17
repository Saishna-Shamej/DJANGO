"""
URL configuration for newwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('guesthome',views.guesthome, name='guesthome'),
    path('ownerhome', views.ownerhome, name='ownerhome'),
    path('guestsignup', views.guestsignup, name='guestsignup'),
    path('ownersignup', views.ownersignup, name='ownersignup'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('upload1',views.upload1,name='upload1'),
    path('upload',views.upload,name='upload'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),
    path('edit_file/<int:pk>/', views.edit_file, name='edit_file'),
    path('view_file/<int:pk>/', views.view_file, name='view_file'),
]
