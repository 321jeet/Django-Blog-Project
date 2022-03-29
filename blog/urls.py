from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('comment/', views.postcomment,name='comment'),
    path('', views.blogHome,name='blogHome'),
    path('<str:slug>', views.blogPost,name='blogPost'),
    
]