from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, custom_logout


urlpatterns = [
    path('register/', RegisterView.as_view(),name="register_user"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', custom_logout, name='logout'),
]
