from datetime import datetime

from telegram.models import (Telegram, SendLog, Channel, LEVEL_CHOICES,
        Subscription)
from telegram.exceptions import ChannelDoesNotExist, LevelDoesNotExist
from telegram.utils import import_class


def send_telegram(channel, subject, message, level):
    try:
        channel = Channel.objects.get(name=channel)
    except Channel.DoesNotExist:
        raise ChannelDoesNotExist('Channel %s does not exist. Cannot proceed'
                ' with sending the message.' % channel)
    existing_level = None
    for lvl in LEVEL_CHOICES:
        if lvl[1] == level.upper():
            existing_level = lvl[0]
            break
        else:
            continue
    if not existing_level:
        raise LevelDoesNotExist('Level %s does not exist. Cannot proceed'
                ' with sending the message.' % level)
    return _build_telegrams(channel, subject, message, existing_level)


def _build_telegrams(channel, subject, message, level):
    telegram = Telegram(
            subject=subject,
            content=message,
            level=level,
            channel=channel)
    telegram.save()
    subscriptions = Subscription.objects.filter(
            channel=channel, level=level, disabled=False)
    for subscription in subscriptions:
        for sub_plat in subscription.subscriptionplatform_set.all():
            send_log = SendLog(
                    telegram=telegram,
                    subscription_platform=sub_plat
            )
            send_log.save()


def send_all_unsent_telegrams():
    send_logs = SendLog.objects.filter(sent=False)
    for send_log in send_logs:
        platform = send_log.subscription_platform.platform
        subscription = send_log.subscription_platform.subscription
        telegram = send_log.telegram
        handler = import_class(platform.handler)
        handler = handler(telegram, subscription, platform)
        handler.handle()
        send_log.sent = True
        send_log.sent_at = datetime.now()
        send_log.save()
