from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Import for authentication
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)# Ensure user is authenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user of UserProfile to the currently logged-in user

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    