from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album, name="album"),
    path('<int:image_id>', views.imgdetail, name="detail"),
    path('newalbum/', views.albumpost, name="newalbum"),
]