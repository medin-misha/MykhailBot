from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
from utils.print_live_table import LiveTableDraw

from .keyboard import build_info_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Command("table"))
async def create_table(msg: Message):
    table = LiveTableDraw(name="misha", birthday_date="03/09/2008")
    image = table.create_table()


    # await msg.answer(text="text", reply_markup=build_info_kb())
    #

    await msg.bot.send_document(
        chat_id=msg.chat.id,
        document=BufferedInputFile(
            file=image.getvalue(),
            filename="table.png"
        )
    )
