# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from ribbonwish.models import User
from accounts.forms import UserLoginForm
from accounts.forms import UserRegisterForm
from accounts.forms import UserChangeForm


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserRegisterForm

    list_display = [
        'birth_data',
        'email',
        'first_name',
        'is_admin',
        'last_name',
    ]

    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'avatar',
                'birth_data',
                'first_name',
                'last_name',
            )
        }),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'birth_data',
                'email',
                'password1',
                'password2'
            )
        }),
    )

    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Register your models here.
