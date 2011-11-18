class BaseHandler(object):

    def __init__(self, telegram, subscription, user=None):
        self.telegram = telegram
        self.subscription = subscription
        self.subscription_meta = subscription.subscriptionmeta_set.all()
        self.user = user

    def handle(self):
        raise NotImplementedError('`handle` needs to be defined')
