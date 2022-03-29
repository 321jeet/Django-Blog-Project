from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('search/', views.search,name='search'),
    path('singup/', views.singup,name='singup'),
    path('login/', views.handellogin,name='login'),
    path('logout/', views.handellogout,name='logout'),
]