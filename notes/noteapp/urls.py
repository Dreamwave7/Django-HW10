from django.urls import path
from . import views

app_name = "noteapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("tag/", views.tag, name="tag"),
    path("note/",views.note, name="note")
    ]