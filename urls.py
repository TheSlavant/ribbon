from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^', include('ribbonwish.urls')),
#    url(r'^register/', views.register, name='register'),
]
