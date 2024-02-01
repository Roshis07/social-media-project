
from django.urls import path, include
from .views import Register
urlpatterns = [
    path('Register/', Register.as_view(),name="reegister-user"),
]
