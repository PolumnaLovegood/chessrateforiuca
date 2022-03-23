from django.contrib.auth.models import User, Group
from .models import Profile, Games
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ("whitePlayer", "blackPlayer", "winColor", "dateOfGame", "moves")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'nickname', 'rate')
