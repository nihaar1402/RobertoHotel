from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('discover',views.discover,name='discover'),
     path('contact',views.contact,name='contact'),
     path('about',views.about,name='about'),
     path('room',views.room,name='room')
]
