# # -*- coding: utf-8 -*-
# from django.contrib.auth.tests.utils import skipIfCustomUser
# from django.contrib.auth.tests.custom_user import CustomUser, ExtensionUser
# from django.test import TestCase, override_settings
#
#
# class ApplicationTestCase(TestCase):
#     @skipIfCustomUser
#     def test_normal_user(self):
#         "Run tests for the normal user model"
#         self.assertSomething()
#
#     @override_settings(AUTH_USER_MODEL='auth.CustomUser')
#     def test_custom_user(self):
#         "Run tests for a custom user model with email-based authentication"
#         self.assertSomething()
#
#     @override_settings(AUTH_USER_MODEL='auth.ExtensionUser')
#     def test_extension_user(self):
#         "Run tests for a simple extension of the built-in User."
#         self.assertSomething()