from django.contrib import admin
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('', views.index , name='home'),
    path('home', views.home , name='home1'),
    path('about', views.about , name='about'),
    path('services', views.services , name='services'),
    path('contact', views.contact , name='contact'),
]
