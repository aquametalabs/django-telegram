from telegram.models import (Telegram, SendLog, Channel, LEVEL_CHOICES,
        Subscription)
from telegram.exceptions import ChannelDoesNotExist, LevelDoesNotExist


def send_telegram(channel, subject, message, level):
    try:
        channel = Channel.objects.get(name=channel)
    except Channel.DoesNotExist:
        raise ChannelDoesNotExist('Channel %s does not exist. Cannot proceed'
                ' with sending the message.')
    existing_level = None
    for lvl in LEVEL_CHOICES:
        if lvl[0] == level:
            existing_level = level
        else:
            continue
    if not existing_level:
        raise LevelDoesNotExist('Level %s does not exist. Cannot proceed'
                ' with sending the message.')
    return _build_telegrams(channel, subject, message, existing_level)


def _build_telegrams(channel, subject, message, level):
    telegram = Telegram(subject=subject, message=Message, level=level)
    telegram.save()
    subscriptions = Subscription.objects.filter(channel=channel, level=level)
    for subscription in subscriptions:
        for sub_plat in Subscription.subscriptionplatform_set.all():
            send_log = SendLog(
                    telegram=telegram,
                    subscription_platform=sub_plat
            )
            send_log.save()
