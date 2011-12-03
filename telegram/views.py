from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from telegram.forms import ChannelForm, PlatformForm, SubscriptionForm
from telegram.models import Channel, Platform, Subscription


def channel_new(request, template_name='telegram/channel_new.html',
        form_class=ChannelForm):
    form = ChannelForm()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)


def channel_create(request, form_class=ChannelForm):
    if request.method != 'POST':
        return HttpResponseNotFound
    form = ChannelForm(data=request.POST)
    if form.is_valid():
        channel = form.save()
        return HttpResponseRedirect(reverse('telegram_channel_view'))


def channel_view(request, channel_id, template_name='telegram/channel_view.html'):
    channel = get_object_or_404(Channel, pk=channel_id)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'channel': channel}, context_instance=context)


def channel_list(request, template_name='telegram/channel_list.html'):
    channels = Channel.objects.all()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'channels':channels}, context_instance=context)


def channel_edit(request, channel_id, template_name='telegram/channel_edit.html',
        form_class=ChannelForm):
    channel = get_object_or_404(Channel, pk=channel_id)
    form = ChannelForm(instance=channel)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)


def channel_update(request, channel_id, form_class=ChannelForm):
    if request.method != 'POST':
        return HttpResponseNotFound


def channel_delete(request, channel_id):
    channel = get_object_or_404(Channel, pk=channel_id)
    channel.delete()
    return HttpResponseRedirect(reverse('telegram_channel_list'))


def platform_new(request, template_name='telegram/platform_new.html',
        form_class=PlatformForm):
    form = PlatformForm()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)


def platform_create(request, form_class=PlatformForm):
    if request.method != 'POST':
        return HttpResponseNotFound
    form = PlatformForm(data=request.POST)
    if form.is_valid():
        platform = form.save()
        return HttpResponseRedirect(reverse('telegram_platform_view'))


def platform_view(request, platform_id, template_name='telegram/platform_view.html'):
    platform = get_object_or_404(Platform, pk=platform_id)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'platform': platform}, context_instance=context)


def platform_list(request, template_name='telegram/platform_list.html'):
    platforms = Platform.objects.all()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'platforms':platforms}, context_instance=context)


def platform_edit(request, platform_id, template_name='telegram/platform_edit.html',
        form_class=PlatformForm):
    platform = get_object_or_404(Platform, pk=platform_id)
    form = PlatformForm(instance=platform)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)


def platform_update(request, platform_id, form_class=PlatformForm):
    if request.method != 'POST':
        return HttpResponseNotFound


def platform_delete(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id)
    platform.delete()
    return HttpResponseRedirect(reverse('telegram_platform_list'))


def subscription_new(request, template_name='telegram/subscription_new.html',
        form_class=SubscriptionForm):
    form = SubscriptionForm()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)


def subscription_create(request, form_class=SubscriptionForm):
    if request.method != 'POST':
        return HttpResponseNotFound
    form = SubscriptionForm(data=request.POST)
    if form.is_valid():
        subscription = form.save()
        return HttpResponseRedirect(reverse('telegram_subscription_view'))


def subscription_view(request, subscription_id, template_name='telegram/subscription_view.html'):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'subscription': subscription}, context_instance=context)


def subscription_list(request, template_name='telegram/subscription_list.html'):
    subscriptions = Subscription.objects.all()
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'subscriptions':subscriptions}, context_instance=context)


def subscription_edit(request, subscription_id, template_name='telegram/subscription_edit.html',
        form_class=SubscriptionForm):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    form = SubscriptionForm(instance=subscription)
    context = RequestContext(request)
    return render_to_response(template_name=template_name,
            dictionary={'form': form}, context_instance=context)

def subscription_update(request, subscription_id, form_class=SubscriptionForm):
    if request.method != 'POST':
        return HttpResponseNotFound


def subscription_delete(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    subscription.delete()
    return HttpResponseRedirect(reverse('telegram_subscription_list'))
