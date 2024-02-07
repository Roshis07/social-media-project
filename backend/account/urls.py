from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(),name="register_user"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    ]
