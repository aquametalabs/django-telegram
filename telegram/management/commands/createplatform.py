from django.core.management.base import BaseCommand, CommandError

from telegram.models import Platform

from telegram.utils import import_class


class Command(BaseCommand):

    def handle(self, *args, **options):
        if len(args) > 3 or len(args) < 2:
            raise CommandError('Usage: python manage.py createplatform platform_name path.to.Handler ["this is my platform description"]')
        platform_name = args[0]
        platform_handler = args[1]
        try:
            import_class(platform_handler)
        except:
            raise CommandError('Not a valid platform handler or it does not exist')
        try:
            description = args[2]
        except IndexError:
            description = None
        try:
            platform = Platform.objects.get(name=platform_name)
            raise CommandError('Platform %s already exists' % platform_name)
        except Platform.DoesNotExist:
            platform = Platform(name=platform_name, handler=platform_handler, description=description)
            platform.save()
        self.stdout.write('platform %s was successfully created\n' % platform.name)
