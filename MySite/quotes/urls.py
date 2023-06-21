from django.contrib import admin
from django.urls import path, include
from . import views 
app_name = "quotes"

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<str:author_name>", views.author_bio, name = "author" ),
    path("add_author", views.add_author, name= "add_author"),
    path("add_quote", views.add_quote, name="add_quote")
    ]