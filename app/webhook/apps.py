import asyncio
import requests
from aiogram import Bot
from django.apps import AppConfig
from django.conf import settings


# async def set_webhook_url():
#     bot = Bot(token=settings.BOT_TOKEN)
#     webhook_url = f"{settings.BASE_SITE}/webhook"
#     await bot.set_webhook(webhook_url)
#     await bot.close()

def set_webhook_url():
    bot_token = settings.BOT_TOKEN
    url_to_send_updates_to = f"{settings.BASE_SITE}/webhook/"
    url=f"https://api.telegram.org/bot{bot_token}/setWebhook?url={url_to_send_updates_to}"
    res = requests.post(url)
    print(res)


class WebhookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webhook'

    def ready(self):
        # asyncio.run(set_webhook_url())
        set_webhook_url()



# if __name__ == '__main__':
#     asyncio.run(set_webhook_url())