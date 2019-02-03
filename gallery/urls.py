from django.contrib import admin
from django.urls import path, include
from .views import home_view, new_view

app_name = 'gallery'

urlpatterns = [
    path('', home_view, name='home'),
    path('new/', new_view, name='new'),
]
