from django.contrib import admin
from django.urls import path, include, re_path
from app import views
from django.views.static import serve
from django_prometheus.views import get_metrics






urlpatterns = [
    path('', views.home, name='home'),
    path('metrics/', get_metrics),
]
