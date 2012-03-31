from django.core.mail import send_mail
from django.conf import settings

from telegram.handlers.base import BasePlatformHandler
from telegram.models import PlatformMeta


class EmailHandler(BasePlatformHandler):

    def handle(self):
        """
        Will try to use settings.TELEGRAM_EMAIL_HANDLER_FROM,
        the platformmeta setting "subject_prepend", and the subscriptionmeta
        setting "email_address".
        """
        try:
            meta = self.platform.platformmeta_set.get(key='subject_prepend')
            subject = '%s: %s' % (meta.value, self.telegram.subject)
        except PlatformMeta.DoesNotExist:
            subject = self.telegram.subject
        try:
            from_address = self.platform.platformmeta_set.get(key='from_address').value
        except PlatformMeta.DoesNotExist:
            from_address = settings.TELEGRAM_EMAIL_HANDLER_FROM
        send_mail(
                subject,
                self.telegram.content,
                from_address,
                [self.subscription.subscriptionmeta_set.get(key='email_address').value])

