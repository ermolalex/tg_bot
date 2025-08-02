import json
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

# Initialize your Aiogram bot and dispatcher
BOT_TOKEN = settings.BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
user_router = Router()

@csrf_exempt
async def telegram_webhook(request):
    if request.method == 'POST':
        try:
            update = json.loads(request.body.decode('utf-8'))
            print("******* update", update)
            # Process the update using Aiogram's dispatcher
            await dp.process_update(types.Update(**update))
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return HttpResponse(status=405) # Method Not Allowed


# @user_router.message(CommandStart())
# async def cmd_start(message: Message) -> None:
#     user_id = message.from_user.id
#     print(f"Обрабатываем команду /start от пользователя с id={user_id}")
#     await message.answer(f"Hello пользователь с id={user_id}")

@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer('Привет!')

@dp.message()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi! I'm your Django-powered bot.")
#
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.reply(message.text)