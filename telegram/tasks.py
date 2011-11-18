from celery.decorators import task

from telegram.api import send_all_unsent_telegrams


@task
def offload_sending_of_telegrams():
    send_all_unsent_telegrams()
