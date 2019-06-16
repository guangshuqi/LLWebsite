from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="users-home"),
    path("about/", views.about, name="users-about"),
]
