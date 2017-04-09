from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ribbonwish.urls')),
    # url(r'^$', views.register, name='index'),
    # url(r'^feed/', views.feed, name ='feed'),
    # url(r'^register/', views.register, name='signup'),
]
