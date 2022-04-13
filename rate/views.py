from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer, GamesSerializer, ProfileSerializer, ProfileGameSerializer
from .models import Games, Profile
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class ProfileGameViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profiles = Profile.objects.filter(user=self.request.user)
        return profiles


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
