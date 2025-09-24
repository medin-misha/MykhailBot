from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import Messages
from .keyboards import ReplyKeyboards
from .utils import save_user

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await save_user(chat_id=msg.chat.id, username=msg.from_user.username)
    await msg.reply(text=Messages.start, reply_markup=ReplyKeyboards.kb_start())
    await state.clear()


@router.message(Command("social"))
async def social_handler(msg: Message, state: FSMContext):
    await msg.answer(text=Messages.social, reply_markup=ReplyKeyboards.kb_social())
    await state.clear()
