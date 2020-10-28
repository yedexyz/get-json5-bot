import json5
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentTypes
from aiogram.utils import executor

API_TOKEN: str = os.environ["API_TOKEN"]  # 1231231231:SALAD12_SAddamsASASJDJAKSDJKSADASs

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentTypes.ANY)
async def json_please(message: types.Message):
    await message.answer("<code>" + json5.dumps(message.to_python(), indent=4, ensure_ascii=False) + "</code>",
                         parse_mode="html")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
