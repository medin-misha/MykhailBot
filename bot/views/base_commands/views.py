from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import Messages
from .keyboards import ReplyKeyboards

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message):
    # TODO: Create authentication user in system
    await msg.reply(text=Messages.start, reply_markup=ReplyKeyboards.kb_start())

@router.message(Command("social"))
async def social_handler(msg: Message):
    await msg.reply(text=Messages.social, reply_markup=ReplyKeyboards.kb_social())