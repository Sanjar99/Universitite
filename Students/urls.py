from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.groups_list , name= 'groups_list' ),
]