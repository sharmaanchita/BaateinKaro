from .views import *
from django.urls import path

urlpatterns = [
    path("", profile_view, name= "profile")
]
