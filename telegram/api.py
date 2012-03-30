from datetime import datetime

from django.conf import settings

from telegram.models import (Telegram, SendLog, Channel, LEVEL_CHOICES,
        Subscription)
from telegram.exceptions import ChannelDoesNotExist, LevelDoesNotExist
from telegram.utils import import_class


FORCE_QUEUEING = getattr(settings, 'TELEGRAM_FORCE_QUEUEING', False)


def send_telegram(channel, subject, message, level='INFO', add_to_queue=True, **kwargs):
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
    return _build_telegrams(channel, subject, message, existing_level, add_to_queue=add_to_queue, **kwargs)


def _build_telegrams(channel, subject, message, level, add_to_queue, **kwargs):
    telegram = Telegram(
            subject=subject,
            content=message,
            level=level,
            channel=channel,
            additional_arguments=kwargs)
    telegram.save()
    if channel.handler:
        handler = import_class(channel.handler)(telegram, channel, level)
        subscriptions = handler.handle()
    else:
        subscriptions = Subscription.objects.filter(
                channel=channel, level__gte=level, disabled=False)
    for subscription in subscriptions:
        for sub_plat in subscription.subscriptionplatform_set.all():
            send_log = SendLog(
                    telegram=telegram,
                    subscription_platform=sub_plat
            )
            send_log.save()
            if not FORCE_QUEUEING:
                if not add_to_queue:
                    _send_now(send_log)


def send_all_unsent_telegrams():
    send_logs = SendLog.objects.filter(sent=False)
    for send_log in send_logs:
        _send_now(send_log)


def _send_now(send_log):
    platform = send_log.subscription_platform.platform
    subscription = send_log.subscription_platform.subscription
    telegram = send_log.telegram
    handler = import_class(platform.handler)
    handler = handler(telegram, subscription, platform, **telegram.additional_arguments)
    handler.handle()
    send_log.sent = True
    send_log.sent_at = datetime.now()
    send_log.save()
