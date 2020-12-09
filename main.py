from urllib.parse import urljoin

import json5
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentTypes
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

API_TOKEN: str = os.environ["API_TOKEN"]  # 1231231231:SALAD12_SAddamsASASJDJAKSDJKSADASf
PROJECT_NAME: str = os.environ["PROJECT_NAME"]  # Set it as you've set TOKEN env var
HOST = "0.0.0.0"
PORT: str = os.environ["PORT"]

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/webhook/' + API_TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentTypes.ANY)
async def json_please(message: types.Message):
    await message.answer("<code>" + json5.dumps(message.to_python(), indent=4, ensure_ascii=False) + "</code>",
                         parse_mode="html")


async def on_startup(_):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info(dp)


async def on_shutdown(_):
    logging.info(dp)


if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_URL_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=HOST, port=PORT)
