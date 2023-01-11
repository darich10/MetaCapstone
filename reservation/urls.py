from django.contrib import admin
from django.urls import path
from .views import say_hello
from . import views

urlpatterns = [
    # path('', say_hello, name='sayHello'),
    path('', views.index, name='index')
]