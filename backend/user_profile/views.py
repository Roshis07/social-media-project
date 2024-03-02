from rest_framework import generics, permissions

from .models import Profile
from .serializers import ProfileSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return user_profile

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
