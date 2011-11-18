from telegram.handlers.base import BaseHandler


class DummyHandler(BaseHandler):

    def handle(self):
        print 'handling that sucker'
