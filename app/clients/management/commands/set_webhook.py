import requests
from django.core.management.base import BaseCommand
from django.conf import settings


# logger = create_logger(logger_name=__name__)

class Command(BaseCommand):
    help = 'Set TG Webhook'

    def handle(self, *args, **options):
        """
        set webhook     POST https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
        delete webhook  https://api.telegram.org/bot{my_bot_token}/setWebhook?url=
        get webhook     GET https://api.telegram.org/bot{my_bot_token}/getWebhookInfo

        :return:
        """
        bot_token = settings.BOT_TOKEN
        url_to_send_updates_to = f"{settings.BASE_SITE}/webhook/"
        url = f"https://api.telegram.org/bot{bot_token}/setWebhook?url={url_to_send_updates_to}"
        res = requests.post(url)
        print(res)
