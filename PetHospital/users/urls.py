# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 10:16
# @Author  : jasonWang
# @FileName: urls.py
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # ex: /users/
    path('login/', views.login,name = 'login'),
    path('', views.verify_user, name='verify_user'),
]