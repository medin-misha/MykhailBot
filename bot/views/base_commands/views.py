from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import Messages
from .keyboards import ReplayKeyboards

router = Router()


@router.message(CommandStart)
async def start_handler(msg: Message):
    # TODO: Create authentication user in system
    await msg.reply(text=Messages.start, reply_markup=ReplayKeyboards.kb_start())
