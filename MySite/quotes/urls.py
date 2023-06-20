from django.contrib import admin
from django.urls import path, include
from . import views 
app_name = "quotes"

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<str:author_name>", views.author_bio, name = "author" )
    ]