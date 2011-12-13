from django.contrib import admin
from telegram.models import *


class SubscriptionPlatformInline(admin.TabularInline):

    model = SubscriptionPlatform
    extra = 1


class SubscriptionAdmin(admin.ModelAdmin):

    fields = ('channel', 'level', 'disabled',)
    inlines = (SubscriptionPlatformInline,)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class PlatformAdmin(admin.ModelAdmin):

    pass


admin.site.register(Telegram)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(SubscriptionMeta)
admin.site.register(Channel)
admin.site.register(SubscriptionPlatform)
admin.site.register(SendLog)
