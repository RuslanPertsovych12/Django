from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_name, name='hello_name'),
]

