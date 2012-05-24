import urllib
import urllib2
import json

from django.conf import settings

from telegram.handlers.base import BasePlatformHandler


class WebserviceHandler(BasePlatformHandler):

    def handle(self):
        webservice_url = self.subscription.subscriptionmeta_set.get(
                key='webservice_url').value
        payload = json.dumps({
                'channel': self.subscription.channel.name,
                'subject': self.telegram.subject,
                'content': self.telegram.content
                })
        data = urllib.urlencode({'payload': payload})
        request = urllib2.Request(webservice_url, data)
        response = urllib2.urlopen(request)
