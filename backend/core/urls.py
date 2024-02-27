"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('user_profile/', include("user_profile.urls")),
]
