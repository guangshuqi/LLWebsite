from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='job-home'),
    path('about/',views.about, name='job-about'),
]