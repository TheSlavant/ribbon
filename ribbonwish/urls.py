from django.conf.urls import url, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.register, name='index'),
    url(r'^feed/', views.feed, name ='feed'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    # url(r'^$', views.index, name='index'),
    # url(r'^feed/', views.feed, name ='feed'),
    # url(r'^register/', views.register, name='register'),
]
