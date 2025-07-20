import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from telegram import Update
from telegram.ext import Application # Or your custom bot handler

# Assuming 'application' is your python-telegram-bot Application instance
# initialized elsewhere (e.g., in your bot's __init__.py or a separate module)

@csrf_exempt
async def telegram_webhook_view(request):
    if request.method == 'POST':
        try:
            update_data = json.loads(request.body)
            update = Update.de_json(data=update_data, bot=application.bot)
            await application.update_queue.put(update)
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "GET requests not supported"}, status=405)
