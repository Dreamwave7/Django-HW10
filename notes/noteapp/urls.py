from django.urls import path
from . import views

app_name ="noteapp"

urlpatterns = [
    path("",views.main, name="main")
    ]