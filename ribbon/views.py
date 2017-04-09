#coding=utf-8

from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

# def index(request):
#     return render(request, 'ribbonwish/signup.html', {})
# #    return HttpResponse("hello")

# def feed(request):
#     return render(request, 'ribbonwish/login.html', {})
#
# from django.contrib.auth import authenticate, login
#
#
# from ribbonwish.forms import UserForm
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect, HttpResponse
#
# def register(request):
#
#
#     registered = False
#
#
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         # profile_form = UserProfileForm(data=request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#
#
#             user.set_password(user.password)
#             user.save()
#
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#
#
#             # if 'picture' in request.FILES:
#             #     profile.picture = request.FILES['picture']
#
#             profile.save()
#
#
#             registered = True
#
#
#         else:
#             print user_form.errors, profile_form.errors
#
#
#     else:
#         user_form = UserForm()
#         # profile_form = UserProfileForm()
#
#
#     return render(request,
#             'ribbonwish/signup.html',
#             {'user_form': user_form,  'registered': registered} )
#
#
# def user_login(request):
#
#
#
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#
#         user = authenticate(username=username, password=password)
#
#
#         if user:
#
#             if user.is_active:
#
#                 login(request, user)
#                 return HttpResponseRedirect('/ribbonwish/feed')
#             else:
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
#
#
#     #else:
#
#         return render(request, 'ribbonwish/login.html', {})
