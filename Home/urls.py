# -*- coding: utf-8 -*-

from django.urls import path
from Home import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services')]
