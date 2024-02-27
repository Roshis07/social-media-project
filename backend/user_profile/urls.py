from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles_detail/<str:user__username>/', UserProfileDetail.as_view(), name='userprofile-detail'),
]
