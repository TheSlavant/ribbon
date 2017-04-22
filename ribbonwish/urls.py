from django.conf.urls import url, include


from rest_auth.registration.views import RegisterView, VerifyEmailView
from django.contrib.auth import views as auth_views

from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name='index'),
    # url(r'^feed/', views.feed, name ='feed'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # URLs that do not require a session or valid token
    # url(r'^password/reset/$', PasswordResetView.as_view(),
    #     name='rest_password_reset'),
    # url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
    #     name='rest_password_reset_confirm'),
    # url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # # URLs that require a user to be logged in with a valid session / token.
    # url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    # url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    # url(r'^password/change/$', PasswordChangeView.as_view(),
    #     name='rest_password_change'),

    # url(r'^$', views.index, name='index'),
    # url(r'^feed/', views.feed, name ='feed'),
    # url(r'^register/', views.register, name='register'),
]
