from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
from aiogram.fsm.context import FSMContext
from utils.print_live_table import LiveTableDraw
from config import Messages
from .states import GetUserBirthDateForTable
from .utils import create_table, send_table_or_error, get_user_by_chat_id, reformat_user_date

router = Router()


@router.message(Command("table"))
async def get_date_for_table(msg: Message, state: FSMContext):
    await msg.answer(text=Messages.table_get_birthday)
    await state.set_state(GetUserBirthDateForTable.get_date)


@router.message(GetUserBirthDateForTable.get_date, F.text)
async def create_table_by_date(msg: Message, state: FSMContext):
    table_data: dict = create_table(date=msg.text, username=msg.from_user.username)
    await send_table_or_error(table_data=table_data, msg=msg, state=state)



@router.message(GetUserBirthDateForTable.get_date)
async def create_by_date_message_error(msg: Message, state: FSMContext):
    """Хендлер сработает если пользователь скинет не текстовые данные."""
    await msg.reply(text=Messages.table_get_birthday_type_error)
    await state.set_state(GetUserBirthDateForTable.get_date)


@router.message(Command("tableupdate"))
async def update_user_table(msg: Message, state: FSMContext):
    user: dict = await get_user_by_chat_id(chat_id=msg.chat.id)
    if user.get("birthday_date"):
        date: str = reformat_user_date(date=user["birthday_date"])
        table_data: dict = create_table(username=msg.from_user.username, date=date)
        await send_table_or_error(table_data=table_data, msg=msg)
    else:
        await msg.reply(text="Функция недоступна")