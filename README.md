Overview
========

Django Telegram is yet another messaging framework for django. It uses a channel methodology and you send messages to subscribers of those
channels by broadcasting.

Pull requests are quite welcome!


Usage
=====

## Installation ##

1. `pip install django-telegram`

2. Edit your `settings.py:`

    ```
    INSTALLED_APPS += ("telegram",)
    ```

4. Add in the urls:

    ```
    urlpatterns += patterns('',          
        url(r'telegram/',   include('telegram.urls',  namespace='telegram',  app_name='telegram') ),
    )
    ```

## Configuration ##

1. Optional:

    * `TELEGRAM_FORCE_QUEUEING` - Boolean True/False. This option will ignore the add_to_queue=False option when broadcasting to a channel.

    * `TELEGRAM_EMAIL_HANDLER_FROM` - String. This will be the from address when using the email handler.

## Use it ##

Using telegram is a matter of setting up channels, subscribing to those channels, telling the subscription what platforms you would like to
receive notifications on, and finally broadcasting messages to channels.

There are a few things you need to do to get started. This current development version uses the django admin to set things up. Eventually 
I (pull requests are welcome)  will build and interface that can be styled and used within your application.

1. Channels: A channel is what a user subscribes to to get messages about a certain type of system or data. To create a channel, go to the 
Django admin and navigate to telegram. Add a new channel and give it a name, description and optionally a handler.

    * Channel handlers are inherited 
    from `telegram.handlers.base.BaseChannelHandler` and must implement a `handle(self)` method. This method is called when you broadcast to a channel 
    and expects a Subscription query set to be returned.


2. Platforms:

    * Handlers:

    * Included Handlers:

3. Subscriptions:

4. Subscription meta data:

5. 

Credits
=======
django-telegram was written by Kyle Terry for Aquameta.
