from .views import *
from django.urls import path

urlpatterns = [
    path("", profile_view, name= "profile"),
    path("edit/", edit_profile_view, name= "edit_profile"),
    path("onboarding/", edit_profile_view, name= "profile_onboarding"),
    path("settings/" , setting_view, name="profile_settings"),
    path("verifyemail/", profile_emailverify, name= "profile_emailverify"),
    path("delete/", profile_delete, name= "profile_delete"),
]
