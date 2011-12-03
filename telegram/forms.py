from django.forms import ModelForm
from telegram.models import Channel, Platform, Subscription


class ChannelForm(ModelForm):

    class Meta:
        model = Channel


class PlatformForm(ModelForm):

    class Meta:
        model = Platform


class SubscriptionForm(ModelForm):

    class Meta:
        model = Subscription
