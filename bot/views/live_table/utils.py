from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile
import aiohttp

from datetime import datetime
from typing import Optional, Dict
import io
import json

from config import QueueSettings, AppViewsPaths, BotSettings
from ..amqp_broker import broker
from utils.print_live_table import LiveTableDraw

async def save_user_birthday_by_chat_id(chat_id: int, birthday: str) -> None:
    dict_data = {"chat_id": chat_id, "birthday": birthday}
    string: str = json.dumps(dict_data)
    await broker.publish(message=string, queue=QueueSettings.birthday_queue)


def validate_date_format(date: str, format: str = "%d/%m/%Y") -> Optional[str]:
    """Проверка формата даты из строки date"""
    try:
        datetime.strptime(date, format)
        return None
    except ValueError as ext:
        print(ext)
        return f"Неверный формат даты {ext}"


def create_table(date: str, username: str) -> Dict[str, io.BytesIO | None | str | list]:
    """Функция создающая файл с таблицей. Возвращает словарь с таблицей, статусом создания, и ошибками."""
    errors = []
    date_error = validate_date_format(date=date)
    if date_error:
        errors.append(date_error)
        return {"table": None, "is_created": False, "errors": errors}
    table = LiveTableDraw(name=username, birthday_date=date)
    table_image = table.create_table()
    return {"table": table_image, "is_created": True, "errors": errors, "date": date}


async def send_table_or_error(
    table_data: Dict[str, io.BytesIO | None | str | list], msg: Message, state: FSMContext | None = None
) -> None:
    """Функция которая скидывает таблицу в чат пользователю или
    оправляет ему сообщение об ошибке формата введённой им даты"""
    if table_data.get("errors"):
        await msg.answer(
            "Ты скинул что то не то, формат даты должен быть <b>03/09/2008</b>."
        )
        return None

    await msg.bot.send_document(
        chat_id=msg.chat.id,
        document=BufferedInputFile(
            file=table_data["table"].getvalue(), filename="table.png"
        ),
    )
    await save_user_birthday_by_chat_id(chat_id=msg.chat.id, birthday=table_data["date"])
    if state is not None:
        await state.clear()
    return None


async def get_user_by_chat_id(chat_id: int) -> Dict[str, int | str | None]:
    url: str = BotSettings.app_url + AppViewsPaths.get_user_by_chat_id.format(chat_id=chat_id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            result_bytes: bytes = await response.read()
            if response.status != 200:
                return {}
            return json.loads(result_bytes)


def reformat_user_date(date: str) -> str:
    # Преобразуем строку в объект даты
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    # Форматируем в нужный вид
    return date_obj.strftime("%d/%m/%Y")