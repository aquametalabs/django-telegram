class BaseChannelHandler(object):

    def __init__(self, telegram, channel, level):
        self.telegram = telegram
        self.channel = channel
        self.level = level

    def handle(self):
        raise NotImplementedError('`handle` needs to be defined')


class BasePlatformHandler(object):

    def __init__(self, telegram, subscription, platform, user=None, **kwargs):
        self.telegram = telegram
        self.subscription = subscription
        self.subscription_meta = subscription.subscriptionmeta_set.all()
        self.platform = platform
        self.user = user
        self.extra = kwargs

    def handle(self):
        raise NotImplementedError('`handle` needs to be defined')
