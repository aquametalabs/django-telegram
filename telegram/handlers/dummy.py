from telegram.handlers.base import BaseHandler


class DummyHandler(BaseHandler):

    def handle(self):
        print 'Channel: %s' % self.telegram.channel.name
        print 'Subject: %s' % self.telegram.subject
        print 'Message: %s' % self.telegram.content
        print 'Level: %s' % self.subscription.get_level_display()
