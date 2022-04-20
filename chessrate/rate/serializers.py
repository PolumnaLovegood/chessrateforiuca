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
    whitePlayer = serializers.StringRelatedField(many=False)
    blackPlayer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Games
        fields = ("blackPlayer", "whitePlayer", "winColor", "dateOfGame", "moves")


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    url = serializers.HyperlinkedIdentityField(view_name='profiles_games', read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'rate', 'RD', 'url')


class ProfileGameSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    games = GamesSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'rate', 'games')
