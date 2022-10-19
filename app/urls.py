from django.contrib import admin
from django.urls import path, include, re_path
from app import views
from django.views.static import serve





urlpatterns = [
    path('', views.home, name='home'),
]
