from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import (login_view, register_view, logout_view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('ribbonwish.urls')),
    url(r'^login/', login_view, name = 'login')
    # url(r'^$', views.register, name='index'),
    # url(r'^feed/', views.feed, name ='feed'),
    # url(r'^register/', views.register, name='signup'),
]
