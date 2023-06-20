from django.contrib import admin
from django.urls import path, include
from . import views 
app_name = "users"



urlpatterns = [
    path("signup/", views.signup, name ="signup"),
    path("error/",views.error, name ="error"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout")
    ]