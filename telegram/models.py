from django.db import models
from django.contrib.auth.models import User

LEVEL_CHOICES = (
        (1, 'DEBUG'),
        (2, 'INFO'),
        (3, 'SUCCESS'),
        (4, 'WARNING'),
        (5, 'ERROR'),
        (6, 'CRITICAL'),
)


class Subscription(models.Model):

    user = models.ForeignKey(User)
    message_channel = models.ForeignKey('Channel')
    level = models.IntegerField(default=2,
            choices=LEVEL_CHOICES)
    platforms = models.ManyToManyField('Platform',
            through='SubscriptionPlatform')
    disabled = models.BooleanField(default=False)


class Channel(models.Model):

    name = models.CharField(max_length=255)


class Platform(models.Model):

    name = models.CharField(max_length=255)
    handler = models.CharField(max_length=255)


class SubscriptionPlatform(models.Model):

    subscription = models.ForeignKey('Subscription')
    platform = models.ForeignKey('Platform')


class Telegram(models.Model):

    channel = models.ForeignKey('Channel')
    content = models.TextField()
    level = models.IntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField()

class SendLog(models.Model):

    telegram = models.ForeignKey('Telegram')
    subscription_platform = models.ForeignKey('SubscriptionPlatform')
    sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
