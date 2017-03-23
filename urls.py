from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feed/', views.feed, name ='feed'),
    url(r'^register/', views.register, name='register'),
]
