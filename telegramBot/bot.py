import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, WebAppInfo, MenuButtonWebApp

from commands import router

load_dotenv()

TOKEN = getenv("TOKEN_API")

if TOKEN is None:
    raise ValueError("No token provided. Please set the TOKEN_API environment variable.")

bot = Bot(token=TOKEN)
# All handlers should be attached to the Router
dp = Dispatcher()
dp.include_router(router)

async def set_web_app_menu_button(bot: Bot):
    # URL
    web_app_url = 'https://adjacentai.github.io/TelegrammWebApp.github.io/docs/index.html'

    # MenuButtonWebApp
    menu_button = MenuButtonWebApp(
        text='Open Web App',
        web_app=WebAppInfo(url=web_app_url)
    )

    # MenuButtonWebApp
    await bot.set_chat_menu_button(menu_button=menu_button)


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
