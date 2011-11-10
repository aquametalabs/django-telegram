class BaseHandler(object):

    def __init__(self, message, subject=None):
        self.message = message
        self.subject = subject

    def handle(self):
        raise NotImplementedError('`handle` needs to be defined')
