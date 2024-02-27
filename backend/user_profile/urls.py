from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/detail/', UserProfileDetail.as_view(), name='userprofile-detail'),
]
