from django.core.management.base import BaseCommand, CommandError

from telegram.models import Channel


class Command(BaseCommand):

    def handle(self, *args, **options):
        if len(args) > 2 or len(args) < 1:
            raise CommandError('Usage: python manage.py createchannel channel_name ["this is my channel description"]')
        channel_name = args[0]
        try:
            description = args[1]
        except IndexError:
            description = None
        try:
            channel = Channel.objects.get(name=channel_name)
            raise CommandError('Channel %s already exists' % channel_name)
        except Channel.DoesNotExist:
            channel = Channel(name=channel_name, description=description)
            channel.save()
        self.stdout.write('Channel %s was successfully created\n' % channel.name)
