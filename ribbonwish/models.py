from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings

from ribbonwish.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True, db_index=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_data = models.DateField('birth_data', null=True, blank=True)
    is_admin = models.BooleanField('is_admin', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        return self.email
        # send_mail(subject, message, from_email, [self.email], **kwargs)


# class Course(models.Model):
#     slug = models.SlugField(max_length=100)
#     name = models.CharField(max_length=100)
#     tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Friendship(models.Model):
    from_friend = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='friend_set'
    )
    to_friend = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_friend_set'
    )


    def __str__(self):
        return '%s, %s' % (
            self.from_friend.email,
            self.to_friend.email
        )

    class Admin:
        pass

    class Meta:
        unique_together = (('to_friend', 'from_friend'),)

# class UserProfile(models.Model):
#     #
#     user = models.OneToOneField(User)
#
#     #
# #    website = models.URLField(blank=True)
# #     picture = models.ImageField(upload_to='profile_images', blank=True)
#
#     #
#     def __unicode__(self):
#         return self.user.username


