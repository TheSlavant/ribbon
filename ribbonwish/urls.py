from django.conf.urls import url, include


from django.views.generic import TemplateView
from accounts.views import (login_view, register_view, logout_view, home_view)

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="signup.html"), name='index'),
    url(r'^$', register_view, name='index'),
    url(r'^login/', login_view, name = 'login'),
    url(r'^home/', home_view, name = 'home')
]
