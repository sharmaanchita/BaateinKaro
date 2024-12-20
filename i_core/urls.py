"""
URL configuration for i_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from ii_home.views import *
from ii_users.views import *
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile/", include("ii_users.urls")),
    path("accounts/", include("allauth.urls")),
    path("@<username>", profile_view, name="profile"),
    path("emailchange/", profile_emailchange, name="profile_emailchange"),
    
    path("", include("iii_chat.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
