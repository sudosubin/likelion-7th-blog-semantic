from django.contrib import admin
from django.urls import path, include
from .views import home_view, detail_view, new_view, edit_view, delete

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<int:post_id>/', detail_view, name='detail'),
    path('edit/<int:post_id>/', edit_view, name='edit'),
    path('delete/<int:post_id>/', delete, name='delete'),
    path('new/', new_view, name='new'),
]
