from .views import *
from django.urls import path

urlpatterns = [
    path("", profile_view, name= "profile"),
    path("edit/", edit_profile_view, name= "edit_profile"),
    path("onboarding/", edit_profile_view, name= "profile_onboarding"),
]
