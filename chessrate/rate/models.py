from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField("Rate", default=400)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    @receiver(post_save, sender=User)
    def create_user_profile(self, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(self, instance, **kwargs):
        instance.profile.save()


class Games(models.Model):
    whitePlayer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='+')
    blackPlayer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='+')
    winColor = models.CharField(verbose_name="End", max_length=10)
    dateOfGame = models.DateTimeField(verbose_name="Time of game", auto_now_add=True)
    moves = models.TextField(verbose_name="Moves", max_length=1000, default=0)

    def __str__(self):
        return self.winColor

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
