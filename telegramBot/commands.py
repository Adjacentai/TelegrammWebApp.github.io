from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.reply("Hello! Click the button below to open the Web App.")
